from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics, viewsets, mixins
from django.http import JsonResponse

from .models import CustomUser, Coords, Post, Images
from .serializers import UserSerializer, CoordsSerializer, PostSerializer, PostDetailSerializer, AuthEmailPostSerializer


class PostAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request):
        pereval = PostSerializer(data=request.data)
        try:
            if pereval.is_valid(raise_exception=True):
                pereval.save()
                data = {'status': '200', 'message': 'null', 'id': f'{pereval.instance.id}'}
                return JsonResponse(data, status=200, safe=False)

        except Exception as exc:
            responseData = {'status': '400', 'message': f'Bad Request: {exc}', 'id': 'null'}
            return JsonResponse(responseData, status=400, safe=False)


class PostDetailAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        try:
            instance = Post.objects.get(pk=pk)
        except:
            return Response({'error': 'Post id not found'}, status=400)

        if instance.status != "N":
            return Response({'message': 'Status not "N"', 'state': 0}, status=400)
        else:
            serializer = PostDetailSerializer(data=request.data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'state': 1}, status=200)


class AuthEmailPostAPIView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = AuthEmailPostSerializer

    def get(self, request, *args, **kwargs):
        email = kwargs.get('email', None)
        if Post.objects.filter(user__email=email).is_exist == True:
            responseData = AuthEmailPostSerializer(Post.objects.filter(user__email=email), many=True).data
        else:
            responseData = {'message': f'Posts with current email ({email}) not found'}

        return Response(responseData, status=200)
