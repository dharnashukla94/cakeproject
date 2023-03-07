from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
def setcookie(request):
    response= render(request, 'setcookie.html')
    #instead of returning it, we will save it in a response variable
    response.set_cookie('name', 'django')
    return response

def getcookie(request):
    nm = request.COOKIES['name']
    return render(request, 'getcookie.html', {'xyz': nm})

def delcookie(request):
     response=render(request, 'delcookie.html')
     response.delete_cookie('name')
     return response

def my_view(request):
    request.session['lastname'] = 'Shukla'
    # session_id = request.session.session_key


def my_other_view(request):
    my_view(request)
    # Retrieve a value from the session
    value = request.session.get('lastname')
    return render(request, 'sessiondemo.html', {'session_id': value})

def my_third_view(request):
    # Remove a value from the session
    del request.session['firstname']
    return render(request, 'deletesession.html')






