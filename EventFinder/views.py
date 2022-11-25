from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views import generic
from django.core.mail import send_mail
from django.urls import reverse_lazy
from CreateEvent.models import BasicInfo
from EventFinder.models import Register
# from braces.views import SelectRelatedMixin

# Create your views here.

class EventFinder(generic.ListView):
    model = BasicInfo
    paginate_by = 10 #if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
    template_name = 'eventfinder/finder.html'

class EventDetail(generic.DetailView):
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

class RegistrationPage(generic.CreateView):
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



