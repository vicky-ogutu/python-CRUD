from rest_framework import viewsets
from .models import main_clientsModel
from .serializers import mainSerializer

class mainViewsets(viewsets.ModelViewSet):
    queryset = main_clientsModel.objects.all()
    serializer_class =mainSerializer