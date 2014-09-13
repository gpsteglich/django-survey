from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response

def user_login(request):
    
    #get context for the user's request
    context = RequestContext(request)
    
    if request.method == 'POST': 
        #get data from login form
        username = request.POST['username']
        password = request.POST['password']
        
        #check if user is valid
        user = authenticate(username=username, password=password)
        
        #if there is a user object, its correct
        #if None, no user with matching data was found
        if user:
            #if account active
            if user.is_active():
                #login and send user to mainpage 
                login(request, user)
                return HttpResponseRedirect("/mainpage/")
            
            else:
                #an inactive account was used- no login in.
                return HttpResponse("Your account is disabled.")
        else:
            #bad login 
            return HttpResponse("Invalid username/password.")
        
    else:
        #method wasnt POST
        return render_to_response('/login.html', {}, context)
            
   
               
                       
            
