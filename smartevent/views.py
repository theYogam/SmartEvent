
from django import forms
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from ikwen.core.models import Application

from smartevent.models import Event, Participant


class ParticipantForm(forms.ModelForm):
    """
    Participant form of an event
    """
    class Meta:
        model = Participant


class ViewEvent(TemplateView):
    template_name = 'smartevent/home.html'

    def get_context_data(self, **kwargs):
        context = super(ViewEvent, self).get_context_data(**kwargs)
        event = Event.objects.get(slug=kwargs['slug'])
        current_released_apps = ['daraja', 'foulassi', 'tsunami', 'pinsview']
        context['ikwen_apps'] = Application.objects.filter(slug__in=current_released_apps)
        context['event'] = event
        return context

    def post(self, request, *args, **kwargs):
        context = super(ViewEvent, self).get_context_data(**kwargs)
        event = Event.objects.get(slug=kwargs['slug'])
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            next_url = reverse('smartevent:view_event', args=(event.slug,))
            messages.success(request, "Thank you very much.")
            return HttpResponseRedirect(next_url, messages)
        else:
            context['form'] = form
            return render(request, self.template_name, context)
