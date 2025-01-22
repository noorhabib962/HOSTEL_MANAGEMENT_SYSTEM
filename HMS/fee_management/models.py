from django.db import models
from student_management.models import Student
from django.utils import timezone

class Payment(models.Model):
    PAY_STATUS = [
        (1, 'Paid'),
        (0, 'Unpaid'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.IntegerField()
    date = models.DateField()
    status = models.IntegerField(choices=PAY_STATUS)

    def month(self):
        return self.date.strftime('%B'), self.date.year

    def __str__(self):
        return f"Fee of {self.student} for {self.date.strftime('%B')} {self.date.year}"
