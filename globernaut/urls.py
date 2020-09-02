from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import  path
from .views import *


urlpatterns = [
    path(r'bplan/', Bplan.as_view(), name='bplan'),
    path(r'emp/', Emp.as_view(), name='emp'),
    path(r'swot/', Emp.as_view(), name='swot'),
    path(r'', Home.as_view(), name='home'),
    path(r'idea/', Idea.as_view(), name='idea'),
    #path(r'delete/<str:folio>', rmAlumno.as_view(), name='delete'),
    path(r'', Home.as_view(), name="home"),
]
