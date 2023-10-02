from django.urls import path
from rest_framework import routers

from bulletin_board_app.views import AdvertListViewSet, AdvertDetailViewSet


router = routers.DefaultRouter()
urlpatterns = router.urls

urlpatterns += [
    path('advert-list/', AdvertListViewSet.as_view(),
         name='advert-list'),
    path('advert/<int:pk>', AdvertDetailViewSet.as_view(),
         name='advert'),
]
