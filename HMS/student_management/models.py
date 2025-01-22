from django.db import models
from hostel_management.models import Hostel, Room
from django.core.exceptions import ValidationError

class Student(models.Model):
    # Personal Information
    STD_GENDER = [
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other"),
     ]
    
    full_name = models.CharField(max_length=100)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, blank= True, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE,  related_name='students', blank=True, null=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices= STD_GENDER)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)
    address = models.TextField()
    check_in = models.DateField()
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def clean(self):
        # Check if the room is full before assigning a student to it
        if self.room:
            students_in_room = Student.objects.filter(room=self.room).count()
            if students_in_room >= self.room.capacity:
                raise ValidationError(f"Room {self.room.room_number} is already full.")


    def __str__(self):
        return self.full_name
