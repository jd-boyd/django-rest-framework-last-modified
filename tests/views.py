from datetime import datetime

from rest_framework.response import Response
from rest_framework.views import APIView

from last_modified.decorators import last_modified


def modified_2010(*args, **kwargs):
    return datetime(2010, 1, 1)


class View2010(APIView):
    @last_modified(last_modified_func=modified_2010)
    def get(self, request):
        return Response({'key': '2010'})


class ViewUnwrapped(APIView):
    def get(self, request):
        return Response({'key': 'unwrapped'})
