
from django.http import HttpResponse, HttpResponseRedirect


def login(request):
    
    if request.method == 'POST': 
        if (request.POST['username'] == 'admin' and 'admin' == request.POST['password']): 
            request.session['admin_id'] = 2
            return HttpResponseRedirect("mainpage.html")    
        else:
            return HttpResponseRedirect("mainpage.html")   
    else: 
        return HttpResponseRedirect("login.html")
