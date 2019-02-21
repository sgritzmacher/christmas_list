from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.

def index(req):
    if 'user_id' not in req.session:
        return redirect('/users/new')

    return render(req, 'users/index.html')      #, context add if activate above


def new(req):
    return render(req, 'users/new.html')



def create(req):
    errors = User.objects.validate(req.POST)
    if len(errors) > 0:
        #flash all error messages
        for error in errors:
            messages.error(req, error)
        
     
    else:
        # has password and create user
        user = User.objects.create_user_with_hashed_password(req.POST)
        req.session['user_id'] = user.id 
        return redirect('/')                            #same as line 39 ('/users')

    return redirect('/users/new')
    

def login(req):
    valid, result = User.objects.login(req.POST)        #changed from - info = User.objects.login(req.POST)
    if valid == False:                                  #changed from - if info[0] == False:
        for error in result:                            #changed from - for error in info[1]:
            messages.error(req, error)
    else:                                               #? in breaking down above the valid and result are set to User.objects and as result it simplifies the following lines
        req.session['user_id'] = result.id              #takes the variable validated below login f(x) info[1].id
        return redirect('/')                            # wes? is this right? change because of posts url ('/users')

    return redirect('/users/new')



