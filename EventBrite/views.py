from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class TestPage(TemplateView):
    template_name = 'test.html'

class FindPage(TemplateView):
    template_name = 'findticket.html'

class HelpPage(TemplateView):
    template_name = 'help.html'

class AppreciationPage(TemplateView):
    template_name = 'createappreciation.html'

class ThanksRegistration(TemplateView):
    template_name = 'thanksreg.html'
