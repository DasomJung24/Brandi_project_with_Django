from django.urls import path, include

urlpatterns = [
    path('seller', include('seller.urls')),
]
