from django.urls import path
# from attendease import views
from .views import index, practice, lecdashcl, lechistory, schedlec

urlpatterns = [
    path("", index, name="index"),
    path("practice/", practice, name="practice"),
    path("lecdashcl/", lecdashcl, name="lecdashcl"),
    path("lechistory/", lechistory, name="lechistory"),
    path("schedlec/", schedlec, name="schedlec"),
    
]