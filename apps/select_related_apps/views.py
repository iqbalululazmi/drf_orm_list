from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Vehicle, Customer
from .serializers import VehicleSerializer, CustomerSerializer

# Create your views here.
@api_view(['GET'])
def list_vehicles(request):
    if request.method == 'GET':
        # posts = Vehicle.objects.all()
        posts = Vehicle.objects.prefetch_related('customer')

        print(posts.query)
        serializer = VehicleSerializer(posts, many=True)
        return Response(serializer.data)

# Get vehicle & customer by Id
@api_view(['GET'])
def get_vehicle_id(request, pk):
    try:
        post = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CustomerSerializer(post)
        vehicle = Vehicle.objects.get(customer=post)
        serializer_vehicle = VehicleSerializer(vehicle)
        print(serializer_vehicle.data)
        return Response({
            'customer': serializer.data,
            'vehicle': serializer_vehicle.data
        })
