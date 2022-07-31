from django.shortcuts import render
from yaml import serialize
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Post
from .serializers import PostSerializers
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser


# Create your views here.
class PostView(APIView):

    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        queryset = Post.objects.all()
        serializer = PostSerializers(queryset, many=True)
        #if serializer.is_valid():
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializers(post, data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(status=HTTP_204_NO_CONTENT)

@csrf_exempt
def post_list(request):
    if request.method == 'GET':
        queryset = Post.objects.all()
        serializer = PostSerializers(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        data = JSONParser.parser(request)
        serializer = PostSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error, status=400)

@csrf_exempt
def post_detail(request, pk):
    try:
        Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=400)
    
    if request.method == 'GET':
        serializer = PostSerializers(Post)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser.parser(request)
        serializer = PostSerializers(Post, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.error, status=400)

    elif request.method == 'DELETE':
        Post.delete()
        return HttpResponse(status=204)

