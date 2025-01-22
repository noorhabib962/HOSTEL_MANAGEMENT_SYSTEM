from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import HostelForm
from .models import Hostel, Room
from student_management.models import Student
from django.db import DatabaseError
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
@login_required
def hostel_list(request):
    hostel = Hostel.objects.all()
    return render(request,'hostel_management/hostel_list.html', {'hostel':hostel})

@login_required
def hostel_details(request,hostel_id):
             hostel = get_object_or_404(Hostel, pk=hostel_id)
             return render(request,'hostel_management/hostel_details.html',{'hostel':hostel})

@login_required
def hostel_create(request):
    if request.method == 'POST':
        try:
            # Handle form submission
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            capacity = request.POST.get('capacity')
            address = request.POST.get('address')

            # Save the hostel to the database
            Hostel.objects.create(
                name=name,
                email=email,
                phone=phone,
                capacity=capacity,
                address=address
            )
            messages.success(request, 'Hostel successfully created!')
            return redirect('hostel_list')  # Redirect to the list of hostels
        except DatabaseError as e:
            # Handle database error
            return HttpResponse(f"An error occurred while saving the hostel: {e}", status=500)
        except Exception as e:
            # Handle any other exceptions
            return HttpResponse(f"An unexpected error occurred: {e}", status=500)
    else:
        # Render the form for GET request
        return render(request, 'hostel_management/create_hostel.html')


def hostel_edit(request,hostel_id):
    hostel = get_object_or_404(Hostel, pk = hostel_id)
    if request.method == 'POST':
        try:
            # Handle form submission
            hostel.name = request.POST.get('name')
            hostel.email = request.POST.get('email')
            hostel.phone = request.POST.get('phone')
            hostel.capacity = request.POST.get('capacity')
            hostel.address = request.POST.get('address')
            hostel.save()
            messages.success(request, 'Hostel successfully updated!')
            return redirect('hostel_list')  # Redirect to the list of hostels
        except DatabaseError as e:
            # Handle database error
            return HttpResponse(f"An error occurred while saving the hostel: {e}", status=500)
        except Exception as e:
            # Handle any other exceptions
            return HttpResponse(f"An unexpected error occurred: {e}", status=500)
    else:
        context = {
            'hostel':hostel
        }
        return render(request, 'hostel_management/hostel_edit.html',context)

@login_required
def hostel_delete(request,hostel_id):
    hostel = get_object_or_404(Hostel, pk=hostel_id)
    if request.method == "POST":
        messages.success(request, 'Hostel successfully daleted!')
        hostel.delete()
        return redirect('hostel_list')
    
    return render(request, 'hostel_management/hostel_confirm_delete.html',{'hostel':hostel})



@login_required
def room_create(request):
    if request.method == 'POST':
        try:
            # Handle form submission
            room_number = request.POST.get('room_number')
            description = request.POST.get('description')
            capacity = request.POST.get('capacity')
            rent = request.POST.get('rent')
            hostel_id = request.POST.get('hostel_id')
            # Save the hostel to the database
            Room.objects.create(
                room_number=room_number,
                capacity=capacity,
                description=description,
                rent=rent,
                hostel_id=hostel_id,
            )
            messages.success(request, 'Room successfully created!')
            return redirect('room_list')  # Redirect to the list of hostels
        except DatabaseError as e:
            # Handle database error
            return HttpResponse(f"An error occurred while saving the hostel: {e}", status=500)
        except Exception as e:
            # Handle any other exceptions
            return HttpResponse(f"An unexpected error occurred: {e}", status=500)
    else:
        hostels = Hostel.objects.all()
        # Render the form for GET request
        return render(request, 'hostel_management/create_room.html',{'hostels':hostels})


@login_required
def room_list(request):
    # rooms = Room.objects.all()
    rooms = Room.objects.annotate(student_count=Count('students'))
    return render(request,'hostel_management/room_list.html', {'rooms':rooms})

@login_required
def room_std_list(request,room_id):
    students = Student.objects.filter(room_id=room_id)
    return render(request,'student_management/room_students_list.html', {'students':students})

def room_edit(request,room_id):
    room = get_object_or_404(Room, pk = room_id)
    hostel_name = get_object_or_404(Hostel, pk = room.hostel_id).name
    if request.method == 'POST':
        try:
            # Handle form submission
            room.room_number = request.POST.get('room_number')
            room.description = request.POST.get('description')
            room.capacity = request.POST.get('capacity')
            room.rent = request.POST.get('rent')
            room.hostel_id = request.POST.get('hostel_id')
            room.save()
            messages.success(request, 'Room successfully updated!')
            return redirect('room_list')  # Redirect to the list of hostels
        except DatabaseError as e:
            # Handle database error
            return HttpResponse(f"An error occurred while saving the hostel: {e}", status=500)
        except Exception as e:
            # Handle any other exceptions
            return HttpResponse(f"An unexpected error occurred: {e}", status=500)
    else:
        
        context = {
            'room':room,
            'hostel_name':hostel_name,
            'hostels' : Hostel.objects.all()
        }
        return render(request, 'hostel_management/room_edit.html',context)

@login_required
def room_delete(request,room_id):
    room = get_object_or_404(Room, pk=room_id)
    if request.method == "POST":
        messages.success(request, 'Room successfully daleted!')
        room.delete()
        return redirect('room_list')
    
    return render(request, 'hostel_management/room_confirm_delete.html',{'room':room})


# def generate_pdf_view(request, customer_id):
#     customer = get_object_or_404(Customer, id=customer_id)
#     loans = Loan.objects.filter(customer=customer)
#     repayments = Repayment.objects.filter(loan__in=loans)

#     # Render the HTML template
#     html_content = render_to_string('customers/customer_summary.html', {
#         'customer': customer,
#         'loans': loans,
#         'repayments': repayments,
#     })

#     # Create a PDF from the HTML content
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename="customer_summary_{customer.id}.pdf"'
#     pisa_status = pisa.CreatePDF(html_content, dest=response)

#     if pisa_status.err:
#         return HttpResponse('Error generating PDF', status=500)

#     return response


