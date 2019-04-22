# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth import authenticate, login

from .forms import ClientSignUp


# Create function where each function will represent a view
def base(request):
    # load base into the page variable
    page = loader.get_template('polls/base.html')

    # rendering the template in httpResponse
    return HttpResponse(page.render())


# def sign_up(request):
# load signUp template in page variable
#   page = loader.get_template('polls/signup.html')

# render page in httpResponse
#  return HttpResponse(page.render())


def sign_up(request):
    # if this is a POST request we need to process the form data

    if request.method == 'POST':
        # create a form instance and populate it with the data from the request
        form = ClientSignUp(request.POST)

        # check if the form is valid(was filled up)
        if form.is_valid():
            # process the data in form.cleaned_data
            form.save()
            # redirect
            return HttpResponse('polls/signin.html')
    else:
        form = ClientSignUp()
        context = {'form': form}
        return render(request, 'polls/signup.html', context)


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # redirect to a success page (index)
            return render(request, 'polls/location.html')
        else:
            # error message wrong password
            message = 'Wrong password'
            context = {'message': message}
            return HttpResponse('polls/signin', context)
    else:

        return render(request, 'polls/signin.html')


def location(request):
    if request.method == 'POST':

        return HttpResponse(request, '')

    else:

        return render(request, 'polls/location.html')


def order(request):
    if request.method == 'POST':
        return HttpResponse(request, '')

    else:
        return render(request, 'polls/order.html')
