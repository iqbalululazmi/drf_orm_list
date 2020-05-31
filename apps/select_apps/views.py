from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import HeroSerializer
from .models import Hero


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

# List hero
@api_view(['GET'])
def list_heroes(request):
    if request.method == 'GET':
        posts = Hero.objects.all().order_by('name')
        print(posts.query)
        serializer = HeroSerializer(posts, many=True)
        return Response(serializer.data)

# Get heroes by Id
@api_view(['GET'])
def get_heroes_id(request, pk):
    try:
        post = Hero.objects.get(pk=pk)
    except Hero.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = HeroSerializer(post)
        return Response(serializer.data)