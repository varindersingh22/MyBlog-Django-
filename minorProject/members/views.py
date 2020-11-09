from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.urls import reverse,reverse_lazy
from .forms import SignUpForm
from myblog.models import Profile

# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class= SignUpForm
    template_name='registration/register.html'
    success_url= reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class= UserChangeForm
    template_name='registration/edit_profile.html'
    success_url= reverse_lazy('home')

    def get_object(self):
        return self.request.user

class ShowProfilePageView(generic.DetailView):
    model = Profile 
    template_name='registration/user_profile.html'

    def get_context_data(self,*args,**kwargs):
        users=Profile.objects.all()
        context= super(ShowProfilePageView,self).get_context_data(*args,**kwargs)
        page_user = get_object_or_404(Profile,id=self.kwargs['pk'])
        context["page_user"]=page_user
        return context
class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name="registration/edit_profile_page.html"
    fields = ['profile_pic','bio','website_url','fb_url','insta_url','pinterest_url','twitter_url']
    success_url = reverse_lazy('home')

class CreateProfilePageView(generic.CreateView):
    model = Profile
    template_name="registration/create_user_profile_page.html"
    fields ='__all__'
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)