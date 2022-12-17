from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http.request import HttpRequest
from .serializers import MembersSerializer, MembershipsSerializer, ReactionsSerializer, ConnectionsSerializer, MessagesSerializer
from .models import Memberships, Members, Reactions, Connections, Messages, ReactionType
from datetime import datetime
from django.forms.models import model_to_dict
import json
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.views import APIView
from django.db.models import Q
from authentication.handlers import JWTHandler
# like : 1
# nomatch : 2
# super_like : 3
# block : 4

class BlockAPI(APIView):
    def post(self, request: HttpRequest):
        """params
        for AccountReaction
        
        receiver_id
        reactor_id
        icon_name
        """
        print(request)
        reactor_id = JWTHandler.get_current_user(request.COOKIES)
        receiver_id = request.GET.get("receiver_id", "")
        type = ReactionType.BLOCK
        issued_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        # print(account_reaction_data)
        # account_reaction_data["created_at"] = datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f")
        # account_reaction_data["deleted_at"] = None
        # print(account_reaction_data)
        
        print("Hello")
        print({"reactor_id": reactor_id, "receiver_id": receiver_id, "issued_date": issued_date,"type": type})
        reaction_serializer=ReactionsSerializer(data={"reactor_id": reactor_id, "receiver_id": receiver_id, "issued_date": issued_date,"type": type})
        
        if reaction_serializer.is_valid():
            print("Saved reactions")
            response1 = reaction_serializer.save()
            
            response = {"reactions": reaction_serializer.data}
            
            return JsonResponse(response, content_type="application/json")   
        
        return JsonResponse("Invalid parameters for usersuperlike", safe=False) 

    
    def delete(self, request: HttpRequest, _reactor_id = 0, _receiver_id = 0):
        reactor_id = JWTHandler.get_current_user(request.COOKIES)        
        
        reactions = Reactions.objects.get(reactor_id=reactor_id, receiver_id=_receiver_id)
        
        reactions.delete()
        
        response = {"reactions": model_to_dict(reactions)}
        
        return JsonResponse(response)


class ChatAPI(APIView):
    def get(self, request: HttpRequest):
        """params
        user_id_1
        user_id_2
        page
        """

        message_per_page = 20
        user_id_1 = JWTHandler.get_current_user(request.COOKIES)
        user_id_2 = request.GET.get("user_id_2", "")
        page = int(request.GET.get("page", ""))
        print(user_id_1, user_id_2, page)
        
        messages_1 = list(Messages.objects.filter(sender_id = user_id_1, recipient_id = user_id_2).values())
        messages_2 = list(Messages.objects.filter(sender_id = user_id_2, recipient_id = user_id_1).values())
        
        
        messages_1.extend(messages_2)
        def sort_messages(x):
            return x["send_date"]
        
        
        messages = sorted(messages_1, key=sort_messages, reverse=True)
        
        
        return JsonResponse(messages[page * message_per_page:page* message_per_page + message_per_page], content_type="application/json",safe=False)
    
    def post(self, request: HttpRequest):
        """params
        sender_id
        recipient_id
        message
        """
        
        sender_id = JWTHandler.get_current_user(request.COOKIES) 
        recipient_id = request.GET.get("recipient_id", "")
        message = request.GET.get("message", "")
        send_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            sender_recipient = Connections.objects.get(user_id_1=sender_id, user_id_2=recipient_id)
        except Exception as e:
            
            return JsonResponse(f'{sender_id} and {recipient_id} can\'t chat with the other.' + str(e), safe=False)
        
        try:
            recipient_sender = Connections.objects.get(user_id_1=recipient_id, user_id_2=sender_id)
        except Exception as e:
            return JsonResponse(f'{sender_id} and {recipient_id} can\'t chat with the other.' + str(e), safe=False)
        
        data = {
            "message": message,
            "send_date": send_date,
            "status": '1',
            "recipient_id": recipient_id,
            "sender_id": sender_id
        }
        print(data)
        message_serializer = MessagesSerializer(data =data)
        
        if message_serializer.is_valid():
            message_serializer.save()
            
            
            return JsonResponse(message_serializer.data, content_type="application/json")   
            
        
        return JsonResponse("Invalid parameters for chat", content_type="application/json",safe=False)
    def delete(self, request: HttpRequest, message_id):
        sender_id = JWTHandler.get_current_user(request.COOKIES) 
                
        messages = Messages.objects.get(message_id=message_id, sender_id = sender_id)

        messages.delete()
        
        return JsonResponse(model_to_dict(messages))
    
    

class SuperLikeAPI(APIView):
    def post(self, request: HttpRequest):
        """params
        for AccountReaction
        
        receiver_id
        reactor_id
        icon_name
        """
     
        print(request)
        reactor_id = JWTHandler.get_current_user(request.COOKIES) 
        receiver_id = request.GET.get("receiver_id", "")
        type = ReactionType.SUPER_LIKE
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
        
        return JsonResponse("Invalid parameters for usersuperlike", safe=False) 
        pass
    
    
    def delete(self, request: HttpRequest, _reactor_id = 0, _receiver_id = 0):
        rector_id = JWTHandler.get_current_user(request.COOKIES) 
        reactions = Reactions.objects.get(reactor_id = rector_id, receiver_id=_receiver_id)
        connections = Connections.objects.get(user_id_1 = rector_id, user_id_2 = _receiver_id)
        
        
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
        reactor_id = JWTHandler.get_current_user(request.COOKIES) 
        receiver_id = request.GET.get("receiver_id", "")
        type = ReactionType.NO_MATCH
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
        
        return JsonResponse("Invalid parameters for nomatch", safe=False) 
    
    
    def delete(self, request: HttpRequest, _reactor_id = 0, _receiver_id = 0):
        reactor_id = JWTHandler.get_current_user(request.COOKIES) 
        
        reactions = Reactions.objects.get(reactor_id=reactor_id, receiver_id=_receiver_id)
        
        reactions.delete()
        
        return JsonResponse(model_to_dict(reactions))


class LikedMembersAPI(APIView):
    def get(self, request: HttpRequest, _receiver_id=0): 
        receiver_id = JWTHandler.get_current_user(request.COOKIES) 
        reactions = Reactions.objects.filter(receiver_id=receiver_id, type=ReactionType.LIKE).values()
        print(reactions)
        
        return JsonResponse([entry for entry in reactions], safe=False)
    

class MembersLikedAPI(APIView):
    def get(self, request: HttpRequest, _reactor_id=0):
        reactor_id = JWTHandler.get_current_user(request.COOKIES) 
        reactions = Reactions.objects.filter(reactor_id= reactor_id, type=ReactionType.LIKE).values()
        print(reactions)

        return JsonResponse([entry for entry in reactions], safe=False)
    
    
    def post(self, request: HttpRequest):
        """params
        for AccountReaction
        
        receiver_id
        reactor_id
        type
        """
        
        print(request)
        reactor_id = JWTHandler.get_current_user(request.COOKIES) 
        receiver_id = request.GET.get("receiver_id", "")
        type = ReactionType.LIKE
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
        reactor_id = JWTHandler.get_current_user(request.COOKIES) 
            
        
        reactions = Reactions.objects.get(reactor_id=reactor_id, receiver_id=_receiver_id)
        
        reactions.delete()
        
        return JsonResponse(model_to_dict(reactions))
    
    
    
    