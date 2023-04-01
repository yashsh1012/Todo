import datetime
from django.shortcuts import render
from .models import CustomUser, Todo, TAG
from .serializers import UserSignUpSerializer, GetProfilSerializer, UpdateProfilSerializer, TodoSerializer, CreateTodoSerializer
from rest_framework.decorators import api_view , authentication_classes, permission_classes 
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.utils.dateparse import parse_date
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

@api_view(['POST'])
def sign_up_api(request):
    if request.method == 'POST' :
        password = request.GET.get('password')
        cpassword = request.GET.get('confirm_password')
        if password != cpassword :
            return Response({'msg': 'Password & Confirm Password are not same'})
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg : User created'})
        return Response(serializer.errors)
    

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def login_api(request):
    if request.method == 'POST' :
        serializer = UserSignUpSerializer(data = request.data)
        user = authenticate(email=request.data.get('email'), password=request.data.get('password'))
        if user is not None:
            return Response({'msg: Login Successful'})
        return Response({'msg: Invalid email and Password'})


    
@api_view(['GET','PUT'])
def profil_api(request, id=None):
    if request.method == 'GET' :
        req_id = request.GET.get('id') or  ""
        if req_id != "" :
            profil = CustomUser.objects.get(id=req_id)
            serializer = GetProfilSerializer(profil)
            return Response(serializer.data)
        profil = CustomUser.objects.all()
        serializer = GetProfilSerializer(profil, many=True)   
        return Response(serializer.data )
    

    # if request.method == 'POST':
    #     serializer = GetProfilSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg : Data Created'})
    #     return Response(serializer.errors)
    
    if request.method == 'PUT' :
        profil = CustomUser.objects.get(id=id)
        serializer = UpdateProfilSerializer(profil, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg: Data Updated'} )
        return Response(serializer.errors)
            

    
@api_view(['GET','PUT','PATCH','POST','DELETE'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def todo_api(request):
    if request.method == 'POST' :
        serializer = CreateTodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg: Data Created'})
        return Response(serializer.errors)  


    if request.method == 'GET':
        req_title = request.GET.get('Title') or ""
        req_description = request.GET.get('Description') or ""
        req_created_date = request.GET.get('Created_Date') or ""
        req_start_date = request.GET.get('start_date') or ""
        req_end_date = request.GET.get('end_date') or ""
        req_due_date = request.GET.get('Due_date') or ""
       # req_day = datetime.date(2023,3,19)
        req_tag = request.GET.get('tag_name') or ""
        req_status = request.GET.get('status') or ""
     #   print(req_day)
        all_todo = Todo.objects.all()

        if req_title != "" :
            all_todo = all_todo.filter(Title__icontains=req_title)

        if req_description != "":   
            all_todo =  all_todo.filter(Description__icontains=req_description)

        if req_start_date and req_end_date != "":
            all_todo = all_todo.filter(Created_Date__range=(req_start_date, req_end_date))
           # all_todo = all_todo.order_by('Created_Date')    

        if req_due_date != "" :
           # date = parse_date(req_due_date)
            all_todo = all_todo.filter(Due_date = req_due_date)

        if req_tag != "" :
            all_todo = all_todo.filter(tag_name__tags__icontains=req_tag)   

        if req_status !="" :
            all_todo = all_todo.filter(status=req_status)      

        serializer = TodoSerializer(all_todo, many=True)
        return Response(serializer.data)

    
    if request.method == 'PUT' :
        req_id = request.GET.get('id') or ""
        query = Todo.objects.get(id=req_id)
        serializer = TodoSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg: Data Updated'})
        return Response(serializer.errors)
    
    if request.method == 'PATCH' :
        req_id = request.GET.get('id') or ""
        query = Todo.objects.get(id=req_id)
        serializer = TodoSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg:Partial Data Updated'})
        return Response(serializer.errors)

    if request.method == 'DELETE' :
        req_id = request.GET.get('id') or ""
        query = Todo.objects.get(id=req_id)
        query.delete()
        return Response({'msg : Data Deleted'})



