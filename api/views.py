from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin,ListModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin

from .models import Person
from .serializers import PersonSerializer,PersonModelSerializer


@api_view(['GET', 'PUT', 'PATCH'])
def singleobj(request, pk):
    person = get_object_or_404(Person, pk=pk)

    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    serializer = PersonSerializer(
        person,
        data=request.data,
        partial=(request.method == 'PATCH')
    )

    serializer.is_valpk(raise_exception=True)
    serializer.save()

    return Response(serializer.data)


@api_view(['GET', 'POST'])
def multipleobj(request):

    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    serializer = PersonSerializer(
        data=request.data,
        many=True
    )

    serializer.is_valpk(raise_exception=True)
    serializer.save()

    return Response(
        serializer.data,
        status=status.HTTP_201_CREATED
    )

class MultipleObjApiView(CreateModelMixin,ListModelMixin,GenericAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args, **kwargs)
    
    def post(self,request):
        return self.create(request)

class SingleObjApiView(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args, **kwargs)

    def put(self, request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request,*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args, **kwargs)
    