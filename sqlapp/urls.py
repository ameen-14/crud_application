from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.insertpageview, name='insertpage'),
    path("insert/", views.InsertData, name="insert"),
    path("show/", views.FetchData, name='show_data')

]