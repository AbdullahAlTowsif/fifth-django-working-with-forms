from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('about/', views.about, name="aboutpage"),
    path('from/', views.submit_form, name="submit_form"),
    path('django_form/', views.StudentForm, name="django_form"),
    # path('django_form/', views.DjangoForm, name="django_form"),
]
