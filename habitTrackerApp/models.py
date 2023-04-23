from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Habit(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta: 
        verbose_name_plural = "Habits"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('habit_update', kwargs={'pk': self.pk})

class Target(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    start_date = models.DateTimeField(default = timezone.now)
    end_date = models.DateTimeField(default = timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('target_update', kwargs={'pk': self.pk})

class HabitLog(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateTimeField(default = timezone.now)
    quantity = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.habit.name + " " + self.date.strftime("%m/%d/%Y")
    
    def get_absolute_url(self):
        return reverse('habit_log_update', kwargs={'pk': self.pk}) 
