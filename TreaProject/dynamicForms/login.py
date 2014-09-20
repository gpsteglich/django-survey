from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def user_login(request):
    
    #get context for the user's request
    context = RequestContext(request)
    
    if request.method == 'POST': 
        #get data from login form
        username = request.POST['username']
        password = request.POST['password']
        #check if user is valid
        _user = authenticate(username=username, password=password)
        
        #if there is a user object, its correct
        #if None, no user with matching data was found
        if _user:
            if _user.is_active:
                #login and send user to mainpage 
                login(request, _user)
                return HttpResponseRedirect("/dynamicForms/mainPage/")
            else:
                #an inactive account was used- no login in.
                return HttpResponse("Your account is disabled.")
        else:
            #bad login 
            return render_to_response('login.html', {'error': True}, context)
    else:
        #method wasnt POST
        return render_to_response('login.html', {"error": False}, context)
            
   
               
                       
            
