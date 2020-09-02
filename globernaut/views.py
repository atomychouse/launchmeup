# -*- encoding: utf-8 -*-

from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import (render, redirect, get_object_or_404)
from django.views.generic.base import TemplateView
from school.utils import (FormCreator)

class Login(TemplateView):
    def post(self, request):
        if request.POST.get('username', 'martin')=='martin':
            return redirect('/globernautup/')
        else:
            return redirect('/globernaut/')
    def get(self, request):
        context = {}
        return render(request, 'globernaut/login.html', context)

class Bplan(TemplateView):
    def get(self, request):
        context = {}
        context['menu'] = [
            ('idea','Home'),
            ('bplan','Canvas BModel'),
            ('emp','Empathy Maps'),
            ('swot','SWOT'),
        ]
        return render(request, 'globernaut/bplan.html', context)

class Emp(TemplateView):
    def get(self, request):
        context = {}
        context['menu'] = [
            ('idea','Home'),
            ('bplan','Canvas BModel'),
            ('emp','Empathy Maps'),
            ('swot','SWOT'),
        ]
        return render(request, 'globernaut/emp.html', context)

class Home(TemplateView):
    def get(self, request):
        context = {}
        context['menu'] = []
        advance = [
            {
            'training':50,
            'creating':10,
            },
            {
            'training':20,
            'creating':0,
            },
            {
            'training':100,
            'creating':100,
            },
            {
            'training':100,
            'creating':100,
            },

        ]
        globernaut = request.GET.get('g', 0)
        context['advance'] = advance[int(globernaut)]
        return render(request, 'globernaut/home.html', context)

class Idea(TemplateView):
    def get(self, request):
        context = {}
        context['menu'] = [
            ('idea','Home'),
            ('bplan','Canvas BModel'),
            ('emp','Empathy Maps'),
            ('swot','SWOT'),
        ]
        return render(request, 'globernaut/idea.html', context)

