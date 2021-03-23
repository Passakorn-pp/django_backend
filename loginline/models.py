from django.db import models

class UserLine(models.Model):
    id_user = models.CharField(max_length=100, primary_key=True, )
    name_user = models.CharField(max_length=100)
    id_auto = models.CharField(max_length=10000,default='10001')
    def __str__(self):
        return f"{ self.id_user} {self.name_user}"

class DataUser(models.Model):
    id_user = models.ForeignKey(UserLine, on_delete=models.CASCADE)
    faculty = models.CharField(max_length=100)
    img = models.CharField(max_length=1000)
    gender = models.CharField(max_length=50)
    year = models.IntegerField(default=1)
    behavior = models.CharField(max_length=1000)

class Dormitory(models.Model):
    id_user = models.ForeignKey(UserLine, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    water_bill = models.IntegerField()
    elect_bill = models.IntegerField()
    img = models.CharField(max_length=1000)
    facbook = models.CharField(max_length=50)
    line = models.CharField(max_length=50)
    call = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    star = models.IntegerField()
    distance = models.IntegerField()
    tags = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.name   
class Imgall(models.Model):
    dormitory = models.ForeignKey(Dormitory, on_delete=models.CASCADE)
    img = models.CharField(max_length=5000)
    def __str__(self):
        return self.dormitory.name


class Room(models.Model):
    dormitory = models.ForeignKey(Dormitory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    free = models.IntegerField()
    qrcode = models.CharField(max_length=50)
    img = models.CharField(max_length=1000,default="https://sv1.picz.in.th/images/2021/03/14/D12sTl.png")
    def __str__(self):
        return f"{ self.dormitory} { self.name}"  

class filterDo(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    air = models.BooleanField(default=False)
    fan = models.BooleanField(default=False)
    refrigerator = models.BooleanField(default=False)
    table = models.BooleanField(default=False)
    tv = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    
class filterDormitory(models.Model):
    dormitory = models.ForeignKey(Dormitory, on_delete=models.CASCADE)
    elevators = models.BooleanField(default=False)
    keycard = models.BooleanField(default=False)
    laundry = models.BooleanField(default=False)
    parking_lot = models.BooleanField(default=False)
    security_camera = models.BooleanField(default=False)
    def __str__(self):
        return f"{ self.id}"  
    
class Question(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(UserLine, on_delete=models.CASCADE)
    dormitory = models.ForeignKey(Dormitory, on_delete=models.CASCADE)
    comment = models.TextField()

class Answer(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    body = models.TextField()
    user = models.ForeignKey(UserLine, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class History(models.Model):
    user = models.ForeignKey(UserLine, on_delete=models.CASCADE)
    dormitory = models.ForeignKey(Dormitory, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user,self.dormitory}"  

class HistoryNouser(models.Model):
    dormitory = models.ForeignKey(Dormitory, on_delete=models.CASCADE) 
    def __str__(self):
        return f"{ self.dormitory}"  

class Like(models.Model):
    user = models.ForeignKey(UserLine, on_delete=models.CASCADE)
    dormitory = models.ForeignKey(Dormitory, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user, self.dormitory}"   

class Rating(models.Model):
    user = models.ForeignKey(UserLine, on_delete=models.CASCADE)
    dormitory = models.ForeignKey(Dormitory, on_delete=models.CASCADE)
    star = models.FloatField()

class Behavior(models.Model):
    user = models.ForeignKey(UserLine, on_delete=models.CASCADE)
    game = models.BooleanField(default=False)
    book = models.BooleanField(default=False)
    song = models.BooleanField(default=False)
    pray = models.BooleanField(default=False)
    exercise = models.BooleanField(default=False)
    cocial = models.BooleanField(default=False)
    art = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    clean = models.BooleanField(default=False)
    movie = models.BooleanField(default=False)
    homework = models.BooleanField(default=False)
    lie_about = models.BooleanField(default=False)
