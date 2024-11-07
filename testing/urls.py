from tkinter.font import names

from django.urls import path
from testing import views


urlpatterns=[
    path('',views.home,name='my_home'),
    path('about/',views.about,name='my_about'),

    path('blog/',views.blog,name='my_blog'),
    path('contact/',views.contact,name='my_contact'),
    path('events/',views.events,name='my_events')


]
