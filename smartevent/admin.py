from django.contrib import admin

from smartevent.models import Event, Participant


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    fields = ('title', 'slug', 'start_time', 'end_time',)
    prepopulated_fields = {"slug": ("title",)}


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'occupation', 'opinion',)
    fields = ('first_name', 'last_name', 'email', 'phone', 'occupation', 'opinion',)
    # prepopulated_fields = {"slug": ("title",)}


admin.site.register(Event, EventAdmin)
admin.site.register(Participant, ParticipantAdmin)
