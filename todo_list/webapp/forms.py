from django import forms
from django.forms import widgets
from .models import Type, Status, Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'types', 'status']

    summary = forms.CharField(max_length=50, required=True, label="Заголовок")
    description = forms.CharField(max_length=2000, required=False, label="Описание",
                                  widget=widgets.Textarea(attrs={"cols": 30, "rows": 5, "class": "test"}))
    types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), label="Типы", widget=forms.CheckboxSelectMultiple)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label="Статусы")
