from django.urls import path
from  . import views 
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('homepage',views.homepage,name='homepage'),
    path('mpesapayment', views.mpesapayment, name='mpesapayment'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('productions',views.productions,name='productions'),
    path('event',views.event,name='event'),
    path('contacts',views.contacts,name='contacts'),
     path("login/", views.login, name="login"),
    path('home',views.home,name='home'),
    path('productions',views.productions),
    path('gallery',views.gallery,name='gallery'),
    path('create-member',views.createmember,name='createmember'),
    path('read-ALLmember', views.readALLmember, name='readALLmember'),
    path('updatemember/<str:pk>/', views.update_member, name='updatemember'),
    path('deletemember/<str:pk>/', views.delete_member, name='deletemember'),
    path('create-event',views.createevent,name='createevent'),
    path('read-ALLevent', views.read_event, name='readALLevent'),
    path('update-event/<str:pk>/', views.update_event, name='updateevent'),
    
    
    path('delete-event/<str:pk>/', views.delete_event, name='deleteevent'),
  
    path('login', auth_views.LoginView.as_view(template_name='dramaapp/login.html'), name='login'),
    path('signup', views.signup_view, name='signup'),
    path('logout', auth_views.LogoutView.as_view(next_page='login'), name='logout'),


  

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)            