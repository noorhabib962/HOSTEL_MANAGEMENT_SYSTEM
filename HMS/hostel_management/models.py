from django.db import models

# Create your models here.
class Hostel(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20)
    capacity = models.IntegerField()
    address = models.TextField(default='')

    def __str__(self):
        return self.name
    

class Room(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=20, unique=True)
    capacity = models.IntegerField()
    description = models.TextField(default='')
    rent = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_students(self): 
        return self.students.count()
    
    def status(self):     
        students_in_room = self.students.count()
        if students_in_room == self.capacity:
            return "Full"
        else:
             return "Not Full"

    def __str__(self):
        return self.description