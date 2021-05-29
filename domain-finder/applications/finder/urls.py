from django.urls import path
from applications.finder import views

urlpatterns = [
    path('', views.DomainView.as_view(), name='all_domain'),
    path('<int:pk>/', views.DomainDetailView.as_view()),
    path('provider/', views.ProviderView.as_view(), name='all_provider'),
    path('provider/<int:pk>/', views.ProviderDetailView.as_view()),
]