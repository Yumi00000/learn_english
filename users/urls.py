from django.urls import path
from users import views

urlpatterns = [
    path('', views.user_page, name='user_page'),
    path('delete/', views.user_delete, name='user_delete'),
    path('login/', views.login_handler, name='login'),
    path('register/', views.register, name='login_handler'),
    path('logout/', views.logout_handler, name='logout_handler')
]
