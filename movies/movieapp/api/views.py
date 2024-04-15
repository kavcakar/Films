from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from movieapp.models import Contain
from movieapp.api.serializers import ContainSerializer

@api_view(['GET'])
def contain_list_create_api_view(request):

    if request.method == 'GET':
        contains = Contain.objects.filter(aktif = True)
        serializer = ContainSerializer(contains)