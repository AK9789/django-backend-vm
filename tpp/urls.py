from django.urls import path, include
# from .views import  login, GetUser, Register
from . import views

urlpatterns = [
    # path('hello-view/', HelloApiViews.as_view()),
    # path('login/', login.as_view()),
    # path('user/', GetUser.as_view()),
    # path('register/', Register.as_view())
    path('user-list/',views.showAll, name='user-list'),
    path('user-specific/<int:pk>/',views.userSpecific, name='user-specific'),
    path('user-create/',views.createUser, name='user-create')
]