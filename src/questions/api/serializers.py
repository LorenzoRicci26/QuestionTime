from rest_framework import serializers
from questions.models import Question, Answer  

class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    created_at = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    user_has_liked_answer = serializers.SerializerMethodField()
    question_slug = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = [
            "id",
            "body",
            "question",
            "author",
            "voters",
            "user_has_liked_answer",
            "likes_count",
            "question_slug",
            "created_at",
            "updated_at"
        ]

    def get_created_at(self, instance):
        return instance.created_at.strftime('%d-%B-%Y')
    
    def get_answers_count(self, instance):
        return instance.answers.count()

    def get_likes_count(self, instance):
        return instance.voters.count()
    
    def get_user_has_liked_answer(self, instance):
        request = self.context.get('request')
        return instance.voters.filter(pk=request.user.pk).exists()

    def get_question_slug(self, instance):
        return instance.question.slug
    
class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    answers_count = serializers.SerializerMethodField()
    user_has_answered = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = [
            "id",
            "content",
            "slug",
            "author",
            "answers_count",
            "user_has_answered",
            "created_at",
        ]

    def get_created_at(self, instance):
        return instance.created_at.strftime('%d-%B-%Y')
    
    def get_answers_count(self, instance):
        return instance.answers.count()
    
    def get_user_has_answered(self, instance):
        request = self.context.get('request')
        return instance.answers.filter(author=request.user).exists()