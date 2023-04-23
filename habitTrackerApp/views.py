from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Habit, Target, HabitLog
from .forms import HabitForm, TargetForm, HabitLogForm, TargetSelectionForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.db.models import Sum
from django.utils import timezone
import datetime

import random
from django.shortcuts import get_object_or_404, redirect

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

class HomePageView(LoginRequiredMixin, generic.TemplateView):
    template_name = "habitTrackerApp/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        target_form = TargetSelectionForm(user=self.request.user)
        context['target_form'] = target_form

        target_id = self.request.GET.get('target')
        if target_id:
            target_form.fields['target'].initial = target_id
            target = Target.objects.get(id=target_id, user=self.request.user)
            context['target'] = target

            # Get the habit logs and aggregate data
            habit_logs = HabitLog.objects.filter(
                habit__target=target,
                date__gte=target.start_date,
                date__lte=target.end_date
            ).values('date').annotate(total_quantity=Sum('quantity')).order_by('date')

            days_count_from_start_to_end = (target.end_date - target.start_date).days + 1
            days_count_from_today_to_end = (target.end_date.date() - timezone.localdate()).days + 1            
            cumsum = 0
            target_expected_quantity = target.quantity / days_count_from_start_to_end

            filled_habit_logs = []
            for date in target.date_range():
                log_for_date = next((log for log in habit_logs if log['date'] == date), None)
                
                if not log_for_date:
                    log_for_date = {'date': date, 'total_quantity': 0}
                
                cumsum += log_for_date['total_quantity']

                log_for_date['habit_logs_quantity_cumsum'] = cumsum
                log_for_date['target_expected_quantity_cumsum'] = round(target_expected_quantity * (date - target.start_date).days, 0)

                filled_habit_logs.append(log_for_date)


            sum_habit_logs = sum(log['total_quantity'] for log in filled_habit_logs) or 0 

            context['habit_logs'] = filled_habit_logs
            context['target_quantity'] = target.quantity
            context['current_rate'] = round(sum_habit_logs / days_count_from_start_to_end, 2)
            context['required_rate'] = round((target.quantity - sum_habit_logs) / days_count_from_today_to_end, 2)
            context['target_achieved_percent'] = int(round(sum_habit_logs / target.quantity * 100, 2))
            
            context['unit_habit_logs'] = target.habit.unit

        return context

class InsertDummyDataView(LoginRequiredMixin, generic.View):

    def get(self, request, *args, **kwargs):
        target_id = kwargs.get('target_id')
        habit_id = kwargs.get('habit_id')

        target = get_object_or_404(Target, id=target_id, user=request.user)
        habit = get_object_or_404(Habit, id=habit_id, user=request.user)
        
        # Insert dummy data
        for date in target.date_range():
            for _ in range(random.randint(1, 3)):  # Insert 1 to 3 rows per date
                quantity = random.randint(1, 10)  # Random quantity between 1 and 10
                HabitLog.objects.create(habit=habit, date=date, quantity=quantity, user=request.user)

        messages.success(request, f"Dummy data inserted for {habit.name} between {target.start_date} and {target.end_date}")

        return redirect('home')