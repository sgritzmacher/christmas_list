from django.db import models
from ..users.models import User

class GiftManager(models.Manager):
    def validate(self, form):
        errors = []

        if len(form['gift']) < 1:
            errors.append('Please type in your Christmas item here!')

        return errors

    def create_item(self, form, user_id):   
        print('USER_ID', user_id)
        user = User.objects.get(id=user_id)
        gift = self.create(
            name = form['gift'],
            creator = user
            
        )
        gift.wishlist_users.add(user)

    def add_item(self, gift_id, user_id):
        gift = Gift.objects.get(id=gift_id)
        user = User.objects.get(id=user_id)
        gift.wishlist_users.add(user)
        

    def remove(self, gift_id, user_id):
        gift = Gift.objects.get(id=gift_id)
        user = User.objects.get(id=user_id)
        gift.wishlist_users.remove(user)

#so in creating the .delete method the code below must acknowledge session logged in and access to 
#other_users
#this code covers the session however not the other_users im thinking from views level we will 
#have to create a query.  alter from .get to .all method.
#test: failed
#error - queryset, wishlist_users - object has no attribute
#this means that wishlist_user is not pulling from model correctly like in other functions 
#in order for .delete to work i need to draw from User and Gift .wishlist_users should work

    def delete(self, gift_id):
        gift = Gift.objects.get(id=gift_id)
        gift.delete()
        




class Gift(models.Model):
  name = models.CharField(max_length=255)
  creator = models.ForeignKey(User, related_name="created_items")
  wishlist_users = models.ManyToManyField(User, related_name="wishlist_items")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = GiftManager()

  def __str__(self):
      return self.name

# gift = Gift.objects.get(id=1)
# gift.wishlist_users.all()