from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import Postserializers
@api_view(["GET"])
def index(request):
    return Response({"sucess:The setup was succesuful"})

@api_view(["Get"])
def Getallpost(request):
    get_all_post= Post.objects.all()
    serializers=Postserializers(get_all_post,many= True)
    
    return Response(serializers.data)

@api_view(["GET ","POST"])
def addpost(request):
    we=request.method
    data= request.data
    serializers=Postserializers(data=data,many=True)
    if serializers.is_valid :
        serializers.save()
        return Response("Sucess")
    else:
        return Response(serializers.errors,status=400)
@api_view(["DELETE"])
def delete(request):
    id =request.data.get('id')
    post= Post.objects.get(id=id)
    post.delete()
    return Response({"sucess":"THis is working"})
@api_view(["GET","POST"])
def Getoneposts(request):
    try:
        id = request.data.get('id')
        post = Post.objects.get(id=id)
        seria= Postserializers(post)
        return Response(seria.data)
    except Post.DoesNotExist:
        return Response({"id":"The id provided is not vaild"})
    
@api_view(["PUT"])
def updatepost(request):
    id =request.data.get('id')
    new_title= request.data.get('title')
    new_content=request.data.get('content')
    try:
        post = Post.objects.get(id=id)
        if new_title:
         post.title= new_title
        post.save()
        if new_content:
         post.content= new_content
        post.save()
        serializers=Postserializers(post)
        return Response(serializers.data)
    except Post.DoesNotExist:
        return Response({"id":"The id provided is not vaild"})
    