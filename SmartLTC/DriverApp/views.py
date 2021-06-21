# from rest_framework import status, generics, mixins
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
#
# from rest_framework.permissions import IsAuthenticated
# from .models import Driver
#
# # from DriverApp.serializers import DriverSerializer
# from rest_framework import generics,filters
#
# from .serializers import DriverSerializer
#
#
# class DriverViewSet(generics.GenericAPIView,mixins.ListModelMixin,
#                       mixins.CreateModelMixin,mixins.UpdateModelMixin,
#                      mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
#     search_fields = ['driver_id']
#     filter_backends = (filters.SearchFilter,)
#     queryset = Driver.objects.all()
#     serializer_class = DriverSerializer
#     lookup_field = 'driver_id'
#     # authentication_classes = [SessionAuthentication,BasicAuthentication]
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, driver_id=None):
#         if driver_id:
#             return self.retrieve(request)
#         else:
#             return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#     def put(self, request, driver_id=None):
#         return self.update(request, driver_id)
#
#     def delete(self, request, driver_id):
#         return self.destroy(request, driver_id)