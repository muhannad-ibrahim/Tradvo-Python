from django.urls import path
from .views import register, home, user_login, app_list, app_add, app_update, app_delete, custom_logout_view

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', custom_logout_view , name='logout'), 
    path('apps/', app_list, name='app_list'),
    path('apps/add/', app_add, name='app_add'),
    path('apps/update/<int:app_id>/', app_update, name='app_update'),
    path('apps/delete/<int:app_id>/', app_delete, name='app_delete'),
]
