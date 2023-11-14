from django import forms
from .models import Lecture

class LectureForm(forms.ModelForm):
    title = forms.CharField(label='Lecture title:', max_length = 101),
    start_date = forms.DateTimeField(label='Start date:', widget=forms.DateInput(attrs={'type': 'date'}))
    start_time = forms.TimeField(label='Start time:', widget=forms.DateInput(attrs={'type': 'time'}))
    end_date = forms.DateTimeField(label='End date:', widget=forms.DateInput(attrs={'type': 'date'}))
    end_time = forms.TimeField(label='End time:', widget=forms.DateInput(attrs={'type': 'time'}))

    class Meta:
        model = Lecture
        fields = ['title', 'start_date', 'start_time', 'end_date', 'end_time', 'course', 'classroom']


class MarkAttendanceForm(forms.ModelForm):

    class Meta:
        model = Lecture
        fields = []