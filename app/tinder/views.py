from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http.request import HttpRequest
from .serializers import MembersSerializer, MembershipsSerializer, ReactionsSerializer, ConnectionsSerializer
from .models import Memberships, Members, Reactions, Connections
from datetime import datetime
from django.forms.models import model_to_dict
import json
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.views import APIView

# like : 1
# nomatch : 2

class SuperLikeAPI(APIView):
    def post(self, request: HttpRequest):
        """params
        for AccountReaction
        
        receiver_id
        reactor_id
        icon_name
        """
        print(request)
        reactor_id = request.GET.get("reactor_id", "")
        receiver_id = request.GET.get("receiver_id", "")
        type = request.GET.get("type", "")
        issued_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        # print(account_reaction_data)
        # account_reaction_data["created_at"] = datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f")
        # account_reaction_data["deleted_at"] = None
        # print(account_reaction_data)
        
        print("Hello")
        print({"reactor_id": reactor_id, "receiver_id": receiver_id, "issued_date": issued_date,"type": type})
        reaction_serializer=ReactionsSerializer(data={"reactor_id": reactor_id, "receiver_id": receiver_id, "issued_date": issued_date,"type": type})
        
        connection_serializer = ConnectionsSerializer(data={"user_id_1": reactor_id, "user_id_2": receiver_id, "created_date": issued_date})
        
        
        if reaction_serializer.is_valid():
            print("Saved reactions")
            response1 = reaction_serializer.save()
            
            if connection_serializer.is_valid():
                print("Saved connections")
                response2 = connection_serializer.save()
            
            response = {"reactions": reaction_serializer.data, "connections": connection_serializer.data}
            
            return JsonResponse(response, content_type="application/json")   
        
        return JsonResponse("Invalid parameters for userlike", safe=False) 
        pass
    
    
    def delete(self, request: HttpRequest, _reactor_id = 0, _receiver_id = 0):
        reactions = Reactions.objects.get(reactor_id=_reactor_id, receiver_id=_receiver_id)
        connections = Connections.objects.get(user_id_1 = _reactor_id, user_id_2 = _receiver_id)
        
        
        reactions.delete()
        connections.delete()
        
        response = {"reactions": model_to_dict(reactions), "connections": model_to_dict(connections)}
        
        return JsonResponse(response)
    
    
    


class NoMatchAPI(APIView):
    def post(self, request: HttpRequest):
        """params
        for AccountReaction
        
        receiver_id
        reactor_id
        icon_name
        """
        print(request)
        reactor_id = request.GET.get("reactor_id", "")
        receiver_id = request.GET.get("receiver_id", "")
        type = request.GET.get("type", "")
        issued_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        # print(account_reaction_data)
        # account_reaction_data["created_at"] = datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f")
        # account_reaction_data["deleted_at"] = None
        # print(account_reaction_data)
        
        print("Hello")
        print({"reactor_id": reactor_id, "receiver_id": receiver_id, "issued_date": issued_date,"type": type})
        reaction_serializer=ReactionsSerializer(data={"reactor_id": reactor_id, "receiver_id": receiver_id, "issued_date": issued_date,"type": type})
        
        
        if reaction_serializer.is_valid():
            response = reaction_serializer.save()
            
            
            return JsonResponse(reaction_serializer.data, content_type="application/json")   
        
        return JsonResponse("Invalid parameters for userlike", safe=False) 
    
    
    def delete(self, request: HttpRequest, _reactor_id = 0, _receiver_id = 0):
        reactions = Reactions.objects.get(reactor_id=_reactor_id, receiver_id=_receiver_id)
        
        reactions.delete()
        
        return JsonResponse(model_to_dict(reactions))


class LikedMembersAPI(APIView):
    def get(self, request: HttpRequest, _receiver_id=0):
        
        reactions = Reactions.objects.filter(receiver_id= _receiver_id, type=1).values()
        print(reactions)
        
        return JsonResponse([entry for entry in reactions], safe=False)
    

class MembersLikedAPI(APIView):
    def get(self, request: HttpRequest, _reactor_id=0):
        reactions = Reactions.objects.filter(reactor_id= _reactor_id, type=1).values()
        print(reactions)
        return JsonResponse([entry for entry in reactions], safe=False)
    
    
    def post(self, request: HttpRequest):
        """params
        for AccountReaction
        
        receiver_id
        reactor_id
        icon_name
        """
        print(request)
        reactor_id = request.GET.get("reactor_id", "")
        receiver_id = request.GET.get("receiver_id", "")
        type = request.GET.get("type", "")
        issued_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        # print(account_reaction_data)
        # account_reaction_data["created_at"] = datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f")
        # account_reaction_data["deleted_at"] = None
        # print(account_reaction_data)
        
        print("Hello")
        print({"reactor_id": reactor_id, "receiver_id": receiver_id, "issued_date": issued_date,"type": type})
        reaction_serializer=ReactionsSerializer(data={"reactor_id": reactor_id, "receiver_id": receiver_id, "issued_date": issued_date,"type": type})
        
        
        
        
        if reaction_serializer.is_valid():
            response = reaction_serializer.save()
            
            
            return JsonResponse(reaction_serializer.data, content_type="application/json")   
        
        return JsonResponse("Invalid parameters for userlike", safe=False) 
    
    def delete(self, request: HttpRequest, _reactor_id=0, _receiver_id = 0):
        
        
        reactions = Reactions.objects.get(reactor_id=_reactor_id, receiver_id=_receiver_id)
        
        reactions.delete()
        
        return JsonResponse(model_to_dict(reactions))