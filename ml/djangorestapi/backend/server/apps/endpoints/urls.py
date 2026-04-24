from django.urls import path
from .views import CreateCustomer, CreateProduct, CustomerViewSet, ProductViewSet

urlpatterns = [
    path('createcustomer/', CreateCustomer.as_view()),
    path('createproduct/', CreateProduct.as_view()),
    path('getcustomer/', CustomerViewSet.as_view({'get': 'list'})),
    path('getproduct/', ProductViewSet.as_view({'get': 'list'})),
]