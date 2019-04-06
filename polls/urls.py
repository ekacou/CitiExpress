from django.conf.urls import url
from .views import base
from .views import sign_up
from .views import sign_in
from .views import location

urlpatterns = [

    url('index/', base, name='base_page'),
    url('signup/', sign_up, name='sign_up_page'),
    url('signin/', sign_in, name='sign_up_page'),
    url('location/', location, name='main location page'),
]
