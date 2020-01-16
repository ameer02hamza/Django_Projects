from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('bhome', views.blog, name='blogs'),
    path(r'detailblog/<int:id>', views.detailview, name="detailblog"),
    path(r'logout', views.logout, name='logout'),
    path(r'addblog', views.addblog, name="addblog"),
    path(r'updateblog/<int:id>', views.editview, name="updateblog"),
    path(r'delete/<int:id>', views.delete, name="delete"),
    path(r'comnt/<int:id>', views.deletecom, name="deletecom"),
]