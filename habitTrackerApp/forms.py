from django import forms
from .models import Habit, Target, HabitLog
from django.db.models import ForeignKey
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Row, Column, HTML, Div, MultiField


class HbtModelForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))


class HabitForm(HbtModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'category', 'unit']

class TargetForm(HbtModelForm):
    class Meta:
        model = Target
        fields = ['habit', 'title', 'quantity', 'start_date', 'end_date']

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields['habit'].queryset = Habit.objects.filter(user=user)

class HabitLogForm(HbtModelForm):
    class Meta:
        model = HabitLog
        fields = ['habit', 'date', 'quantity']

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields['habit'].queryset = Habit.objects.filter(user=user)

class TargetSelectionForm(forms.Form):
    target = forms.ModelChoiceField(
        queryset=Target.objects.none(),
        label='Select Target',
        required=True
    )

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields['target'].queryset = Target.objects.filter(user=user)