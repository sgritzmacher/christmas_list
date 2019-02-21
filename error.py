

#conversation pieces

# quick layout of cycle

#following validation and login registration

#1.
#views/index of app where action takes place such as a dashboard/index (gifts)
#context{ create variables for html to run info from DB}

#html
#you can see these items as a simple heading or in a for loop - convert static html.

#2.
#action to the dash

#models
#create a function that passes self, form , and locks with user_id 
#import user table to get user id link between tables
#dictionary to specify specific column names and create variables we will need for further actions

#views
#functions 
#need item and create = also verify urls accommodate
#1 for grabbing items and send to dash
#a create route this processes the info/ contents of function include a query that uses model function
#with logged in reference its purpose is to grab the list of info from models function and upload
#into html this looks like = my wishlist of items personal to me being logged in

#3
#add item from other list to my own - this is an action - in the form of a button
#models
#create def add_items function and pass; self , gift_id, user_id which inside the function 
#store queries that lock on elements in Gift model and users app/ User model and final query
#acknowledges the relationship quer and says .add (method) this to user created from create_item function

#views
#create function add_item
#this sets up the button to push info that has grabbed from gift_id and user_id)

#html
#create form use "/add_item/" all forms start with slash
#this is form inside table
#input type="hidden"
#name="gift_id" this was used in models 