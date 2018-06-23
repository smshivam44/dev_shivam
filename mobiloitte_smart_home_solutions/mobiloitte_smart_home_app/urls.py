from django.conf.urls import url
from .views import *

urlpatterns = [
   
    url(r'^alexa-login', AlexaLogin.as_view(), name="alexa-login"),

]