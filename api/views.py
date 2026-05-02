from django.shortcuts import get_object_or_404
from .models import Person
from .serializers import PersonSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'PUT', 'PATCH'])
def singleobj(request, id):
    person = get_object_or_404(Person, id=id)

    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        serializer = PersonSerializer(
            instance = person,
            data=request.data,
            partial=(request.method == 'PATCH')
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "updated": "successfully",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def multipleobj(request):

    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PersonSerializer(
            data=request.data,
            many=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "created": "successful",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
