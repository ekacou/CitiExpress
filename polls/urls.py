from django.conf.urls import url
from .views import base
from .views import sign_up
from .views import sign_in
from .views import location
from .views import order
from .views import citiexpress
from .views import sign_out
from .views import about
from .views import aide


urlpatterns = [

    url('index/', base, name='base_page'),
    url('signup/', sign_up, name='sign_up_page'),
    url('signin/', sign_in, name='sign_in_page'),
    url('signout/', sign_out, name='sign_out'),
    url('location/', location, name='location_page'),
    url('order/', order, name='order result page'),
    url('citiexpress/', citiexpress, name='citiexpress'),
    url('about/', about, name='about_page'),
    url('help/', aide, name='Help_page'),
]
