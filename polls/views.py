# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import ClientSignUp, ClientSignIn, UploadFile
from django.core.files.storage import FileSystemStorage


# Create function where each function will represent a view
def base(request):
    # load base into the page variable
    page = loader.get_template('polls/index.html')

    # rendering the template in httpResponse
    return HttpResponse(page.render())


def sign_up(request):
    # if this is a POST request we need to process the form data

    if request.method == 'POST':
        # create a form instance and populate it with the data from the request
        form = ClientSignUp(request.POST)

        # check if the form is valid(was filled up)
        if form.is_valid():
            # process the data in form.cleaned_data
            form.save()

            # create user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            user = User.objects.create_user(username, email, password)

            # save user
            user.save()

            # redirect
            return render(request, 'polls/signin.html')
    else:
        form = ClientSignUp()
        context = {'form': form}
        return render(request, 'polls/signup.html', context)


def sign_in(request):
    # Process information if Post method is used
    if request.method == 'POST':

        # Set username and password to user input
        username = request.POST['username']
        password = request.POST['password']

        # Send authentication request through django
        user = authenticate(request, username=username, password=password)

        # If user exist in db return user landing page
        if user is not None:

            # log user in
            login(request, user)

            # redirect to a success page (index)
            return render(request, 'polls/citiexpress.html')
        else:
            # error message wrong password or username
            message = 'Wrong Username/password'
            context = {'message': message}
            return render(request, 'polls/signin.html', context)
    else:
        # if request is a GET reload form and display signin
        form = ClientSignIn()

        context = {'form': form}
        # is any other issues redirect to signin page
        return render(request, 'polls/signin.html', context)


def location(request):
    if request.method == 'POST':

        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)

        return HttpResponse(request, '')

    else:

        return render(request, 'polls/location.html')


def order(request):
    if request.method == 'POST':
        return HttpResponse(request, '')

    else:
        return render(request, 'polls/order.html')


def citiexpress(request):
    if request == 'POST':

        return HttpResponse('polls/citiexpress.html')

    else:

        return render(request, 'polls/citiexpress.html')


def sign_out(request):
    logout(request)
    message = 'You are now logged out!'
    context = {
        "message": message
    }
    return render(request, 'polls/index.html', context)


def about(request):
    return render(request, 'polls/about.html')


def aide(request):
    return render(request, 'polls/help.html')
