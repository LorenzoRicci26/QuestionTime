from django.urls import include, path
from rest_framework.routers import DefaultRouter

from questions.api import views as qv

router = DefaultRouter()
router.register(r'questions', qv.QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'questions-answers/<slug:slug>/', 
        qv.AnswerCreateAPIView.as_view(), 
        name="answer-create"
    ),
    path(
        'questions-new-answer/<slug:slug>/', 
        qv.AnswerListAPIView.as_view(), 
        name="answer-list"
    ),
    path(
        'answers-detail/<uuid:id>/', 
        qv.AnswerRetrieveUpdateDeleteAPIView.as_view(), 
        name="answer-detail"
    ),
    path(
        'answers-like/<uuid:id>/', 
        qv.AnswerLikeAPIView.as_view(), 
        name="answer-like"
    )
]
