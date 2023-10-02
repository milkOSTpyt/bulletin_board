from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from bulletin_board_app.models import Advert
from bulletin_board_app.serializers import AdvertListSerializer, AdvertDetailSerializer


class AdvertListViewSet(generics.ListAPIView):
    model = Advert
    serializer_class = AdvertListSerializer

    def get_queryset(self):
        return Advert.objects.all().select_related('city', 'category').order_by('-created_at')


class AdvertDetailViewSet(generics.RetrieveAPIView):
    model = Advert
    serializer_class = AdvertDetailSerializer

    def get(self, request, *args, **kwargs):
        advert_obj = get_object_or_404(Advert, pk=self.kwargs['pk'])
        advert_obj.views += 1
        advert_obj.save()
        result = AdvertDetailSerializer(advert_obj)
        return Response(result.data)

