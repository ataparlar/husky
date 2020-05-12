from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    title = models.CharField(
        max_length=120,
        verbose_name="Post Başlığı:"
    )
    """text = models.TextField(
        verbose_name="Post Metni:"
    )"""
    query = models.SmallIntegerField(
        verbose_name="Post Sırası:",
        default=1,
    )
    text = RichTextField(
        verbose_name="Post Metni:"
    )
    img = models.ImageField(
        blank=True,
        null=True,
        verbose_name="Post Fotoğrafı:"
    )
    width = models.SmallIntegerField(
        verbose_name="Görselin genişliği. Piksel biriminde.",
        blank=True,
        null=True,
    )
    date = models.DateField(
        blank=True,
        null=True
    )
    small_text = models.TextField(
        blank=True,
        null=True,
        verbose_name="Çarpıcı yazı. Eklenirse sol tarafta ayrı blok olarak gözükür."
    )
    page = models.ForeignKey(
        "Sayfa",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Bu post, hangi sayfada yer alacak?",
    )

    def __str__(self):
        return self.title


class KayanFotograf(models.Model):
    title = models.CharField(
        max_length=120,
        verbose_name="Kayan Fotoğraf İsmi"
    )
    img = models.ImageField(
        verbose_name="Kayan Fotoğraf"
    )
    query = models.SmallIntegerField(
        blank=False,
        null=False,
        default=0,
        verbose_name="Kayan Fotoğraf Sırası"
    )

    def __str__(self):
        return self.title


class ArkaPlanFotograf(models.Model):
    bg_name = RichTextField(
        max_length=120,
        verbose_name="Arka planın önünde yazacak yazı:",
        default="a"
    )
    img = models.ImageField(
        verbose_name="Sayfanın arka plan fotoğrafı."
    )
    page = models.ForeignKey(
        "Sayfa",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Bu fotoğraf, hangi sayfada yer alacak?",
    )

    def __str__(self):
        return self.bg_name


class Sayfa(models.Model):
    page_name = models.CharField\
        (max_length=120,
         verbose_name="Sayfa adı"
         )
    atomic = False

    def __str__(self):
        return self.page_name