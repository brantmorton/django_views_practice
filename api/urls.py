from django.urls import path, include
from .views import ArticleAPIView, ArticleDetails, ArticleViewSet, article_list, article_detail

from rest_framework import routers

router = routers.DefaultRouter()
router.register('', ArticleViewSet)

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('apiview/', ArticleAPIView.as_view()),
    path('apiview/<int:id>/', ArticleDetails.as_view()),
    path('', article_list),
    path('<int:pk>/', article_detail)
]