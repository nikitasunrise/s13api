from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404, render

from api.models import BlogPost


def mainpage(request):
    header = "Main page"
    users = User.objects.all()
    return render_to_response('index.html', {'users': users, 'header': header})


def msg(request, user_id):
    posts = BlogPost.objects.filter(own_user_id=user_id)
    return render_to_response('user.html', {'posts': posts})


def history(request):
    msgs = BlogPost.objects.all()
    return render_to_response('history.html', {'msgs': msgs})


#def auth_login(request):
#
