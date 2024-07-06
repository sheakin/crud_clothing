from django.urls import path
from .views import *
urlpatterns = [
    path('home',HomeView.as_view(),name='home'),
    path('auser',Add_User.as_view(),name="auser"),
    path('ulist',UserList.as_view(),name="ulist"),
    path('udel<int:uid>',UserRemove.as_view(),name="udel"),
    path('uedit<int:uid>',UpdateUser.as_view(),name="uedit")

]