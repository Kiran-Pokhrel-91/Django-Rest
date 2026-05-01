from django.urls import path
from . import views

urlpatterns = [
    path('singleobj/<int:id>/', views.singleobj),
    path('multipleobj/', views.multipleobj)
]
