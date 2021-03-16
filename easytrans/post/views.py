from .models import Poster
from .serializers import PosterSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class PosterViewSet(ModelViewSet):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer
    # 指定权限
    permission_classes = [IsAuthenticatedOrReadOnly]
    # 对于put和delete，要额外进行判断，即只能修改或删除自己的poster

    # 过滤
    filter_fields = ('title', )  # 可以过滤的域
