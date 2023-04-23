from django.contrib import admin
from .models import Habit, Target, HabitLog

admin.site.register(Habit, 
    list_display=['name', 'category', 'unit', 'user'],
    list_filter=['category', 'user'],
)

admin.site.register(Target,
    list_display=['habit', 'title', 'quantity', 'start_date', 'end_date', 'user'],
    list_filter=['habit', 'start_date', 'end_date', 'user'],        
)

admin.site.register(HabitLog, 
    list_display=['habit', 'date', 'quantity', 'user'],
    list_filter=['habit', 'user'],
)