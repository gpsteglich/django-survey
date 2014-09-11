from django.http import HttpResponse


def logout(request):
    
    try:
        del request.session['admin_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")