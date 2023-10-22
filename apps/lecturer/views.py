from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from .models import Lecture
from .forms import LectureForm
# Create your views here.

class CreateLectureView(CreateView):
    model = Lecture
    form_class = LectureForm
    template_name = 'dashboard/lecture/create_lecture.html'
    # success_url = reverse_lazy('category')
    # success_message = 'Category created successfully.'

    # def form_valid(self, form): 
    #     if Category.objects.filter(title__iexact = form.cleaned_data.get('title')):
    #         messages.error(self.request, "Category already present.")
    #         return super().form_invalid(form)
    #     return super().form_valid(form)