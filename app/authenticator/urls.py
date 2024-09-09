from django.urls import path

# Views
from app.authenticator import views as auth_views


# NotAuth
urlpatterns = [
    path('auth/login/', auth_views.UserLoginAPIViewSet.as_view(), name='auth_login'),
    path('auth/token/', auth_views.TokenValidationAPIViewSet.as_view(), name='token_validation'),
    path('auth/token/refresh/', auth_views.CustomTokenRefreshView.as_view(), name='token_refresh'),
]
