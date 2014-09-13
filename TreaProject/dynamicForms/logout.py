from django.contrib.auth import logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Use the login_required() decorator to ensure only those logged in can access the view.

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/dynamicForms/login/')
