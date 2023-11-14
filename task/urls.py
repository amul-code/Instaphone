from django.urls import path
from . import views

urlpatterns = [
    path('user/register/', views.user_registration, name='user-registration'),
    path('user/login/', views.user_login, name='user-login'),
    path('contacts/', views.manage_contacts, name='manage-contacts'),
    path('mark/spam/', views.mark_spam, name='mark-spam'),
    path('search/', views.search, name='search'),
    # Other endpoints and views from your 'views.py'
]
