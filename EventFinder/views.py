from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic
from django.views.generic import TemplateView
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from . import models
from CreateEvent.models import BasicInfo
from EventFinder.models import Register
from django.http import HttpResponse
from braces.views import SelectRelatedMixin
from django.http import Http404

# Create your views here.

class EventFinder(generic.ListView, SelectRelatedMixin):
    model = BasicInfo
    paginate_by = 10 #if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
    template_name = 'eventfinder/finder.html'

class EventDetail(generic.DetailView, SelectRelatedMixin):
    model = BasicInfo

    # queryset = models.EventFinder.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    # def get_object(self, query_set):
    #     event = get_object_or_404(EventFinder, pk=self.kwargs['pk'])
    #     return event

    template_name = 'eventfinder/eventdetail.html'

class RegistrationPage(generic.CreateView, SelectRelatedMixin):
    fields = ("first_name","last_name", "phone_number","email_address")
    model = Register

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event_id'] = self.kwargs['event_id']
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # self.object.user = self.request.user
        self.object.event = get_object_or_404(BasicInfo, pk=self.kwargs['event_id'])
        self.object.save()
        self.sendmail(form)
        return super().form_valid(form)
    success_url =reverse_lazy('thanksreg')
    template_name ='eventfinder/register.html'
    def sendmail(self, form):
        # template = render_to_string('eventfinder/email_template.html', {'name': request.user.profile.first_name})
        send_mail(
            'subject here',
            'Hey! Thanks for registering for this event. Hope to see you there!',
            'woleoyediran25@gmail.com',
            ['woleoyediran@gmail.com'],
            fail_silently=False,
        )



