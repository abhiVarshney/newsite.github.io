from django.urls import path
from app.views import home,jobDetails,show

urlpatterns = [
    path('', home,name='home'),
    path('job/<id>', jobDetails,name='jobDetail'),
    path('show/', show,name='show'),
]
