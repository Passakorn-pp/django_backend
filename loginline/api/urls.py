from django.urls import path
from loginline.api.views import UserLineApiView,GetMormitory,GetMormitoryClick,addDataUser,addDataDormitory,Question_view,Answer_view,get_Question,updateDataDormitory,sethistory,gethistory,setlike,getlike,GetMormitoryLike,GetUserLike,GetData,updateData,SetRating,GetRating,GetReccomend
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('sentuserline/', UserLineApiView.as_view() , name="sent_userline"),
    path('getDormitory/', GetMormitory , name="get_dormitory"),
    path('DormitoryClick/', GetMormitoryClick , name="dormitoryClick"),
    path('addDataUser/', addDataUser , name="addDataUser"),
    path('addDataDormitory/', addDataDormitory , name="addDataDormitory"),
    path('addQuestion/', Question_view , name="addQuestion"),
    path('addAnswer/', Answer_view , name="addAnswer"),
    path('get_Question/', get_Question , name="getQuestion"),
    path('updateDataDormitory/', updateDataDormitory , name="updateDataDormitory"),
    path('history/', sethistory , name="history"),
    path('gethistory/',  gethistory , name=" gethistory"),
    path('setlike/',  setlike , name="setlike"),
    path('getlike/',  getlike , name="getlike"),
    path('GetMormitoryLike/', GetMormitoryLike , name="GetMormitoryLike"),
    path('GetUserLike/',  GetUserLike , name="GetUserLike"),
    path('GetData/', GetData , name="GetData"),
    path('updateData/', updateData , name="updateData"),
    path('GetRating/', GetRating, name="GetRating"),
    path('SetRating/', SetRating , name="SetRating"),
    path('GetReccomend/', GetReccomend , name="GetReccomend"),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)