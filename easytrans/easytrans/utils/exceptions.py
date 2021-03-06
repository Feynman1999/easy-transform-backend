from rest_framework.views import exception_handler as drf_exception_handler
import logging
from django.db import DatabaseError
from redis.exceptions import RedisError
from rest_framework.response import Response
from rest_framework import status

# 和配置文件对应
logger = logging.getLogger('django')

# 在drf的基础上追加
def exception_handler(exc, context):
    """
    :param exc: 异常的示例对象
    :param context: (key: request 和  view)
    :return: Response
    """
    response = drf_exception_handler(exc, context)

    if response is None:
        view = context['view']
        if isinstance(exc, DatabaseError) or isinstance(exc, RedisError):
            # 数据库异常
            logger.error("[{}] {}".format(view, exc))
            response = Response({'message': '服务器内部错误'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)
    return response
