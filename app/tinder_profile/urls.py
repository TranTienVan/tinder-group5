from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [    
    path('users', MembersInforAPI.as_view(), name = "setup_profile"),
    path('settings', MembersSettingsAPI.as_view(), name = "setup_settings"),

    path('upgrade', get_example, name = "upgrade"),
    path('config',get_publishable_key, name = "config"),
    path('checkout-session', get_checkout_session, name = "checkout-session"),
    path('create-checkout-session', create_checkout_session, name="create-checkout-session"),
    path('customer_portal', customer_portal, name="customer_portal"),
    path('webhook', csrf_exempt(webhook_received), name="webhook"),
    path('canceled', get_cancel, name="canceled"),
    path('success', get_success, name="success"),
]

