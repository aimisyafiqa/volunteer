from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,name="index"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("event", views.event, name='event'),
    path("search_event", views.search_event, name="search_event" ),
    path('join_event/<str:eventid>/', views.join_event, name='join_event'),  # Accept alphanumeric event IDs
    path('update_student/<str:studentid>/', views.update_student, name='update_student'),
    path('update_student/save_update_student/<str:studentid>/', views.save_update_student, name='save_update_student'),
    path('myprofile', views.myprofile, name='myprofile'),
    path('delete_event/<str:volunteerid>/', views.delete_event, name='delete_event'),
    path('homepage/', views.homepage, name='homepage'),
    path("logout", views.logout,name="logout"),
]