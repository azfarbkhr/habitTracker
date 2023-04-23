from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('habit/', views.HabitListView.as_view(), name='habit_list'),
    path('habit/create/', views.HabitCreateView.as_view(), name='habit_create'),
    path('habit/<int:pk>/update/', views.HabitUpdateView.as_view(), name='habit_update'),
    path('target/', views.TargetListView.as_view(), name='target_list'),
    path('target/create/', views.TargetCreateView.as_view(), name='target_create'),
    path('target/<int:pk>/update/', views.TargetUpdateView.as_view(), name='target_update'),
    path('habitlog/', views.HabitLogListView.as_view(), name='habit_log_list'),
    path('habitlog/create/', views.HabitLogCreateView.as_view(), name='habit_log_create'),
    path('habitlog/<int:pk>/update/', views.HabitLogUpdateView.as_view(), name='habit_log_update'),
    path('login/', auth_views.LoginView.as_view(template_name='habitTrackerApp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('insert_dummy_data/<int:target_id>/<int:habit_id>/', views.InsertDummyDataView.as_view(), name='insert_dummy_data'),

]
