from rest_framework.views import APIView
from .serializers import actorSerializer
from .models import Actor
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
#this returns all of the actors
class ActorsList(APIView):
    def get(self, request):
        actors = Actor.objects.all()
        serializer = actorSerializer(actors, many=True)
        return Response(serializer.data)
    def post(self, request): #adds a new item
        serializer = actorSerializer(data=request.data)
        if(serializer.is_valid()): #if there are no errors with the response
            serializer.save() #save it to the serializer
            return Response(serializer.data, status=status.HTTP_201_CREATED) #good functional post request
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #

#do the detail view here for a specific actor?
class ActorByID(APIView):
    def get_object(self, pk): #returns a single actor instance; new get() defined below; pk is primary key
        return Actor.objects.get(pk=pk)
    def get(self, request, pk): #we make a different definition for get for this use case
        actor = self.get_object(pk)
        serialize_obj = actorSerializer(actor)
        return Response(serialize_obj.data)
    def put(self, request, pk): #changes an item
        actor = self.get_object(pk)
        serializer = actorSerializer(actor, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        actor = self.get_object(pk)
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

