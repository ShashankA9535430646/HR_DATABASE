from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.log_in,name='login'),
    path('logout',views.log_out,name='logout'),
    path('home',views.home,name='home'),
    path('form',views.display_form,name='form'),
    path('details',views.display_details,name="detail"),
    path('details/<id>',views.display_details_individuals,name="details"),
    path('details',views.display_details_individuals,name="details"),
    path('details/delete/<id>',views.delete_details,name='delete'),
    path('details/update/<id>',views.update_details,name='update'),
]