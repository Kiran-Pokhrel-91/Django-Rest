from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Person
from .serializers import PersonSerializer


@api_view(['GET', 'PUT', 'PATCH'])
def singleobj(request, id):
    person = get_object_or_404(Person, id=id)

    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    serializer = PersonSerializer(
        person,
        data=request.data,
        partial=(request.method == 'PATCH')
    )

    serializer.is_valid(raise_exception=True)
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

    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(
        serializer.data,
        status=status.HTTP_201_CREATED
    )

class MultipleObjApiView(APIView):
    def get(self,request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = PersonSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SingleObjApiView(APIView):

    def get(self, request, id):
        person = get_object_or_404(Person, id=id)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    def put(self, request, id):
        person = get_object_or_404(Person, id=id)
        serializer = PersonSerializer(person, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, id):
        person = get_object_or_404(Person, id=id)
        serializer = PersonSerializer(person, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        person = get_object_or_404(Person, id=id)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
