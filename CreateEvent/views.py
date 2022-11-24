from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from . import models
from . import forms


# Create your views here.
class CreateEvent(generic.CreateView, LoginRequiredMixin):
    fields = ("name", "organizer", "venue", "date", "type","category","image", "summary","details")
    model =models.BasicInfo

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
    # form_class =forms.BasicInfoForm
    success_url =reverse_lazy('CreateEvent:addticket')
    template_name ='CE_detail.html'



class AddTickets(generic.CreateView, LoginRequiredMixin):
    fields = ("General_admission", "Available_Quantity","price",)
    model=models.AddTickets

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    success_url = reverse_lazy('appreciate')
    template_name = 'tickets.html'

class Dashboard(generic.DetailView, LoginRequiredMixin):
    pass




# Username: Wholes
# password: testpassword