from django.contrib import admin
from builds.models import PCBuild

@admin.register(PCBuild)
class PCBuildAdmin(admin.ModelAdmin):
    ...
