from django.urls import path
from . import views

urlpatterns = [
    path('singleobj/<int:pk>/', views.singleobj),
    path('multipleobj/', views.multipleobj),
    path('person/<int:pk>/', views.SingleObjApiView.as_view()),
    path('persons/', views.MultipleObjApiView.as_view())
]
