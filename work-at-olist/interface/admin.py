from django.contrib import admin
from .models import Category
from .models import Channel

admin.site.register(Channel)
admin.site.register(Category)
