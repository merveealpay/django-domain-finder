from django.urls import path
from applications.finder import views

urlpatterns = [
    path('', views.DomainView.as_view(), name='all_domain'),
    path('provider/', views.ProviderView.as_view(), name='all_provider')
]