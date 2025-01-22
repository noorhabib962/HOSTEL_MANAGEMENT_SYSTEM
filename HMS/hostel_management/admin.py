from django.contrib import admin
from .models import Hostel, Room
from django.utils.html import format_html

class RoomInline(admin.TabularInline):  
    model = Room 
    extra = 1 

class HostelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    inlines = [RoomInline]
    ordering = ['id']

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'description','capacity', 'total_students', 'status')
    list_filter = ['room_number']
    ordering = ['id']
    @admin.display(description='Status') 
    def status(self, obj):
        count = obj.students.count() 
        flag = ''
        if count == obj.capacity: 
            flag = 'Full'
            color = 'red' 
        else:
            flag = 'Not Full' 
            color = 'green' 
        return format_html('<b style="color: {};">{}</span>', color, flag)
        
admin.site.register(Hostel, HostelAdmin)
admin.site.register(Room, RoomAdmin)
