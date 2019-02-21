from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^items/$', views.items, name="items"),
    url(r'^create/$', views.create, name="create"),
    url(r'^add_item/$', views.add_item, name="add_item"),
    url(r'^remove/$', views.remove, name="remove"),
    url(r'^close_ups/$', views.close_ups, name="close_ups"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^delete/$', views.delete, name="delete"),

]
    # url(r'^$', views.index, name="index"), why - the BASE where home resides for site
    # url(r'^create/$', views.create, name="create"), why - processing the new item 
    # url(r'^gifts/$', views.gift, name="gift"), why - we are adding a new item
    # url(r'^actions/$', views.action, name="action"), why - alteration in DB access to traffic urls / link
    # url(r'^removes/$', views.remove, name="remove"), why - alteration in DB access to traffic urls / link
    # url(r'^close_ups/$', views.close_up, name="close_up"), why - this is a view restroute avoided views.view
    # url(r'^logout/$', views.logout, name="logout"), why - safely log out a secure way of out with session
    # url(r'^home/$', views.home, name="home"), NO, this is because it is html that brings us back home simple