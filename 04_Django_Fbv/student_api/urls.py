from django.urls import path, include

from .views import home, butun_ogrencileri_getir,yeni_ogrenci_create_et,tek_ogrenciyi_goruntuleme_islemi,ogrenciyi_guncelleme ,ogrenci_sil


urlpatterns = [
    path("homesayfasinigetir/", home),
    path("ogrencilerinhepsinigetir/", butun_ogrencileri_getir),
    path("yeniogrenciolustur/",yeni_ogrenci_create_et),
    path("tekogrenci/<int:pk>/", tek_ogrenciyi_goruntuleme_islemi),
    path("ogrenciyiguncelle/<int:pk>/", ogrenciyi_guncelleme),
    path("ogrencisil/<int:pk>/", ogrenci_sil)

]