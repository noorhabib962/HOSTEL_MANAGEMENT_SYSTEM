from django.contrib import admin
from django.http import HttpResponse
from django.utils.html import format_html
from .models import  Student
from fee_management.models import Payment
from hostel_management.models import Room
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

def generate_payment_report(modeladmin, request, queryset):
    # Create a buffer to hold the PDF data
    buffer = io.BytesIO()

    # Create a canvas object
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, height - 50, "Student Payment Report")

    # Table Header
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 100, "Student")
    c.drawString(200, height - 100, "Amount")
    c.drawString(300, height - 100, "Date")
    c.drawString(400, height - 100, "Status")

    # Fetch Payment Data
    y_position = height - 130
    payments = Payment.objects.all()

    for payment in payments:
        student_name = str(payment.student)
        amount = str(payment.amount)
        date = payment.date.strftime('%Y-%m-%d')
        status = 'Paid' if payment.status == 1 else 'Unpaid'

        c.setFont("Helvetica", 12)
        c.drawString(50, y_position, student_name)
        c.drawString(200, y_position, amount)
        c.drawString(300, y_position, date)
        c.drawString(400, y_position, status)

        y_position -= 20
        if y_position < 50:  # Add a new page if the current page is full
            c.showPage()
            y_position = height - 50

    c.save()

    # Return the PDF as a downloadable response
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')

generate_payment_report.short_description = "Generate Payment Report"



class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'contact_number', 'clickable_room')
    search_fields = ['full_name', 'email']
    list_filter = ['room']
    actions = [generate_payment_report] # Add the action here

    @admin.display(description='Room') 
    def clickable_room(self, obj): 
        if obj.room: return format_html('<a href="/admin/hostel_management/room/{}/change/">{}</a>', obj.room.id, obj.room.room_number) 
        return '-'

admin.site.register(Student, StudentAdmin)


