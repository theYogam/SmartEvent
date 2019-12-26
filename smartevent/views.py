import json
from threading import Thread

from django import forms
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _, get_language, activate

# Create your views here.
from django.views.generic import TemplateView

from ikwen.core.models import Application
from ikwen.core.utils import get_model_admin_instance, get_service_instance, get_item_list, get_model, get_mail_content, \
    XEmailMessage, logger

from daraja.models import Dara
from smartevent.models import Event, Participant

ADMIN_EMAIL = 'silatchomsiaka@gmail.com'


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


def thankyou(request, *args, **kwargs):

    cta_url = 'https://blog.ikwen.com/des-reseaux-sociaux-a-daraja/'
    dara_list = Dara.objects.all()
    participant_list = Participant.objects.all()
    dara_email_list = []

    sender = 'ikwen Daraja <no-reply@ikwen.com>'

    for dara in dara_list:
        dara_lang = dara.member.language
        activate(dara_lang)

        if dara_lang == 'en':
            cta_url = 'https://blog.ikwen.com/from-social-network-to-daraja/'

        dara_name = dara.member.first_name
        dara_email = dara.member.email
        subject = _("Start making money now !")
        html_content = get_mail_content(subject, template_name='smartevent/mails/thank-you.html',
                                        extra_context={'dara_name': dara_name,
                                                       'cta_url': cta_url})
        msg = EmailMessage(subject, html_content, sender, [dara_email])
        msg.content_subtype = "html"
        msg.extra_headers = {'Reply-To': 'contact@ikwen.com'}
        Thread(target=lambda m: m.send(), args=(msg,)).start()
        dara_email_list.append(dara_email)

    for participant in participant_list:
        if participant.email in dara_email_list:
            continue
        lang = 'fr'
        activate(lang)
        dara_name = participant.first_name
        dara_email = participant.email
        subject = _("Start making money now !")
        html_content = get_mail_content(subject, template_name='smartevent/mails/thank-you.html',
                                        extra_context={'dara_name': dara_name,
                                                       'cta_url': cta_url,
                                                       })
        msg = EmailMessage(subject, html_content, sender, [dara_email])
        msg.content_subtype = "html"
        Thread(target=lambda m: m.send(), args=(msg,)).start()

    response = {"success": True}
    return HttpResponse(json.dumps(response), 'content-type: text/json')

    # dara_list = [{'email': 'silatchomsiaka@gmail.com', 'name': 'Silatchom'},
    #              {'email': 'rsihon@gmail.com', 'name': 'Sihon'},
    #              {'email': 'wilfriedwillend@gmail.com', 'name': 'Wilfried'},
    #              {'email': 'cedricfotso1@gmail.com', 'name': 'Cedric'}]
    #
    # for dara in dara_list:
    #     lang = 'fr'
    #     activate(lang)
    #     dara_name = dara.get('name')
    #     dara_email = dara.get('email')
    #     subject = _("Start making money now !")
    #     html_content = get_mail_content(subject, template_name='smartevent/mails/thank-you.html',
    #                                     extra_context={'dara_name': dara_name,
    #                                                    'cta_url': cta_url,
    #                                                    })
    #     msg = EmailMessage(subject, html_content, sender, [dara_email])
    #     msg.content_subtype = "html"
    #     msg.extra_headers = {'Reply-To': 'contact@ikwen.com'}
    #     Thread(target=lambda m: m.send(), args=(msg,)).start()
    #
    # response = {"success": True}
    # return HttpResponse(json.dumps(response), 'content-type: text/json')


