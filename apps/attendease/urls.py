from django.urls import path
# from attendease import views
from .views import index, dashboard

urlpatterns = [
    path("", index, name="index"),
    path("dashboard/", dashboard, name="dashboard"),
]