from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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
