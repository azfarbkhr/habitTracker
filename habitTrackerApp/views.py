from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Habit, Target, HabitLog
from .forms import HabitForm, TargetForm, HabitLogForm

class HabitListView(generic.ListView):
    model = Habit

class HabitCreateView(generic.CreateView):
    model = Habit
    form_class = HabitForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Habit created successfully.')
        return super().form_valid(form)
    
class HabitUpdateView(generic.UpdateView):
    model = Habit
    form_class = HabitForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Habit updated successfully.')
        return super().form_valid(form)    

class TargetListView(generic.ListView):
    model = Target

class TargetCreateView(generic.CreateView):
    model = Target
    form_class = TargetForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Target created successfully.')
        return super().form_valid(form)      

class TargetUpdateView(generic.UpdateView):
    model = Target
    form_class = TargetForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Target updated successfully.')
        return super().form_valid(form)  
    
class HabitLogListView(generic.ListView):
    model = HabitLog

class HabitLogCreateView(generic.CreateView):
    model = HabitLog
    form_class = HabitLogForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Habit Log created successfully.')
        return super().form_valid(form)  


class HabitLogUpdateView(generic.UpdateView):
    model = HabitLog
    form_class = HabitLogForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Habit Log updated successfully.')
        return super().form_valid(form)      
