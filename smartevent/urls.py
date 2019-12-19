from django.conf.urls import url, patterns
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

from smartevent.views import ViewEvent

urlpatterns = patterns(
    '',
    url(r'^(?P<slug>[-\w]+)/$', ViewEvent.as_view(), name='view_event'),
)

