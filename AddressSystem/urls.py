from django.urls import path 
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('contacts/mycontacts/', views.viewAllContacts, name = 'All Contact'),
    path('contacts/viewContactDetails/<int:pk>/', views.viewContact, name = 'Contact details'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('sign up/', views.registration, name="Sign up"),
    path('log in/', views.userLogin, name="log in"),
    path('addContacts/', views.AddContact, name = 'AddContacts'),
    path('contact/<int:pk>/delete', views.ContactDelete.as_view(template_name = 'Contact_Delete.html'), name = 'Contact-Delete'),
    path('contact/<int:pk>/update', views.contactUpdate, name = 'Contact-Update'),






]