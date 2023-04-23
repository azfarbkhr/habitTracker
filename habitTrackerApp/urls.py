from django.urls import path
from . import views

urlpatterns = [
    path('habit/', views.HabitListView.as_view(), name='habit_list'),
    path('habit/create/', views.HabitCreateView.as_view(), name='habit_create'),
    path('habit/<int:pk>/update/', views.HabitUpdateView.as_view(), name='habit_update'),
    path('target/', views.TargetListView.as_view(), name='target_list'),
    path('target/create/', views.TargetCreateView.as_view(), name='target_create'),
    path('target/<int:pk>/update/', views.TargetUpdateView.as_view(), name='target_update'),
    path('habitlog/', views.HabitLogListView.as_view(), name='habit_log_list'),
    path('habitlog/create/', views.HabitLogCreateView.as_view(), name='habit_log_create'),
    path('habitlog/<int:pk>/update/', views.HabitLogUpdateView.as_view(), name='habit_log_update'),
]
