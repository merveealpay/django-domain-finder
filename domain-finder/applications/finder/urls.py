from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.finder import views

# urlpatterns = [
#     path('', views.DomainViewSet, name='all_domain'),
#     path('<int:pk>/', views.DomainDetailView.as_view()),
#     path('provider/', views.ProviderView.as_view(), name='all_provider'),
#     path('provider/<int:pk>/', views.ProviderDetailView.as_view()),
# ]
from applications.finder.views import DomainViewSet

router = DefaultRouter()
router.register(r'domains', views.DomainViewSet)
router.register(r'providers', views.ProviderViewSet)

urlpatterns = [
    path('', include(router.urls)),

]