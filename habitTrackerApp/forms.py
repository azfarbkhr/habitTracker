from django import forms
from .models import Habit, Target, HabitLog

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'category', 'unit']

class TargetForm(forms.ModelForm):
    class Meta:
        model = Target
        fields = ['habit', 'title', 'quantity', 'start_date', 'end_date']

class HabitLogForm(forms.ModelForm):
    class Meta:
        model = HabitLog
        fields = ['habit', 'date', 'quantity']
