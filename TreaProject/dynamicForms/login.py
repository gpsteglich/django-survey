from django.httpb import HttpResponse

def login(request):
    
    if request.method == 'POST': 
        if (request.POST['username'] == 'admin' and 'admin' == request.POST['password']): 
            request.session['admin_id'] = 2
            return HttpResponse("You're logged in.")    
        else:          
            return HttpResponse("User and password didn't match.")   
    else: 
        return HttpResponse("Login page.")