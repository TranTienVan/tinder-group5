from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView, TemplateView

urlpatterns = [
    path("hello_world/", include("hello_world.urls")),
    path("admin/", admin.site.urls),

    re_path(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    re_path(r'^signup/$', TemplateView.as_view(template_name="signup.html"),
        name='signup'),
    re_path(r'^email-verification/$',
        TemplateView.as_view(template_name="email_verification.html"),
        name='email-verification'),
    re_path(r'^login/$', TemplateView.as_view(template_name="login.html"),
        name='login'),
    re_path(r'^logout/$', TemplateView.as_view(template_name="logout.html"),
        name='logout'),
    re_path(r'^password-reset/$',
        TemplateView.as_view(template_name="password_reset.html"),
        name='password-reset'),
    re_path(r'^password-reset/confirm/$',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password-reset-confirm'),

    re_path(r'^user-details/$',
        TemplateView.as_view(template_name="user_details.html"),
        name='user-details'),
    re_path(r'^password-change/$',
        TemplateView.as_view(template_name="password_change.html"),
        name='password-change'),
    re_path(r'^resend-email-verification/$',
        TemplateView.as_view(template_name="resend_email_verification.html"),
        name='resend-email-verification'),

    re_path(r'^dj-rest-auth/', include('dj_rest_auth.urls')),
    re_path(r'^dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    re_path(r'^account/', include('allauth.urls')),
    re_path(r'^accounts/profile/$', RedirectView.as_view(url='/', permanent=True), name='profile-redirect'),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
