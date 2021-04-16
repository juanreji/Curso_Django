# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Registrado

class AdminRegistrado(admin.ModelAdmin):
	list_display = ["__unicode___", "nombre", "timestamp"]
	class Meta:
		model = Registrado

admin.site.register(Registrado)
