# views.py

from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Person
from .serializers import PersonSerializer, PersonModelSerializer


# FUNCTION BASED VIEWS
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def singleobj(request, pk):

    person = get_object_or_404(Person, pk=pk)

    # GET
    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    # DELETE
    if request.method == 'DELETE':
        person.delete()
        return Response(
            {"message": "Person deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )

    # PUT / PATCH
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

    # GET ALL
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    # POST
    serializer = PersonSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(
        serializer.data,
        status=status.HTTP_201_CREATED
    )


# CLASS BASED VIEWS
class MultipleObjApiView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer
    ## uncomment for authentication
    # authentication_classes = [TokenAuthentication] 
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        print(request.user)
        return super().get(request, *args, **kwargs)


class SingleObjApiView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer