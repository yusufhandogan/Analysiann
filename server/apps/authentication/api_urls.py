from django.conf.urls import *
from rest_framework.authtoken.views import obtain_auth_token

from .api_views import *

urlpatterns = [
    url(r'^login$', APILoginViewSet.as_view(), name='api-login'),
    url(r'^logout$', APILogoutViewSet.as_view(), name='api-logout'),
    url(r'^token$', APITokenViewSet.as_view(), name='api-token'),
    url(r'^user-info$', APIUserInfoViewSet.as_view(), name='api-user-info'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', csrf_exempt(obtain_auth_token), name='api-token-auth'),
    url(r'^facebook-signup/?$', csrf_exempt(FacebookLoginOrSignup.as_view()), name='facebook-login-signup'),

]
