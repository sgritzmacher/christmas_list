from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Gift
from ..users.models import User


def index(req):
    if 'user_id' not in req.session:
        return redirect('/users/new')

    # DO NOT CHANGE
    context = {
        'user_wishlist' : Gift.objects.filter(wishlist_users__id=req.session['user_id']),
        'other_gifts' : Gift.objects.exclude(wishlist_users__id=req.session['user_id']),
        'welcome' : User.objects.get(id=req.session['user_id']),
        # 'person' : Gift.objects.filter(creator="first_name"),
        # 'wish_list' : Gift.objects.
    }

    return render(req, 'gifts/index.html', context)
 
 #variable in context other_gifts just done in dictionary but is gatewy to pass info from query
 #query accesses model wishlist_users it asks for session and user id uses .filter because we 
 #want the items we selected.

 #other_gifts query .exclude we don't want what we have we want everyone elses picks

# def delete(req):
#     req.session.delete()
#     return redirect('/')

#i want to clear - route completed url to views.  we need to acknowledge the person logged in and others
#how do we accomplish this? 
#above code logs out because req.session is the whole session of user it doesn't isolate contents

#start over what do i know....
#how do i get a variable into the query? such as other_gifts, other_gifts is settled and moves to html
#not sure
#plan could be to construct .delete method and figure out query that attaches and deletes


def delete(req):
    Gift.objects.delete(req.POST['gift_id'])
    return redirect('/')

#i think we start in models we want to create a method delete
#utilize structure of remove with focus of remove from DB. stuck remove doesn't address
#how to include others list?  
#thought of passing another value such as variable for others but fall short of how to construct
#query around variable inside views.



def remove(req):
    print(req.POST)
    Gift.objects.remove(req.POST['gift_id'], req.session['user_id'])
    return redirect('/')




def logout(req):
    req.session.clear()
    return redirect('/users/new')



def add_newitem(req):
    return render(req, 'gifts/')
  
 

def add_item(req):
    print(req.POST)
    Gift.objects.add_item(req.POST['gift_id'], req.session['user_id'])
    return redirect('/')

def items(req):
    return render(req, 'gifts/items.html')




def create(req):
    errors = Gift.objects.validate(req.POST)
    if len(errors) > 0:
        for error in errors:
            messages.error(req, error)
    else:
        Gift.objects.create_item(req.POST, req.session['user_id'])
    
    return redirect('/')


def logout(req):
    req.session.clear()
    return redirect('/users/new')




def close_ups(req):

    return render(req, 'gifts/close_ups.html')
    pass
