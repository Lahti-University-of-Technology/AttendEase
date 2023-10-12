from django.urls import path
# from attendease import views
from .views import index

urlpatterns = [
    path("", index, name="index"),
]