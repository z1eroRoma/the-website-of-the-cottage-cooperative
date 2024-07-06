from django.contrib import admin
from .models import Member, Plot, Transaction, Event, Resource

admin.site.register(Member)
admin.site.register(Plot)
admin.site.register(Transaction)
admin.site.register(Event)
admin.site.register(Resource)
