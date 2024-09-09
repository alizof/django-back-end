# Libs
import datetime 
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

# Modules/Serializer
from .serializers import UserLoginSerializer

# Utils
from utils.api_response import api_response


# Login
class UserLoginAPIViewSet(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']


            user = authenticate(username=username, password=password)
            if user is not None:

                refresh = RefreshToken.for_user(user)
                user.last_login = datetime.datetime.now() 
                user.save()

                return api_response.poui_simple_response(
                    {
                        "token": str(refresh.access_token),
                        "refresh_token": str(refresh)
                    },
                    [
                        api_response.poui_default_msg(200,'information',f'Bem-vindo(a) de volta {user.username}.')
                    ]
                )
            else:
                return api_response.poui_msg_simple_response(401,'error','Credenciais inválidas','',status.HTTP_401_UNAUTHORIZED)
        else:
            return api_response.poui_default_msg(400,'errow',serializer.errors,'',status=status.HTTP_400_BAD_REQUEST)
        
        
        
        
class TokenValidationAPIViewSet(APIView):
    def get(self,request):
        
        token = request.headers.get('Authorization').split()
        
        if len(token) != 2 or token[0].lower() != 'bearer':
            return api_response.poui_msg_simple_response(400, 'error', 'Token inválido no cabeçalho.', '', status.HTTP_400_BAD_REQUEST)

        if not token[1]:
            return api_response.poui_msg_simple_response(400,'error','Token nao informado.','',status.HTTP_400_BAD_REQUEST)

        try:
            AccessToken(token[1])
            
            return api_response.poui_simple_response(True)
                
        except TokenError as e:
            return api_response.poui_msg_simple_response(401,'error',str(e),'',status.HTTP_400_BAD_REQUEST)
 

class CustomTokenRefreshView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        if refresh_token:
            try:
                token = RefreshToken(refresh_token)

                token.verify()
                new_access_token = token.access_token
                
                return api_response.poui_simple_response({
                    "token": str(new_access_token),
                    "refresh_token": str(refresh_token)
                })
            except Exception as e:
                return api_response.poui_msg_simple_response(401,'error',str(e),'',status.HTTP_400_BAD_REQUEST)
        else:
            return api_response.poui_msg_simple_response(400,'error','Refresh Token nao e provido.','',status.HTTP_401_UNAUTHORIZED)
