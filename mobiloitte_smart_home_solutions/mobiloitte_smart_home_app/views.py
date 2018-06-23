from django.shortcuts import render
from django.views import View
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from random import randint
from .models import AppUser
from .forms import LoginForm
# Create your views here.

class AlexaLogin(View):
    """View for Alexa Login"""
    def get(self,request):
        #global state
        #state = request.GET['state']
        return render(request,'login.html')
    
    def post(self,request):
        params = request.POST
        form = LoginForm(params or None)
        user = authenticate(email=params['email'], password=params['password'])
        if user:
            serializer = LoginSerializer(user)
            print(user.create_jwt())
            return redirect("https://pitangui.amazon.com/spa/skill/account-linking-status.html?vendorId=M2MDDCSGAS3C8H"+"#access_token="+user.create_jwt()+"&state="+state+"&token_type=JWT")
        return render(request,'login.html',{"message":"Your credential are not correct"})  
