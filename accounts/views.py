from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,FormView
from .forms import *
from django.contrib.auth import authenticate,login
from django.urls import reverse_lazy
from django.forms import BaseModelForm
# Create your views here.

class LandingView(TemplateView):
    template_name="landing.html"



class LoginView(FormView):
    template_name="log.html"
    form_class=LogForm
    def post(self,request):
        form_data=LogForm(data=request.POST)
        if form_data.is_valid():
            uname=form_data.cleaned_data.get('username')
            pswd=form_data.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pswd)
            if user:
                login(request,user)
                return redirect('home')
            else:
                return redirect('log')
        return render(request,"log.html",{"form":form_data})

class RegView(CreateView):
    template_name="register.html"
    form_class=RegForm
    success_url=reverse_lazy('log')
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_valid(form)
    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_invalid(form)
