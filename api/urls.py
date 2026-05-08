from django.urls import path
from . import views

urlpatterns = [
    # FUNCTION BASED VIEWS
    path('singleobj/<int:pk>/', views.singleobj),
    path('multipleobj/', views.multipleobj),

    # CLASS BASED VIEWS
    path('person/<int:pk>/', views.SingleObjApiView.as_view()),
    path('persons/', views.MultipleObjApiView.as_view()),
]