from django.contrib import admin
from .models import *

# Register your models here.

class adminSlider(admin.ModelAdmin):
    list_display = ["title"]

    class Meta:
        model = KayanFotograf

admin.site.register(KayanFotograf, adminSlider)


class adminPost(admin.ModelAdmin):
    list_display = ["title", "text", "date"]

    class Meta:
        model = Post

admin.site.register(Post, adminPost)

class adminBG(admin.ModelAdmin):
    list_display = ["page"]

    class Meta:
        model = ArkaPlanFotograf

admin.site.register(ArkaPlanFotograf, adminBG)

class adminPage(admin.ModelAdmin):
    list_display = ["page_name"]

    class Meta:
        model = Sayfa

admin.site.register(Sayfa, adminPage)