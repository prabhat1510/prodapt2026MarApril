# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import CustomerService
from .serializers import CustomerSerializer

class CustomerView(APIView):

    def get(self, request):
        customers = CustomerService.get_all_customers()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            customer = CustomerService.create_customer(request.data)
            print("===customer===",customer)
            serializer = CustomerSerializer(customer)
            print("===serializer.data===",serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"error": str(e)}, status=400)


class CustomerDetailView(APIView):

    def get(self, request, pk):
        try:
            customer = CustomerService.get_customer(pk)
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        except ValueError as e:
            return Response({"error": str(e)}, status=404)

    def put(self, request, pk):
        try:
            customer = CustomerService.update_customer(pk, request.data)
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        except ValueError as e:
            return Response({"error": str(e)}, status=400)

    def delete(self, request, pk):
        try:
            CustomerService.delete_customer(pk)
            return Response({"message": "Deleted successfully"})
        except ValueError as e:
            return Response({"error": str(e)}, status=404)