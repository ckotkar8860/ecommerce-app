from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the ecommerce site!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('', home),  # Add this line for the root path
]
