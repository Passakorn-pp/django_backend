from loginline.models import UserLine,Dormitory,Room,filterDo,filterDormitory,DataUser,Question,Answer,History,HistoryNouser,Like
from rest_framework import generics,mixins
from loginline.api.serializers import UserLineSerializers
import json 
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

class UserLineApiView  (mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):

    queryset = UserLine.objects.all()
    serializer_class = UserLineSerializers

    def post(self,request, *args, **kwargs):
        mydata = json.loads(request.body)
        db = UserLine.objects.filter(id_user = mydata["id_user"])

        if(db):
            db2 = UserLine.objects.get(id_user = mydata["id_user"])
            if(mydata["type_user"]=="User"):
                if(DataUser.objects.filter(id_user = db2)):
                    return JsonResponse({"user" : mydata["type_user"],"state" : "yes"})
                else:
                    return JsonResponse({"user" : mydata["type_user"],"state" : "no"})
            if(mydata["type_user"]=="Dormitory"):
                if(Dormitory.objects.filter(id_user = db2)):
                    dor = Dormitory.objects.filter(id_user = db2)
                    return JsonResponse({"user" : mydata["type_user"],"state" : "yes","name" : dor[0].name})
                else:
                    return JsonResponse({"user" : mydata["type_user"],"state" : "no"})
            
            
        else:
            return JsonResponse({"user" : mydata["type_user"],"state" : "no"})
        
        

        # return JsonResponse({"status" : "Success"})

    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


def GetMormitory(request):
    if request.method == 'GET':
        dormitory = Dormitory.objects.all()
        data = list(dormitory.values())
        data4 = list(dormitory.values())
        # data2 = list(room.values())
        # data3 = list(filterDor.values())
        for i in range(len(data)):
            room = Room.objects.filter(dormitory_id = data[i]['id'])
            filterDor = filterDormitory.objects.filter(dormitory_id = data[i]['id'])
            data2 = list(room.values())
            data5 = list(filterDor.values())
            data4[i].update({"filterDor" : data5})
            data4[i].update({"room" : data2})
            
            
            for j in range(len(data4[i]['room'])):
                filterRoom = filterDo.objects.filter(room_id = data2[j]['id'])
                data3 = list(filterRoom.values())
                data4[i]['room'][j].update({"filter" : data3})

        return JsonResponse({"dormitory" : data4,},  safe=False)
        # serialized = serializers.serialize("json", dormitory,)
        # return HttpResponse(serialized, content_type='application/json')

@csrf_exempt
def GetMormitoryClick(request):
    if request.method == 'POST':
        mydata = json.loads(request.body)
        dormitory = Dormitory.objects.filter(name = mydata["name"])
        data = list(dormitory.values())
        filterDor = filterDormitory.objects.filter(dormitory_id = data[0]['id'])
        room = Room.objects.filter(dormitory_id = data[0]['id'])
        data5 = list(filterDor.values())
        data2 = list(room.values())
        data[0].update({"filterDor" : data5})
        data[0].update({"room" : data2})
        for j in range(len(data[0]['room'])):
                filterRoom = filterDo.objects.filter(room_id = data2[j]['id'])
                data3 = list(filterRoom.values())
                data[0]['room'][j].update({"filter" : data3})

        

        return JsonResponse({"dormitory" : data,}, safe=False)

@csrf_exempt
def addDataUser(request):
    if request.method == 'POST':
        mydata = json.loads(request.body)

        u_line = UserLine(id_user=mydata["id_user"], name_user=mydata["name_user"])
        u_line.save()

        id_line = UserLine.objects.get(id_user=mydata["id_user"])

        data_u_line = DataUser(id_user=id_line,faculty=mydata["faculty"],gender =mydata["gender"])
        data_u_line.save()
        
        return HttpResponse("success")

@csrf_exempt
def addDataDormitory(request):
    if request.method == 'POST':
        mydata = json.loads(request.body)

        u_line = UserLine(id_user=mydata["id_user"], name_user=mydata["name_user"])
        u_line.save()

        id_line = UserLine.objects.get(id_user=mydata["id_user"])

        data_dor = Dormitory(id_user=id_line,
                                name=mydata["name"],
                                water_bill =mydata["water_bill"],
                                elect_bill =mydata["elect_bill"],
                                facbook =mydata["facebook"],
                                line =mydata["line"],
                                call =mydata["call"],
                                address =mydata["address"],
                                tags =mydata["environment"],
                                gender =mydata["typedormitory"],
                                img = mydata["img"],
                                star = 5,
                                distance = 0
                                )
        data_dor.save()

        d_parking_lot = False
        d_elevators = False
        d_security_camera = False
        d_keycard = False
        d_laundry = False
        if(mydata["filterDor"].count("elevators")>0):
            d_elevators = True
        if(mydata["filterDor"].count("keycard")>0):
            d_keycard = True
        if(mydata["filterDor"].count("laundry")>0):
            d_laundry = True
        if(mydata["filterDor"].count("parking_lot")>0):
            d_parking_lot = True
        if(mydata["filterDor"].count("security_camera")>0):
            d_security_camera = True
        
        data_filterdor = filterDormitory(dormitory=data_dor,
                                elevators=d_elevators,
                                keycard = d_keycard,
                                laundry = d_laundry,
                                parking_lot = d_parking_lot,
                                security_camera = d_security_camera,
                                )
        data_filterdor.save()

        for i in range(len(mydata["room"])):

            data_room = Room(dormitory=data_dor,
                            name= mydata["room"][i]["nameroom"],
                            price = mydata["room"][i]["price"],
                            free = mydata["room"][i]["free"],
                            img = mydata["room"][i]["img"]
                            )

            data_room.save()

            d_air = False
            d_fan = False
            d_refrigerator = False
            d_table = False
            d_tv = False
            d_wifi = False
            if(mydata["room"][i]["filter"].count("air")>0):
                d_air = True
            if(mydata["room"][i]["filter"].count("fan")>0):
                d_fan = True
            if(mydata["room"][i]["filter"].count("refrigerator")>0):
                d_refrigerator = True
            if(mydata["room"][i]["filter"].count("table")>0):
                d_table = True
            if(mydata["room"][i]["filter"].count("tv")>0):
                d_tv = True
            if(mydata["room"][i]["filter"].count("wifi")>0):
                d_wifi = True

            data_filterroom = filterDo(room=data_room,
                                air=d_air,
                                fan = d_fan,
                                refrigerator = d_refrigerator,
                                table = d_table,
                                tv = d_tv,
                                wifi = d_wifi
                                )
            data_filterroom.save()
        
        return HttpResponse("success")

@csrf_exempt
def Question_view(request):
    if request.method == 'POST':
        mydata = json.loads(request.body)
        dormitory = Dormitory.objects.get(name=mydata["name"])
        user = UserLine.objects.get(id_user=mydata["user"])
        question = Question(user=user, dormitory = dormitory, comment = mydata["comment"])

        question.save()

        return HttpResponse("success")

        

@csrf_exempt
def Answer_view(request):
    if request.method == 'POST':
        mydata = json.loads(request.body)
        user = UserLine.objects.get(id_user=mydata["name"])
        question = Question.objects.get(id= mydata["id"])
        answer = Answer(body = mydata["body"], user=user, question=question)

        answer.save()

        return HttpResponse("success")

@csrf_exempt
def get_Question(request):
    if request.method == 'POST':
        mydata = json.loads(request.body)
        dormitory = Dormitory.objects.get(name = mydata["name"])
        question = Question.objects.filter(dormitory = dormitory)
        
        data = list(question.values())
        

        count = 0
        for i in question:
            # user = UserLine.objects.filter(id_user=question.user.id_user)
            # data[count].update({"user" : user.values()})
            user = UserLine.objects.filter(id_user=i.user_id)
            data3 = list(user.values())
            data[count].update({"user" : data3[0]})
            
            answer = Answer.objects.filter(question = i)
            data2 = list(answer.values())
            data[count].update({"answer" : data2})
            

            count2 = 0
            for j in answer:
                user = UserLine.objects.filter(id_user=j.user_id)
                data4 = list(user.values())
                # print(data[count]['answer'])
                data[count]['answer'][count2].update({"user" : data4[0]})
                count2 += 1
            count += 1
        
        return JsonResponse({"Question" : data,}, safe=False)

# def getRecommend():
#     if request.method == 'GET':
#         recommend = Autoencoder.objects.all()
#         data = list(recommend.values())
#         return JsonResponse({"Question" : data,}, safe=False)


@csrf_exempt
def GetData(request):
    if request.method == 'POST':
        mydata = json.loads(request.body)

        id_line = UserLine.objects.get(id_user=mydata["id_user"])
        data_user = DataUser.objects.filter(id_user = id_line.id_user)

        data = list(data_user.values())
        
    return JsonResponse({"Data" : data}, safe=False)

@csrf_exempt
def updateData(request):
    if request.method == 'POST':
        mydata = json.loads(request.body)

        id_line = UserLine.objects.get(id_user=mydata["id_user"])
        id_data = DataUser.objects.filter(id_user = id_line.id_user)
        data = list(id_data.values())
        print(data)
        data_user = DataUser(id = data[0]['id'],
                            id_user = id_line,
                            faculty = mydata["faculty"],
                            gender = mydata["gender"])
        data_user.save()
        
    return HttpResponse("success")

@csrf_exempt
def updateDataDormitory(request):
    if request.method == 'POST':
        mydata = json.loads(request.body)

        id_line = UserLine.objects.get(id_user=mydata["id_user"])
        id_dor = Dormitory.objects.get(name=mydata["name"])
        data_dor = Dormitory(id = id_dor.id,
                                id_user=id_line,
                                name=mydata["name"],
                                water_bill =mydata["water_bill"],
                                elect_bill =mydata["elect_bill"],
                                facbook =mydata["facebook"],
                                line =mydata["line"],
                                call =mydata["call"],
                                address =mydata["address"],
                                tags =mydata["environment"],
                                gender =mydata["typedormitory"],
                                star = id_dor.star,
                                distance = id_dor.distance,
                                img = id_dor.img
                                )
        data_dor.save()

        d_parking_lot = False
        d_elevators = False
        d_security_camera = False
        d_keycard = False
        d_laundry = False
        if(mydata["filterDor"][0]["elevators"] == True):
            d_elevators = True
        if(mydata["filterDor"][0]["keycard"] == True):
            d_keycard = True
        if(mydata["filterDor"][0]["laundry"] == True):
            d_laundry = True
        if(mydata["filterDor"][0]["parking_lot"] == True):
            d_parking_lot = True
        if(mydata["filterDor"][0]["security_camera"] == True):
            d_security_camera = True
        id_filterdor = filterDormitory.objects.filter(dormitory=data_dor)
        data_filterdor = filterDormitory(id = id_filterdor[0].id,
                                dormitory=data_dor,
                                elevators=d_elevators,
                                keycard = d_keycard,
                                laundry = d_laundry,
                                parking_lot = d_parking_lot,
                                security_camera = d_security_camera,
                                )
        data_filterdor.save()

        

        for i in range(len(mydata["room"])):
            id_room = Room.objects.filter(dormitory=data_dor)
            data_room = Room(id = id_room[i].id,
                            dormitory=data_dor,
                            name= mydata["room"][i]["name"],
                            price = mydata["room"][i]["price"],
                            free = mydata["room"][i]["free"]
                            )

            data_room.save()

            d_air = False
            d_fan = False
            d_refrigerator = False
            d_table = False
            d_tv = False
            d_wifi = False
            if(mydata["room"][i]["filter"][0]["air"] == True):
                d_air = True
            if(mydata["room"][i]["filter"][0]["fan"] == True):
                d_fan = True
            if(mydata["room"][i]["filter"][0]["refrigerator"] == True):
                d_refrigerator = True
            if(mydata["room"][i]["filter"][0]["table"] == True):
                d_table = True
            if(mydata["room"][i]["filter"][0]["tv"] == True):
                d_tv = True
            if(mydata["room"][i]["filter"][0]["wifi"] == True):
                d_wifi = True
            id_filterroom = filterDo.objects.filter(room=data_room)
            data_filterroom = filterDo(id=id_filterroom[0].id,
                                room=data_room,
                                air=d_air,
                                fan = d_fan,
                                refrigerator = d_refrigerator,
                                table = d_table,
                                tv = d_tv,
                                wifi = d_wifi
                                )
            data_filterroom.save()
        
        return HttpResponse("success")

@csrf_exempt
def sethistory(request):
    if request.method == 'POST':
        mydata = json.loads(request.body)
        dormitory = Dormitory.objects.get(name = mydata["name"])
        if(UserLine.objects.filter(id_user = mydata["user_id"])):
            user = UserLine.objects.get(id_user = mydata["user_id"])
            if(History.objects.filter(user=user)):
                user = UserLine.objects.get(id_user = mydata["user_id"])
            else:
                history = History(user=user,dormitory=dormitory)    
                history.save()
        else:
            nouser = HistoryNouser(dormitory=dormitory)
            nouser.save()

    return HttpResponse("success")

@csrf_exempt
def gethistory(request):
    if request.method == 'POST':
        mydata = json.loads(request.body)
        data = ""
        data2 = ""
        dormitory = Dormitory.objects.get(name = mydata["name"])
        if(HistoryNouser.objects.filter(dormitory=dormitory)):
            nouser = HistoryNouser.objects.filter(dormitory=dormitory)
            data = list(nouser.values())
        if(History.objects.filter(dormitory=dormitory)):
            user = History.objects.filter(dormitory=dormitory)
            data2 = list(user.values())
            for i in range(len(user)):
                user_data = DataUser.objects.filter(id_user=user[i].user_id)
                data3 = list(user_data.values())
                data2[i].update({"datauser" : data3})

            
            
    return JsonResponse({"NoUser" : data, "User" : data2}, safe=False)

@csrf_exempt
def setlike(request):
    if request.method == 'POST':
        mydata = json.loads(request.body)
        dormitory = Dormitory.objects.get(name = mydata["name"])
        user = UserLine.objects.get(id_user = mydata["user_id"])
        if(mydata["status"] == "like"):
            like_dormitory = Like(user=user,dormitory=dormitory)
            like_dormitory.save()
        else:
            delete_like = Like.objects.get(user=user,dormitory=dormitory)
            delete_like.delete()
    return HttpResponse("success")

@csrf_exempt
def getlike(request):
    if request.method == 'POST':
        data = ""
        mydata = json.loads(request.body)
        dormitory = Dormitory.objects.get(name = mydata["name"])
        user = UserLine.objects.get(id_user = mydata["user_id"])
        if(Like.objects.filter(user=user,dormitory=dormitory)):
            data = "เพิ่มแล้ว"   
        else:
            data = "เพิ่มในรายการที่สนใจ"
    return JsonResponse(data, safe=False)

@csrf_exempt
def GetUserLike(request):
    if request.method == 'POST':
        mydata = json.loads(request.body)
        user = UserLine.objects.get(id_user = mydata["user_id"])
        like_dormitory = Like.objects.filter(user=user)
        data = list(like_dormitory.values())
        for i in range(len(like_dormitory)):
            dormitory = Dormitory.objects.filter(id=like_dormitory[i].dormitory_id)
            data1 = list(dormitory.values())
            data[i].update({"dormitory" : data1})
            filterDor = filterDormitory.objects.filter(dormitory_id = data[i]["dormitory"][0]['id'])
            data2 = list(filterDor.values())
            data[i].update({"filterdormitory" : data2})
            room = Room.objects.filter(dormitory_id = data[i]["dormitory"][0]['id'])
            data3 = list(room.values())
            data[i].update({"room" : data3})
            for j in range(len(data[i]['room'])):
                filterRoom = filterDo.objects.filter(room_id = data[i]['room'][j]['id'])
                data4 = list(filterRoom.values())
                data[i]['room'][j].update({"filter" : data4})

        return JsonResponse({"dormitory" : data,},  safe=False)
    
@csrf_exempt
def GetMormitoryLike(request):
    if request.method == 'POST':
        mydata = json.loads(request.body)
        dormitory = Dormitory.objects.get(name=mydata['name'])
        like = Like.objects.filter(dormitory=dormitory)
        data = list(like.values())
    return JsonResponse(data,  safe=False)