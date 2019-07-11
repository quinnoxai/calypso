from django.shortcuts import render,reverse
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.http import HttpResponse
#from .insert import create_tablet
from django.views.decorators.csrf import csrf_exempt

from .status_fetch import fetch_status
#from .status_fetch import fetch_date_time
#from .status_fetch import fetch_status_name
import datetime,os,json,time
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

#from .welcome_message.showmessage import show_welcome_message
from .main_action_faq import get_response
from .models import IntentFeedback,LetterTable,EmployeeFeedback
from .check_if_empty import is_empty
# Create your views here.

def homepage(request):
    # print("user name",request.session["user"])
    request.session["pre_state"] = {}
    return render(request, "home.html")

#----login over---

## logout view
# @api_view(['GET','POST'])

##function to get the userdata and welcome message

"""@api_view(["GET","POST"])
def get_welcome_message(request):
  #access_token = get_access_token(request, request.build_absolute_uri(reverse('gettoken')))
  # If there is no token in the session, redirect to home

    return HttpResponseRedirect(reverse('home'))"""




###chatview

@api_view(['GET', 'POST'])
@csrf_exempt
def chat(request):
    if request.method == 'GET':
        return Response(status=status.HTTP_403_FORBIDDEN,data={"message":"error"})
    elif request.method == 'POST':
        input_dict = request.data
        print("here in post",input_dict)
        dict_rec=request.session["pre_state"]
        #user_info=request.session["user_info"]
        dict_rec=get_response(input_dict["message"],dict_rec)
        request.session["pre_state"]=dict_rec
        if "response_complete" not in dict_rec:
            request.session["pre_state"]={}

        print("dc in views",dict_rec)




        return HttpResponseForbidden(status=status.HTTP_200_OK, data=dict_rec)



@api_view(['GET','POST'])
def refresh_view(request):
    # print("Here in refresh")

    if "dict_rec" in request.session:
        # print("Here in refresh view", request.session["dict_rec"])
        request.session["dict_rec"]={}
        # del request.session["dict_rec"]
        # print("Deleted")
    return Response(status=status.HTTP_200_OK)
	
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # print(request.data)
            user = form.get_user()
            username = user.username
            print("Username is:",username)
            login(request,user)
            response=redirect("/helpdesk/home")
            print(response)
            return response
    else:
        form = AuthenticationForm()
    return render(request,"login.html",{'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        response=redirect("/login")
        return response
