from django.urls import path
from . import views

urlpatterns = [
    path('singleobj/<int:id>/', views.singleobj),
    path('multipleobj/', views.multipleobj),
    path('person/<int:id>/', views.SingleObjApiView.as_view()),
    path('persons/', views.MultipleObjApiView.as_view())
]
