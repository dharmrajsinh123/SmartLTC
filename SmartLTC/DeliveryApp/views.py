from rest_framework import status, generics, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from rest_framework.permissions import IsAuthenticated
from .models import store, role_mst,user_mst

# from DeliveryApp.serializers import storeSerializer
from rest_framework import generics, filters

from .serializers import StoreSerializer, role_mstSerializer,user_mstSerializer


class StoreViewSet(generics.GenericAPIView, mixins.ListModelMixin,
                   mixins.CreateModelMixin, mixins.UpdateModelMixin,
                   mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    search_fields = ['id']
    filter_backends = (filters.SearchFilter,)
    queryset = store.objects.all()
    serializer_class = StoreSerializer
    lookup_field = 'id'
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    # authentication_classes = [TokenAuthentication]
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


class role_mstViewSet(generics.GenericAPIView, mixins.ListModelMixin,
                      mixins.CreateModelMixin, mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    search_fields = ['id']
    filter_backends = (filters.SearchFilter,)
    queryset = role_mst.objects.all()
    serializer_class = role_mstSerializer
    lookup_field = 'id'
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    # authentication_classes = [TokenAuthentication]
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

class user_mstViewSet(generics.GenericAPIView, mixins.ListModelMixin,
                      mixins.CreateModelMixin, mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    search_fields = ['id']
    filter_backends = (filters.SearchFilter,)
    queryset = user_mst.objects.all()
    serializer_class = user_mstSerializer
    lookup_field = 'id'
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    # authentication_classes = [TokenAuthentication]
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

# from django.shortcuts import render
#
# # Create your views here.
