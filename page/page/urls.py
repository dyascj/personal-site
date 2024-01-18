from django.urls import path
from myapp.views import spline_view

urlpatterns = [
    path('home/', spline_view, name='home'),
    # ... other paths ...
]