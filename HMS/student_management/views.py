from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from hostel_management.models import Hostel, Room
from .models import Student
from django.db import DatabaseError
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request,'student_management/student_list.html', {'students':students})

@login_required
def student_create(request):
    if request.method == 'POST':
        try:
            # Handle form submission
            room_id = request.POST.get('room_id')
            room = get_object_or_404(Room, id=room_id)
            students = Student.objects.filter(room=room)

            # Count the number of students in that room
            num_students = students.count()
            if room.capacity == num_students:
                messages.error(request, 'Room is Full!')
                return redirect('student_create')

            else:
        
                full_name = request.POST.get('full_name')
                hostel_id = request.POST.get('hostel_id')
                room_id = request.POST.get('room_id')
                gender = request.POST.get('gender')
                date_of_birth = request.POST.get('date_of_birth')
                contact_number = request.POST.get('contact_number')
                email = request.POST.get('email')
                address = request.POST.get('address')
                photo = request.FILES.get('photo')

                student = Student(
                    full_name=full_name,
                    hostel_id=hostel_id,
                    room_id=room_id,
                    date_of_birth=date_of_birth,
                    gender=gender,
                    contact_number=contact_number,
                    email=email,
                    photo=photo,
                    address=address
                )
                student.save()

                messages.success(request, 'Student successfully created!')
                return redirect('student_list')
        
        except DatabaseError as e:
            # Handle database error
            return HttpResponse(f"An error occurred while saving the hostel: {e}", status=500)
        except Exception as e:
            # Handle any other exceptions
            return HttpResponse(f"An unexpected error occurred: {e}", status=500)
    else:
        hostels = Hostel.objects.all()
        rooms = Room.objects.all()
        # Render the form for GET request
        return render(request, 'student_management/create_student.html',{'hostels':hostels,'rooms':rooms})


def student_edit(request,student_id):
    student = get_object_or_404(Student, pk = student_id)
    if request.method == 'POST':
        try:
            # Handle form submission
            student.full_name = request.POST.get('full_name')
            student.hostel_id = request.POST.get('hostel_id')
            student.room_id = request.POST.get('room_id')
            student.gender = request.POST.get('gender')
            student.date_of_birth = request.POST.get('date_of_birth')
            student.contact_number = request.POST.get('contact_number')
            student.email = request.POST.get('email')
            student.address = request.POST.get('address')
            photo = request.FILES.get('photo')
            if photo:
                student.photo = request.FILES.get('photo')
            
            student.save()
            messages.success(request, 'Student successfully updated!')
            return redirect('student_list')  # Redirect to the list of hostels
        except DatabaseError as e:
            # Handle database error
            return HttpResponse(f"An error occurred while saving the hostel: {e}", status=500)
        except Exception as e:
            # Handle any other exceptions
            return HttpResponse(f"An unexpected error occurred: {e}", status=500)
    else:
        context = {
            'rooms':Room.objects.all(),
            'student':student,
            'hostels' : Hostel.objects.all()
        }

        return render(request, 'student_management/student_edit.html',context)

@login_required
def student_delete(request,student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == "POST":
        messages.success(request, 'Student successfully daleted!')
        student.delete()
        return redirect('student_list')
    
    return render(request, 'student_management/student_confirm_delete.html',{'student':student})
