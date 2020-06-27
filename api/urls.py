from django.urls import path
from django.conf.urls import include


from .import views

urlpatterns = [

    path('sellers/', views.userlist,name='userlist'),
    path('user/<str:pk>/', views.userdetail,name='userdetail'),
    path('user-create/', views.usercreate,name='usercreate'),
    path('user-update/<str:pk>', views.userupdate,name='userupdate'),
    path('user-delete/<str:pk>', views.userdelete,name='userdelete'),
    path('job/', views.joblist,name='joblist'),
    path('job/<str:pk>/', views.jobdetail,name='jobdetail'),
    path('myjobs/', views.myjobs,name='myjobs'), 
    #path('jobs-created/<int:pk>/', views.jobscreated,name='jobscreated'),
    path('job-create/', views.jobcreate,name='jobcreate'),
    path('job-update/<int:pk>', views.jobupdate,name='jobupdate'),
    path('job-delete/<int:pk>', views.jobdelete,name='jobdelete'),
    path('offer/<int:pk>/', views.offercreate,name='offerlist'),
    path('myoffers/<str:pk>/', views.myoffers,name='myoffers'),
    path('offer-detail/<str:pk>/', views.offerdetail,name='offerdetail'),
    path('offer-create/<int:pk>/', views.offercreate,name='offercreate'),
    path('offer-delete/<str:pk>', views.offerdelete,name='offerdelete'),
    path('checkout/', views.order, name='paypal'),
    path('review/<int:pk_order>/', views.review,name='review'),
    path('buyerreview/<int:pk_order>/<int:pk_user>/<int:is_seller>/', views.review,name='buyerreview'),
    path('sellerreview/<int:pk_order>/<int:pk_user>/<int:is_seller>/', views.review,name='sellerreview'),
    # path('offer-detail/<str:pk>/', views.offerdetail,name='offerdetail'),
    path('offer-create/', views.offercreate,name='offercreate'),
    #path('offer-delete/<str:pk>', views.offerdelete,name='offerdelete'),
    path('order/<int:pk>/', views.order, name='paypal'),
    path('google/', views.GoogleLogin.as_view(), name='google_login'),
]
