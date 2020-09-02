from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import  path
from .views import *


urlpatterns = [
    path(r'idea/<str:id>/', Idea.as_view(), name='gup_idea'),
    #path(r'addalumno/', AddAlumno.as_view()),
    #path(r'auth/', AuthParent.as_view()),
    #path(r'parent/', ParentHome.as_view(), name='parent'),
    #path(r'pagos/', ParentPagos.as_view(), name='pagos'),
    #path(r'logout/', Logout.as_view(), name='logout'),
    #path(r'delete/<str:folio>', rmAlumno.as_view(), name='delete'),
    path(r'', Home.as_view(), name="globernautup"),
]
