from django.db import models

# Create your models here.


class Person(models.Model):
    isim = models.CharField(
        max_length=40,
        verbose_name="Yönetim kurulu üyesinin ismi:"
    )
    soyisim = models.CharField(
        max_length=40,
        verbose_name="Yönetim kurulu üyesinin soyismi:"
    )
    img = models.ImageField()

    class Meta:
        abstract = True
        ordering = ('isim', 'soyisim')

    def get_full_name(self):
        return self.isim + " " + self.soyisim

    def get_photo_url(self):
        if not self.img:
            return "default/photo.url"
        return self.img.url

    def __str__(self):
        return self.get_full_name()


class Member(Person):
    # A member is a Person.
    role = models.ForeignKey(
        'Role',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Yönetim kurulu üyesinin rolü:",
    )
    year = models.ForeignKey(
        'OldYear',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Yönetim kurulu üyesi hangi yıl görevdeydi."
    )


class Danisman(Person):
    unvan = models.CharField(
        max_length=25,
        verbose_name="Kulüp danışmanının ünvanı:"
    )
    year = models.ForeignKey(
        'OldYear',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Kulüp danışmanının aktif olduğu yıl:"
    )

    def get_unvan_full_name(self):
        return self.unvan + " " + self.isim + " " + self.soyisim


class OldYear(models.Model):
    year = models.SmallIntegerField(
        verbose_name="Yönetim kurulunun başlangıç yılı:"
    )

    def __str__(self):
        return str(self.year)

class Role(models.Model):
    role = models.CharField(
        max_length=20,
        verbose_name="Yönetim kurulundaki rol:"
    )

    def __str__(self):
        return self.role

