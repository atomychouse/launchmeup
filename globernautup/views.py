# -*- encoding: utf-8 -*-

from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import (render, redirect, get_object_or_404)
from django.views.generic.base import TemplateView
from school.utils import (FormCreator)

IDEAS = [
    {
        'id':1,
        'name':'Great Idea',
        'authors':[
            'CTO: Juan',
            'CEO: Pedro Palacios'
        ],
        'points':0,
        'advance':{
            'training':10,
            'creating':10,
            }
        ,'team':[
            {
                'name':'Glober 1',
                'position':'CEO',
                'since':'3 weeks',
                'glow':'glow/link'
            },
            {
                'name':'Glober 2',
                'position':'CTO',
                'since':'Fundator',
                'glow':'glow/link'
            },
            {
                'name':'Glober 3',
                'position':'TECHNICAL',
                'since':'9 months',
                'glow':'glow/link'
            },
        ]
    },
    {
        'id':2,
        'name':'Another Great Idea',
        'authors':[
            'CTO: FER',
        ],
        'points':230,
        'advance':{
            'training':75,
            'creating':10,
            }
        ,'team':[
            {
                'name':'Glober 1',
                'position':'CEO',
                'since':'3 weeks',
                'glow':'glow/link'
            },
            {
                'name':'Glober 2',
                'position':'CTO',
                'since':'Fundator',
                'glow':'glow/link'
            },
            {
                'name':'Glober 3',
                'position':'TECHNICAL',
                'since':'9 months',
                'glow':'glow/link'
            },
        ]

    },
    {
        'id':3,
        'name':'More Great Ideas',
        'authors':[
            'CTO: ',
        ],
        'points':0,
        'advance':{
            'training':100,
            'creating':10,
            }
        ,'team':[
            {
                'name':'Glober 1',
                'position':'CEO',
                'since':'3 weeks',
                'glow':'glow/link'
            },
            {
                'name':'Glober 2',
                'position':'CTO',
                'since':'Fundator',
                'glow':'glow/link'
            },
            {
                'name':'Glober 3',
                'position':'TECHNICAL',
                'since':'9 months',
                'glow':'glow/link'
            },
        ]

    }

]

class Home(TemplateView):
    def get(self, request):
        context = {}
        context['ideas'] = IDEAS
        return render(request, 'globernautup/home.html', context)

class Idea(TemplateView):
    def get(self, request, id=0):
        context = {}
        id = int(id) - 1
        context['idea'] = IDEAS[int(id)]
        return render(request, 'globernautup/idea.html', context)

class Emp(TemplateView):
    def get(self, request):
        context = {}
        return render(request, 'globernautup/emp.html', context)

