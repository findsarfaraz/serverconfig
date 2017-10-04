
from django.conf.urls import url


app_name ="main_app"

from views import index 

urlpatterns= [
		url(r'^$',index,name ='index'),
		]
