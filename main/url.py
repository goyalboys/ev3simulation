from django.urls import path
from . import views

urlpatterns=[
path('',views.login,name='login'),
path('signup/',views.signup,name='signup'),
    path('index/',views.home,name='home'),
    path('logout/',views.signout)
    #path('likepost/',views.ho,name='likepost'),
#path('validate_ajax/', views.validate_ajax, name='validate_ajax'),
#path('upload/', views.image_upload_view),
]
