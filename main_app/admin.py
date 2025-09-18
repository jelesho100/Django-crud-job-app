from django.contrib import admin
from .models import Application, Interaction, Tag

admin.site.register(Application)
admin.site.register(Interaction)
admin.site.register(Tag)

