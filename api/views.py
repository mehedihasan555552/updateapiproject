from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.contrib.auth import get_user_model
User=get_user_model()
import six
import sys
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from rest_framework.utils import json
from rest_framework.response import Response
import requests
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.


from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import parser_classes
from rest_framework.parsers import FileUploadParser,MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status



@api_view(['GET'])
@parser_classes([MultiPartParser])
@permission_classes([IsAuthenticated])
def scretuserdetail(request, pk):
    user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    #serializer.data['user_token'] = 'user_token'
    return Response(serializer.data)




class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client


@api_view(['GET'])
def usersignupdetail(request, pk):
    tasks = User.objects.get(id=pk)
    serializer = UserSerializer(tasks, many=False)
    return Response(serializer.data)




@api_view(['GET'])
def userlist(request):
    users = User.objects.all().filter(seller=True)
    serializer = TaskSerializer(users, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def userdetail(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)



@api_view(['POST',"GET"])
def usercreate(request):
    print(request.data)
    try:
        if "email" in request.data.keys():
            user_object = User.objects.get(email=request.data['email'])
            print(user_object)
        else:
            return Response({"message":"Email already exists"})
    except User.DoesNotExist:
        user_object = None
    if request.method == 'POST':
        print("what is the problem")
        serializer = CustomRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(request=request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""       for k, v in request.data.items():
            setattr(user, k, v)
        user.save()
        serializer = CustomRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
        #     """


@api_view(['POST',"GET"])
def usercreate(request):
    print(request.data)
    try:
        if "email" in request.data.keys():
            user_object = User.objects.get(email=request.data['email'])
            print(user_object)
        else:
            return Response({"message":"Email already exists"})
    except User.DoesNotExist:
        user_object = None
    if request.method == 'POST':
        print("what is the problem")
        serializer = CustomRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(request=request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        


@api_view(['POST'])
def userupdate(request,pk):
    task = Account.objects.get(id=pk)
    for key, value in request.data.items():
        setattr(task, key, value)
    task.save()

    serializer = TaskSerializer(instance = task ,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def userdelete(request,pk=None):
    user= User.objects.get(pk=Token.objects.get(key=response.data['token']).user_id)
    #return Response({'token': token.key, 'id': token.})
    #task = Account.objects.get(id=pk)
    user.delete()
    return Response('Delete successfully.')


@api_view(['GET'])
def joblist(request,filter=None):
    tasks = Job.objects.all()
    if filter:
        tasks=tasks.filter(description__icontains=filter)
    serializer = JobSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def jobdetail(request, pk):
    tasks = Job.objects.get(id=pk)
    serializer = JobSerializer(tasks, many=False)
    return Response(serializer.data)

"""
@api_view(['GET'])
def jobscreated(request, pk):
    tasks = Job.objects.filter(creator=pk)
    serializer = JobSerializer(tasks, many=True)
    return Response(serializer.data)"""

@api_view(['POST'])
@parser_classes([MultiPartParser])
@permission_classes([IsAuthenticated])
def jobcreate(request):
    #print(request.headers)
    print("pk " , Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id)
    print(request.data)
    user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
    user= User.objects.get(pk=user_token)
    print(request.data)
    serializer = JobSerializer(data=request.data, many=False)
    if serializer.is_valid():
        #serializer.save()
        serializer.save(buyer=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#    return Response(serializer.data)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def myjobs(request): #list of jobs i got accepted
    #print(request.headers)
    #print("pk " , Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id)
    #print(request.data)
    user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
    user= User.objects.get(pk=user_token)
    Jobs=Job.objects.filter(seller=user) 
    serializer = JobSerializer(Jobs, many=False)
    if Jobs:
        #serializer.save()
        #serializer.save(seller=request.user,job=job)
        return Response(serializer.data)
    else:
        return Response({"message":"No jobs for you "}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#from .serializers import FileSerializer

"""
class jobcreate(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      file_serializer = JobSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""








@api_view(['POST'])
def jobupdate(request,pk):
    task = Job.objects.get(id=pk)
    for key, value in request.data.items():
        setattr(task, key, value)
    task.save()
    serializer = JobSerializer(instance = task ,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['DELETE'])
def jobdelete(request,pk):
    task = Job.objects.get(id=pk)
    task.delete()
    return Response('Delete successfully.')






@api_view(['GET'])
@permission_classes([IsAuthenticated])
def myoffers(request): #list of offers i got according to a job
    #print(request.headers)
    #print("pk " , Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id)
    #print(request.data)
    user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
    user= User.objects.get(pk=user_token)
    offers=Offer.objects.filter(job__seller=user) #here is a problem
    serializer = OfferSerializer(offers, many=False)
    print(offer.job.buyer)
    if job.buyer==user:
        #serializer.save()
        #serializer.save(seller=request.user,job=job)
        return Response(serializer.data)
    else:
        return Response({"message":"this job is not yours. "}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






@api_view(['GET'])
@permission_classes([IsAuthenticated])
def offerlist(request,pk): #list of offers i got according to a job
    #print(request.headers)
    #print("pk " , Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id)
    #print(request.data)
    user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
    user= User.objects.get(pk=user_token)
    job = Offer.objects.get(id=pk)
    offers=Offer.objects.filter(job=job) #here is a problem
    serializer = OfferSerializer(offers, many=False)
    if job.buyer==user:
        #serializer.save()
        #serializer.save(seller=request.user,job=job)
        return Response(serializer.data)
    else:
        return Response({"message":"this job is not yours. "}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)














@api_view(['POST'])
@permission_classes([IsAuthenticated])
def offercreate(request,pk=None):
    #print(request.headers)
    #print("pk " , Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id)
    #print(request.data)
    user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
    user= User.objects.get(pk=user_token)
    job=Job.objects.get(pk=pk)
    print(request.data)
    serializer = OfferSerializer(data=request.data, many=False)
    if serializer.is_valid():
        #serializer.save()
        serializer.save(seller=request.user,job=job)
        serializer.data["accepted"]=offer.accepted
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET'])
@permission_classes([IsAuthenticated])
def offerdetail(request,pk=None):
    #print(request.headers)
    #print("pk " , Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id)
    #print(request.data)
    user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
    user= User.objects.get(pk=user_token)
    offer = Offer.objects.get(id=pk)
    serializer = OfferDetailsSerializer(offer, many=False)
    print(offer.job.buyer)
    if offer.seller==user or offer.job.buyer==user:
        #serializer.save()
        #serializer.save(seller=request.user,job=job)
        serializer.data["accepted"]=offer.accepted
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def order(request,pk=None):
    #print(request.headers)
    #print("pk " , Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id)
    #print(request.data)
    if pk:
        user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
        user= User.objects.get(pk=user_token)
        offer=Offer.objects.get(pk=pk)
        offer=offer.accepte()
        order=Order()
        order.save(buyer=user ,offer=offer,seller=offer.seller)
        url=order.paypal()
        serializer= OrderSerializer(instance=order)
        if url:
            """if serializer.is_valid():
            #serializer.save()
            serializer.save(seller=request.user,job=job)
            return Response(serializer.data, status=status.HTTP_201_CREATED)"""
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        else:
            return Response( "please try again later", status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






"""
@api_view(['POST'])
def offercreate(request):
   
    try:
        offer_object = Offer.objects.filter(job=request.data['job'],user=request.data['user'])
    except Offer.DoesNotExist:
        offer_object = None
        
    if offer_object:
        return Response({"error":"Offer already submitted"})
    else:
        serializer = OfferSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
"""










@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def review(request,pk_user=None, pk_order=None,is_seller=0):
    if is_seller==0:
        is_seller=False
    else:
        is_seller=True
    user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
    user= User.objects.get(pk=user_token)
    if pk_order and  not request.POST:
        try:
            order=Order.objects.get(pk=pk_order)
        except:
            return Response("there is a problem in the order ID", status=status.HTTP_400_BAD_REQUEST) 
        reviews=Review.objects.filter(order=order)  
        reviews=reviews.filter(buyer=user).filter(seller=user) 
        if is_seller:
            review=reviews.filter(seller_review=is_seller)[0]
            serializer=GetReviewSerializer(instance=reviews)
            return Response(serializer.data)
        else:
            review=reviews.filter(seller_review=is_seller)[1]
    if pk_order and request.POST:
        try:
            order=Order.objects.get(pk=pk_order)
        except:
            return Response("there is a problem in the order ID", status=status.HTTP_400_BAD_REQUEST)
        if not is_seller:
            serializer= BuyerReviewSerializer(request.data)
            if serializer.is_valid():
                serializer.save(buyer=user,order=order)
            #serializer.save(seller=request.user,job=job)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            #return Response(serializer.data ,status=status.HTTP_201_CREATED)
        else:
            serializer= SellerReviewSerializer(request.data,)
            if serializer.is_valid():
                serializer.save(seller=user,seller_review=True,order=order)
            #serializer.save(seller=request.user,job=job)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""@api_view(['GET'])
def userreviews(request,pk):
    tasks = Review.objects.filter(user=pk)
    serializer = ReviewSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def jobreview(request,pk):
    tasks = Review.objects.filter(job=pk)
    serializer = ReviewSerializer(tasks, many=True)
    return Response(serializer.data)"""

@api_view(['DELETE'])
def offerdelete(request,pk):
    task = Offer.objects.get(id=pk)
    task.delete()
    return Response('Delete successfully.')




