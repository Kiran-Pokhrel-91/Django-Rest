from django.shortcuts import render, get_object_or_404
from .models import Person
from .serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status


# Create your views here.
def singleobj(request, id):
    data = get_object_or_404(Person, id=id)

    if request.method == "PUT":
        stream = io.BytesIO(request.body)
        parsed_data = JSONParser().parse(stream)

        serializer = PersonSerializer(instance=data, data=parsed_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                {"updated": "successfully", "data": serializer.data},
                status=status.HTTP_200_OK
            )

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = PersonSerializer(data)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def multipleobj(request):
    if request.method == "POST":
        stream = io.BytesIO(request.body)
        parsed_data = JSONParser().parse(stream)

        serializer = PersonSerializer(data=parsed_data, many=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                {"created": "successful", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    data = Person.objects.all()
    serializer = PersonSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)
