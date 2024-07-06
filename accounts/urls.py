from django.urls import path,include
from .views import *
urlpatterns = [
    path('log',LoginView.as_view(),name="log"),
    path('reg',RegView.as_view(),name="reg")

]
