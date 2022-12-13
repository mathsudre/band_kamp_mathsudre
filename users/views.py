
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import User
from .permissions import IsAccountOwner
from .serializers import UserSerializer


class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetrieveUpdateDeleteUserView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer
