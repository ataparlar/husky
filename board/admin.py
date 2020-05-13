from django.contrib import admin
from .models import *

# Register your models here.

class adminMember(admin.ModelAdmin):
    list_display = ["isim", "soyisim", "year"]

    class Meta:
        model = Member

admin.site.register(Member, adminMember)


class adminDanisman(admin.ModelAdmin):
    list_display = ["isim", "soyisim", "year"]

    class Meta:
        model = Danisman

admin.site.register(Danisman, adminDanisman)


class adminRole(admin.ModelAdmin):
    list_display = ["role"]

    class Meta:
        model = Role

admin.site.register(Role, adminRole)


class adminYear(admin.ModelAdmin):
    list_display = ["year"]

    class Meta:
        model = OldYear

admin.site.register(OldYear, adminYear)
