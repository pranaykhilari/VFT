from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from db_integration import views as dbview

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns+=[
    url(r'^download/', dbview.access_db, name="access-db")
]



