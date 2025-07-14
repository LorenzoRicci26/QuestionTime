from rest_framework import viewsets, generics, status
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from questions.models import Question, Answer
from questions.api.serializers import QuestionSerializer, AnswerSerializer
from rest_framework.permissions import IsAuthenticated
from questions.api.permissions import IsAuthorOrReadOnly
from rest_framework.views import APIView
from rest_framework import response

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('-created_at')
    serializer_class = QuestionSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get('slug')
        question = get_object_or_404(Question, slug=kwarg_slug)
        if question.answers.filter(author=request_user).exists():
            raise ValidationError("You have already answered to this question")
        
        serializer.save(author=request_user, question=question)

class AnswerListAPIView(generics.ListAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get('slug')
        return Answer.objects.filter(question__slug=kwarg_slug).order_by('-created_at')
    
class AnswerRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    lookup_field = 'id'

class AnswerLikeAPIView(APIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def post(self, request, id):
        answer = get_object_or_404(Answer, id=id)
        answer.voters.add(self.request.user)
        answer.save()
        serializer_context = {"request": request}
        serializer = self.serializer_class(answer, context=serializer_context)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        answer = get_object_or_404(Answer, id=id)
        answer.voters.remove(self.request.user)
        answer.save()
        serializer_context = {"request": request}
        serializer = self.serializer_class(answer, context=serializer_context)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    