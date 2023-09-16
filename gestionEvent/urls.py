from django.urls import include, path
from . import views
from .views import *

urlpatterns = [
    #Path for all GET methods
    path('dashboard/', views.dashboard, name="dashboard"),
    path('index/', views.index, name="index"),
    path('profile/', views.profile, name="profile"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('change_password/', views.change_password, name="change_password"),

    #path for admin urls
    path('admin_profile/', views.admin_profile, name="admin_profile"),
    path('edit_admin_profile/', views.edit_admin_profile, name="edit_admin_profile"),

    #EVENT
    path('create/', views.create_event, name='create_event'),
    path('events/delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('events/', views.event_list, name='event_list'),
    path('events/edit/<int:pk>/', EventUpdateView.as_view(), name='event_edit'),
    path('reservations/', views.reservation, name='reservation'),
    path('create_restauration/', views.create_restauration, name='create_restauration'),
    path('restaurations/', views.restauration, name='restauration'),
    #CATEGORY
    path('create_category/', views.create_event_category, name='create_event_category'),
    path('events_category/', views.event_list_category, name='event_list_category'),
    path('events_category/delete/<int:category_id>/', views.delete_event_category, name='delete_event_category'),
    path('events_category/edit/<int:pk>/', CategoryUpdateView.as_view(), name='edit_event_category'),
    #Auth Links
    path('login/', views.user_login, name='user_login'),
    path('register/', views.user_register, name='user_register'),
    path('logout/', views.user_logout, name='user_logout'),

    path('users_list/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('users_list/', views.user_list, name='user_list'),
    path('reserve/<int:event_id>/', views.reserve_event, name="reserve_event"),

]