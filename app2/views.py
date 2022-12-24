from django.shortcuts import render
from .forms import FeedbackForm
from django.views.generic.edit import FormView
from django.http import HttpResponse

class FeedbackEmailView(FormView):
    template_name = 'feedback.html'
    form_class = FeedbackForm

    def form_valid(self, form):
        form.send_email()
        msg = 'Your response has been recorded'
        return HttpResponse(msg)
        