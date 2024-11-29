from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drfApi.models import Person
from drfApi.serializers import PersonSerializer
from rest_framework import viewsets


# Create your views here.

@api_view(['GET','POST','PUT','DELETE','PATCH'])
def person(request):
    if request.method == 'GET':
        objs = Person.objects.filter(color__isnull=False)
        serializer = PersonSerializer(objs, many=True)
        return Response(serializer.data)
    
        
    elif request.method == 'POST':
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
        
    elif request.method == 'PUT':
        person = get_object_or_404(Person, id=request.data['id'])  
        data = request.data
        serializer = PersonSerializer(person, data=data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'PATCH':
        person = get_object_or_404(Person, id=request.data['id'])  
        data = request.data
        serializer = PersonSerializer(person, data=data,partial = True)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        person = get_object_or_404(Person,id=request.data['id'])
        if person:
            person.delete()
            return Response("Successfullly deleted",status=204)
        return Response("Person not found",status=404)
    


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()  
    serializer_class = PersonSerializer  