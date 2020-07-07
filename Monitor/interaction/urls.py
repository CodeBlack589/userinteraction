from django.urls import path
from interaction import views
app_name="interaction"
urlpatterns=[
  
    path('',views.home,name="home"),
  
]
