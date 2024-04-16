from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from movieapp.models import Contain
from movieapp.api.serializers import ContainSerializer

@api_view(['GET', 'POST'])
def contain_list_create_api_view(request):

    if request.method == 'GET':
        contains = Contain.objects.filter(aktif = True)
        serializer = ContainSerializer(contains, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ContainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)