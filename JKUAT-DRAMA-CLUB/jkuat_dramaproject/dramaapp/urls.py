from django.urls import path
from  . import views 
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('homepage',views.homepage,name='homepage'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('productions',views.productions,name='productions'),
    path('events',views.events,name='events'),
    path('contacts',views.contacts,name='contacts'),
     path("login/", views.login, name="login"),
    path('home',views.home,name='home'),
    path('productions',views.productions),
    path('gallery',views.gallery),
    path('create-member',views.createmember,name='createmember'),
    path('read-ALLmember',views.read_ALL_member,name='readmember'),
    path('update-member/<str:pk>/', views.update_member, name='updatemember'),
    path('delete-member/<str:pk>/', views.delete_member, name='deletemember'),
    path('create-event',views.createevent,name='createevent'),
    path('create-gallery',views.creategallery,name='creategallery'),
   
    path('read-ALLEvent', views.read_event, name='readevent'),    
    path('read-ALLgallery' ,views.read_gallery, name='readgallery'),
   
    path('update-event/<str:pk>/', views.update_event, name='updateevent'),
    path('update-gallery/<str:pk>/', views.update_gallery, name='updategallery'),
    
    path('delete-event/<str:pk>/', views.delete_event, name='deleteevent'),
    path('delete-gallery/<str:pk>/', views.delete_gallery, name='deletegallery'),
    path('login', auth_views.LoginView.as_view(template_name='dramaapp/login.html'), name='login'),
    path('signup', views.signup_view, name='signup'),
    path('logout', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

  

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)            