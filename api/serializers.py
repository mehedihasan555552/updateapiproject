from rest_framework import serializers
from .models import *
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User=get_user_model()
from rest_framework import serializers



class JobSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    description=serializers.CharField(required=True)
    job_budget=serializers.FloatField(required=True)
    job_hours=serializers.IntegerField(required=False)
    job_media=serializers.FileField(required=False)
    job_time=serializers.DateField(required=False)
    class Meta:
        model = Job
        fields = ["id","description","job_budget","job_hours","job_time","job_media",]


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    description=serializers.CharField(required=True)
    job_budget=serializers.FloatField(required=True)
    job_hours=serializers.IntegerField(required=False)
    job_media=serializers.FileField(required=False)
    job_time=serializers.DateField(required=False)
    class Meta:
        model = Job
        fields = ["id","description","job_budget","job_hours","job_time","job_media",]



class OfferSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    description=serializers.CharField(required=True)
    offer_price=serializers.FloatField(required=True)
    offer_hours=serializers.IntegerField(required=True)
    #job_media=serializers.FileField(required=False)
    price_per_hour=serializers.FloatField(required=True)
    #job=serializers.FloatField(required=True)
    #accepted = serializers.BooleanField( read_only=True)
    class Meta:
        model = Offer
        fields = ["id","description","offer_price","offer_hours","price_per_hour",]

class OfferDetailsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    class Meta:
        model = Offer
        fields = ["id","description","accepted","offer_price","offer_hours","price_per_hour",]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['total_amount',"paied","url_payment","total_amount",]

class GetReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["created","description","rate"]
"""
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["created","description","rate"]

"""

class SellerReviewSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    class Meta:
        model = Review
        fields = ["id","buyer_username","created","description","rate","order"] 


        
class BuyerReviewSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    class Meta:
        model = Review
        fields = ["seller_username","created","description","rate","order"] 



"""
"sller"
"created"
"seller_review"
"description"
"rate"
"order"
"""



from rest_auth.registration.serializers import RegisterSerializer
class CustomRegisterSerializer(RegisterSerializer):

    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True,style={'input_type': 'password'})
    #date_of_birth = serializers.DateField(required=True)
    phone=serializers.CharField(required=True)
    country=serializers.CharField(required=True)
    state=serializers.CharField(required=True)
    address=serializers.CharField(required=True)
    phone=serializers.CharField(required=True)
    specializes=serializers.CharField(required=False)
    description=serializers.CharField(required=False)
    seller=serializers.BooleanField(required=False)
    username=serializers.CharField(required=False)
    first_name=serializers.CharField(required=True)
    last_name=serializers.CharField(required=True)
    profile_picture=serializers.FileField(required=False)
    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'username': self.validated_data.get('username', ''),
            'description': self.validated_data.get('description', ''),
            'seller': self.validated_data.get('seller', ''),
            'phone': self.validated_data.get('phone', ''),
            'country': self.validated_data.get('country', ''),
            'address': self.validated_data.get('address', ''),
            'specializes': self.validated_data.get('specializes', ''),
            'profile_picture':self.validated_data.get('profile_picture', ''),
            #'date_of_birth': self.validated_data.get('date_of_birth', ''),
            
        }
"""
class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email','name','date_of_birth'
        "phone",
        "country",
        "address",
        "specializes",
        "description",
        

        )
        read_only_fields = ('email',)


"""
"""
{"user": 
{
'password1': "hello",
'email':'med25@gmzil.com',
'first_name': 'first_name',
'last_name': 'last_name',
'username': 'usernamedfg',
'description': 'description',
'seller': "True",
'phone': 'phone',
'country': 'country',
'address': 'address',
'specializes': 'specializes',
'date_of_birth': 'date_of_birth'}}



{"user": 
{
"password1":"fgds",
"email":"med25@gmzil.com",
"first_name": "first_name",
"last_name": "last_name",
"username": "usernamedfg",
"description": "description",
"seller": "True",
"phone": "phone",
"country": "country",
"address":"address",
"specializes": "specializes"
}}
{
"password1":"fgdsmedsidi",
"password2":"fgdsmedsidi",
 "state": "state",
"email":"med25@gmzil.com",
"first_name": "first_name",
"last_name": "last_name",
"username": "usernamedfg",
"description": "description",
"seller": "True",
"phone": "phone",
"country": "country",
"address":"address",
"specializes": "specializes"
}

            """