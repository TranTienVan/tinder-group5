from django.shortcuts import render
from django.contrib.auth import logout 
from rest_framework.request import Request
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .models import  Members, MembersInfo, MembersSettings
from .serializers import  MembersInfoSerializer, MembersSettingsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.urls import reverse
from django.db import IntegrityError
from authentication.handlers import JWTHandler
from authentication.models import MyUser
import stripe
import json
import os
from django.http import JsonResponse
from django.shortcuts import redirect
from dotenv import load_dotenv, find_dotenv
import datetime
from django.utils import timezone
now = timezone.now()


def hello_world(request):
    return HttpResponse("<h1>Hello world</h1>")

class MembersInforAPI(APIView):
    def get(self, request):
        try: 
            id =  JWTHandler.get_current_user(request.COOKIES) 
            user = MyUser.objects.filter(id = id).first()
            user_info, created = MembersInfo.objects.get_or_create(user = user.members)
            
            serializer_context = {
                 'request': request,
            }
            serializer = MembersInfoSerializer(user_info, serializer_context)
            if serializer.is_valid():
                return Response(serializer.data)
            else: 
                print(serializer.errors)
                return HttpResponse(serializer.errors)
        except IntegrityError:
            return HttpResponseNotFound(f"User With ID:{id} Does Not Exist!")

    def put(self, request):
        try: 
            
            
            id =  JWTHandler.get_current_user(request.COOKIES) 
            user = Members.objects.get(user_id=id)
            if(request.POST.get('user_name') is not None):
                user.user_name = request.POST.get('user_name') 
            user.save()
            
            user_info, created = MembersInfo.objects.get_or_create(user_id = id)
            user_info.address = request.POST.get('address')
            user_info.street = request.POST.get('street')
            user_info.district = request.POST.get('district')
            user_info.city = request.POST.get('city')
            user_info.country = request.POST.get('country')
            user_info.language = request.POST.get('language')
            user_info.hobby = request.POST.get('hobby')
            user_info.company =request.POST.get('company')
            user_info.school = request.POST.get('school')
            user_info.save()

            serializer_context = {
            'request': request,
            }
            
            serializer = MembersInfoSerializer(user_info, serializer_context)
            if serializer.is_valid():
                return Response(serializer.data)
            else: 
                print(serializer.errors)
                return HttpResponse(serializer.errors)
        except Members.DoesNotExist:
            return HttpResponseNotFound(f"User With ID:{id} Does Not Exist!")
        except IntegrityError:
            return HttpResponseNotFound(f"User With ID:{id}Does Not Exist!")
       

    def delete(self,request):
        try:  
            id =  JWTHandler.get_current_user(request.COOKIES) 
            user= Members.objects.get(user_id = id)
            
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT) 

        except Members.DoesNotExist:
            return HttpResponseNotFound(f"User With ID:{id} Does Not Exist!")

class MembersSettingsAPI(APIView):
    def get(self, request):
        try: 
            id =  JWTHandler.get_current_user(request.COOKIES) 
            user = MyUser.objects.filter(id = id).first()
            user_setting, created = MembersSettings.objects.get_or_create(user = user.members)

            serializer_context = {
                'request': request,
            }
            serializer = MembersSettingsSerializer(user_setting, serializer_context)
            if serializer.is_valid():
                return Response(serializer.data)
            else: 
                print(serializer.errors)
                return HttpResponse(serializer.errors)
        except IntegrityError:
            return HttpResponseNotFound(f"User With ID:{id} Does Not Exist!")

    def put(self, request):
        try: 
            id =  JWTHandler.get_current_user(request.COOKIES)
            user_setting, created = MembersSettings.objects.get_or_create(user_id = id)
            user_setting.search_locations = request.POST.get('search_locations')
            user_setting.max_range = request.POST.get('max_range')
            user_setting.min_match_age = request.POST.get('min_match_age')
            user_setting.max_match_age = request.POST.get('max_match_age')
            user_setting.visibility = request.POST.get('visibility')
            
            serializer_context = {
           'request': request,
            }
            serializer = MembersSettingsSerializer(user_setting, serializer_context)
            if serializer.is_valid():
                user_setting.save()
                return Response(serializer.data)
            else: 
                print(serializer.errors)
                return HttpResponse(serializer.errors)
        except IntegrityError:
            return HttpResponseNotFound(f"User With ID:{id} Does Not Exist!")


# Stripe keys

STRIPE_PUBLISHABLE_KEY = os.environ.get("STRIPE_PUBLISHABLE_KEY")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
STRIPE_WEBHOOK_SECRET = os.environ.get("STRIPE_WEBHOOK_SECRET")
DOMAIN = os.environ.get("DOMAIN")
BASIC_PRICE_ID = os.environ.get("BASIC_PRICE_ID")
PRO_PRICE_ID = os.environ.get("PRO_PRICE_ID")
STATIC_DIR = os.environ.get("STATIC_DIR")
BASIC_PRICE = 20
PRO_PRICE = 90
BASIC_DURATION = 30
PRO_DURATION = 180

# Setup Stripe python client library
load_dotenv(find_dotenv())
# For sample support and debugging, not required for production:
stripe.set_app_info(
    'stripe-samples/checkout-single-subscription',
    version='0.0.1',
    url='https://github.com/stripe-samples/checkout-single-subscription')

stripe.api_version = '2020-08-27'
stripe.api_key = STRIPE_SECRET_KEY

static_dir = str(os.path.abspath(os.path.join(
    __file__, "..", STATIC_DIR)))

#? PAYMENT AND UPGRADE TO PREMIUM API

# @app.route('/upgrade', methods=['GET'])
def get_example(request):
    # id =  JWTHandler.get_current_user(request.COOKIES)
    id = 1 ##// TEST
    try:
        member = Members.objects.get(user_id = id)
        if member.membership_date is None or timezone.now().date() > member.membership_date:
             return render(request, 'index.html')
        else:
            return HttpResponse("<h1>You are already a premium member! Thanks you for supporting</h1>")
    except Members.DoesNotExist:
        return HttpResponse(f"User with ID {id} does not exist")


# @app.route('/config', methods=['GET'])
def get_publishable_key(request):
    print("hihi")
    return JsonResponse({
        'publishableKey':STRIPE_PUBLISHABLE_KEY,
        'basicPrice': BASIC_PRICE_ID,
        'proPrice': PRO_PRICE_ID
    })


# Fetch the Checkout Session to display the JSON result on the success page
# @app.route('/checkout-session', methods=['GET'])
def get_checkout_session(request):
    id = request.GET.get('sessionId', '')
    checkout_session = stripe.checkout.Session.retrieve(id)
    return JsonResponse(checkout_session)


# @app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session(request):
    price = request.POST.get('priceId')
    domain_url = DOMAIN + '/api'

    try:
        # Create new Checkout Session for the order
        # Other optional params include:
        # [billing_address_collection] - to display billing address details on the page
        # [customer] - if you have an existing Stripe Customer ID
        # [customer_email] - lets you prefill the email input in the form
        # [automatic_tax] - to automatically calculate sales tax, VAT and GST in the checkout page
        # For full details see https://stripe.com/docs/api/checkout/sessions/create

        # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + '/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=domain_url + '/canceled',
            mode='subscription',
            # automatic_tax={'enabled': True},
            line_items=[{
                'price': price,
                'quantity': 1
            }],
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        # return JsonResponse({'error': {'message': str(e)}}), 400
        print(str(e))
        return HttpResponse(status=400, content="Invalid signature")
def get_success(request):
    return render(request,'success.html')

def get_cancel(request):
    return HttpResponseRedirect(reverse('upgrade'))

# @app.route('/customer-portal', methods=['POST'])
def customer_portal(request):
    # For demonstration purposes, we're using the Checkout session to retrieve the customer ID.
    # Typically this is stored alongside the authenticated user in your database.
    checkout_session_id = request.POST.get('sessionId')
    checkout_session = stripe.checkout.Session.retrieve(checkout_session_id)

    # This is the URL to which the customer will be redirected after they are
    # done managing their billing with the portal.
    return_url =DOMAIN + '/api'

    session = stripe.billing_portal.Session.create(
        customer=checkout_session.customer,
        return_url=return_url,
    )
    return redirect(session.url, code=303)


# @app.route('/webhook', methods=['POST'])
def webhook_received(request):
    # You can use webhooks to receive information about asynchronous payment events.
    # For more about our webhook events check out https://stripe.com/docs/webhooks.
    webhook_secret = STRIPE_WEBHOOK_SECRET
    request_data = json.loads(json.dumps(request.POST))

    if webhook_secret:
        # Retrieve the event by verifying the signature using the raw body and secret if webhook signing is configured.
        # signature = request.headers.get('stripe-signature')
        payload = request.body
        # Checks for the signature of stripe.
        signature = request.headers['Stripe-Signature']
        try:
          
            event = stripe.Webhook.construct_event(
                payload=request.body, sig_header=signature, secret=webhook_secret)
            data = event['data']
        except Exception as e:
            return e
        # Get the type of webhook event sent - used to check the status of PaymentIntents.
        event_type = event['type']
    else:
        data = request_data['data']
        event_type = request_data['type']
    data_object = data['object']

    print('event ' + event_type)

    if event_type == 'checkout.session.completed':
        print('🔔 Payment succeeded!')
        customer_email = data_object.customer_details.email
        amount_total = data_object.amount_total
        try:
            member = Members.objects.get(email=customer_email)
            today = timezone.now().date() 
            if(amount_total/100 ==BASIC_PRICE):
                member.membership_date = today + datetime.timedelta(days=BASIC_DURATION)
            else:
                member.membership_date = today + datetime.timedelta(days=PRO_DURATION)
            member.save()
        except Members.DoesNotExist:
            #Handle when member type wrong email when checkout
            return
            


    return JsonResponse({'status': 'success'})