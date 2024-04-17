from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from movieapp.models import Contain
from movieapp.api.serializers import ContainSerializer

#class views
from rest_framework.views import APIView


class ContainListCreateAPIView(APIView):
    def get(self, request):
        contains = Contain.objects.filter(aktif=True)
        serializer = ContainSerializer(contains, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ContainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ContainDetailAPIView(APIView):

    def get_object(self, request, pk):
        contain_instance = get_object_or_404(Contain, pk=pk)
        return contain_instance

    def get(self, request,pk):
        contain = self.get_object(pk=pk)
        serializer = ContainSerializer(contain)
        return Response(serializer.data)


    def put(self, request, pk):
        contain = self.get_object(pk=pk)
        serializer = ContainSerializer(contain, data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        contain = self,get_object(pk=pk)
        contain.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# @api_view(['GET', 'PUT', 'DELETE'])
# def contain_detail_api_view(request, pk):
    
#     try:
#        contain_instance = Contain.objects.get(pk=pk)
#     except Contain.DoesNotExist:
#         return Response(
#         {
#            'errors':{
#               'code': 404,
#               'message': f'No movie related to this id ({pk}) was found.'
#            }
#         },
#        status=status.HTTP_404_NOT_FOUND
        
#         )

#     if request.method == 'GET':
#         serializer = ContainSerializer(contain_instance)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ContainSerializer(contain_instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
        
#     elif request.method == 'DELETE':
#         contain_instance.delete()
#         return Response(
#             {
#                 'process':{
#                     'code': 204,
#                     'message': f'({pk}) id not found.'
#                 }
#             },
#             status=status.HTTP_204_NO_CONTENT
#         )

               
               
               ### FUNCTION METHOD ###
        # @api_view(['GET', 'POST'])
# def contain_list_create_api_view(request):

    # if request.method == 'GET':
    #     contains = Contain.objects.filter(aktif = True)
    #     serializer = ContainSerializer(contains, many=True)
    #     return Response(serializer.data)
    # elif request.method == 'POST':
    #     serializer = ContainSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status = status.HTTP_201_CREATED)
    #     return Response(status=status.HTTP_400_BAD_REQUEST)