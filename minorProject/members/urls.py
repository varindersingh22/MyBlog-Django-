from django.urls import path
from .views import UserRegisterView,UserEditView,ShowProfilePageView,EditProfilePageView,CreateProfilePageView

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('edit_profile/',UserEditView.as_view(),name='edit_profile'),
    path('<int:pk>/profile/',ShowProfilePageView.as_view(),name='show_profile'),
    path('<int:pk>/edit_profile_page/',EditProfilePageView.as_view(),name='edit_profile_page'),
    path('create_profile_page/',CreateProfilePageView.as_view(),name='create_profile_page'),
]