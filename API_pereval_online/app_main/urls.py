from django.urls import path

from .views import PostAPIView, PostDetailAPIView, AuthEmailPostAPIView

urlpatterns = [
    path('submitData', PostAPIView.as_view()),
    path('submitData/<int:pk>/', PostDetailAPIView.as_view({'get': 'retrieve', 'patch': 'partial_update'})),
    path('submitData/user__email=<str:email>', AuthEmailPostAPIView.as_view({'get': 'list'})),
]
