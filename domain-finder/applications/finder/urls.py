from django.urls import path, include
from rest_framework.routers import DefaultRouter
from applications.finder.views import DomainViewSet

from applications.finder import views

router = DefaultRouter()
router.register(r'domains', views.DomainViewSet)
router.register(r'providers', views.ProviderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]