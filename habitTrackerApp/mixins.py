from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

class UserObjectPermissionsMixin:
    """
    A mixin that ensures the current user has permission to access the object.
    """

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.user != request.user:
            raise PermissionDenied("You do not have permission to access this object.")

        return super().dispatch(request, *args, **kwargs)
    

class CreateView(LoginRequiredMixin, generic.CreateView):

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Record created successfully.')
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class UpdateView(LoginRequiredMixin, UserObjectPermissionsMixin, generic.UpdateView):
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Record updated successfully.')
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

                    
class ListView(LoginRequiredMixin, generic.ListView):
    
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)            
