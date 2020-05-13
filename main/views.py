from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from .models import *
from board.models import *


"""

Environment setup yapılıp localhost üzerinden websitesi'ne ulaşıldıktan sonra
sayfaların açılması için /admin panelinden Sayfas altında sayfa eklenmesi gerekmektedir.
Sayfaların sırası aşağıdaki gibi olmalıdır. Aksi takdirde Postların yerleri karışacaktır.

1 - Ana Sayfa
2 - Biz Kimiz Sayfası
3 - Misyon-Vizyon Sayfası
4 - Hakkımızda Sayfası
5 - Etkinliklerimiz Sayfası
6 - Etkinlik Detayı Sayfası
7 - İletişim Sayfası
8 - Kurul Sayfası
9 - Geçmiş Sayfası

"""


# Create your views here.
def main_view(request):
    main_images = KayanFotograf.objects.all()
    main_posts = Post.objects.filter(page=Sayfa.objects.all()[0]).order_by('query')
    main_bg = ArkaPlanFotograf.objects.get(page=Sayfa.objects.all()[0])
    main_dict = {
        "bg": main_bg,
        "posts": main_posts,
        "images": main_images,
        'oldyears': OldYear.objects.all().order_by("year")

    }
    return render(request, 'main.html', main_dict)


def about_view(request):
    biz_kimiz_post = Post.objects.filter(page=Sayfa.objects.all()[1]).order_by('query')
    misyon_vizyon_post = Post.objects.filter(page=Sayfa.objects.all()[2]).order_by('query')
    hakkimizda_bg = ArkaPlanFotograf.objects.get(page=Sayfa.objects.all()[3])
    urls = {
        "misyon_vizyon": "pieces/hakkimizda/misyon_vizyon.html",
        "biz_kimiz": "pieces/hakkimizda/biz_kimiz.html",
        "kurul": "pieces/hakkimizda/kurul.html"
    }
    hakkimizda_dict = {
        "urls": urls,
        "biz_kimizs": biz_kimiz_post,
        "misyon_vizyons": misyon_vizyon_post,
        "bg": hakkimizda_bg,
        'oldyears': OldYear.objects.all().order_by("year")
    }
    return render(request, 'hakkimizda.html', hakkimizda_dict)


def etkinlik_list_view(request):
    post = Post.objects.filter(page=Sayfa.objects.all()[4]).order_by('-date')
    etkinlik_bg = ArkaPlanFotograf.objects.get(page=Sayfa.objects.all()[4])

    # pagination
    paginator = Paginator(post, 3)
    sayfa = request.GET.get("sayfa")
    etkinlik_post = paginator.get_page(sayfa)

    etkinlik_dict = {
        "etks": etkinlik_post,
        "bg": etkinlik_bg,
        "etks_all": post,  # for archive
        'oldyears': OldYear.objects.all().order_by("year"),
    }
    return render(request, 'etkinliklerimiz.html', etkinlik_dict)


def etkinlik_detay_view(request, id):
    etkinlik = Post.objects.get(id=id)
    return render(request, 'etkinlik_detay.html', {"etk": etkinlik, 'oldyears': OldYear.objects.all().order_by("year")})


def iletisim_view(request):
    iletisim_bg = ArkaPlanFotograf.objects.get(page=Sayfa.objects.all()[5])
    return render(request, 'iletisim.html', {"bg": iletisim_bg, 'oldyears': OldYear.objects.all().order_by("year")})
