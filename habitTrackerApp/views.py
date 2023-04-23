from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Habit, Target, HabitLog
from .forms import HabitForm, TargetForm, HabitLogForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from . import mixins as HbtMixins


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'habitTrackerApp/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid

class HabitListView(HbtMixins.ListView):
    model = Habit
    
class HabitCreateView(HbtMixins.CreateView):
    model = Habit
    form_class = HabitForm
    
class HabitUpdateView(HbtMixins.UpdateView):
    model = Habit
    form_class = HabitForm

class TargetListView(HbtMixins.ListView):
    model = Target

class TargetCreateView(HbtMixins.CreateView):
    model = Target
    form_class = TargetForm

class TargetUpdateView(HbtMixins.UpdateView):
    model = Target
    form_class = TargetForm
    
class HabitLogListView(HbtMixins.ListView):
    model = HabitLog

class HabitLogCreateView(HbtMixins.CreateView):
    model = HabitLog
    form_class = HabitLogForm


class HabitLogUpdateView(HbtMixins.UpdateView):
    model = HabitLog
    form_class = HabitLogForm