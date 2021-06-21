from rest_framework import status, generics, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from rest_framework.permissions import IsAuthenticated
from .models import Company

from CompanyApp.serializers import CompanySerializer
from rest_framework import generics,filters

class CompanyViewSet(generics.GenericAPIView,mixins.ListModelMixin,
                      mixins.CreateModelMixin,mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    search_fields = ['id']
    filter_backends = (filters.SearchFilter,)
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = 'id'
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)