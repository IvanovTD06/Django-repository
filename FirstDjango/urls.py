from django.urls import path
from MainApp.views import main_page

urlpatterns = [
    path("main", main_page)
]