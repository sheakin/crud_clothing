from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,FormView
from .forms import *
from django.urls import reverse_lazy
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views import View



# Create your views here.
class HomeView(TemplateView):
    template_name="home.html"

class Add_User(CreateView):
    template_name="add_user.html"
    form_class=UserForm
    success_url=reverse_lazy('home')
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_valid(form)
    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_invalid(form)

class UserList(View):
    def get(self,request):
        data=A_User.objects.all()
        return render(request,"userlist.html",{"ur":data})

class UserRemove(View):
    def get(self,request,*args,**kwargs):
        uid=kwargs.get('uid')
        ud=A_User.objects.get(id=uid)
        ud.delete()
        return redirect('ulsit')

class UpdateUser(View):
    def get(self,request,*args,**kwargs):
        uid=kwargs.get('uid')
        us=A_User.objects.get(id=uid)
        form=UserForm(instance=us)
        return render(request,"useredit.html",{"form":form})
    def post(self,request,*args,**kwargs):
        uid=kwargs.get('uid')
        us=A_User.objects.get(id=uid)
        form_data=UserForm(data=request.POST,instance=us)
        if form_data.is_valid():
            form_data.save()
            return redirect('ulist')
        return render(request,"useredit.html",{"form":form_data})



