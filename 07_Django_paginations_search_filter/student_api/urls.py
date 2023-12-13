from django.urls import path, include

from .views import(
    #! function views
    # home, 
    # butun_ogrencileri_getir, 
    # yeni_ogreci_create_et, 
    # tek_ogrenciyi_goruntuleme_islemi, 
    # qorenciyi_guncelle, 
    # ogrenci_sil,
    
    #! class views

    #! APIVIEW
    StudentListCreate,
    StudentDetail,

    #? GenericApıView
    StudentGAV,
    StudentDetailGAV,

    # Concrete View
    StudentCV, 
    StudentDetail,
    
    )

urlpatterns = [
    #! function views
    # path("homesayfasinigetir/", home),
    # path("ogrecilerinhepsinigetir/", butun_ogrencileri_getir),
    # path("yeniogrenciolustur/", yeni_ogreci_create_et),
    # path("tekogrenci/<int:pk>/", tek_ogrenciyi_goruntuleme_islemi),
    # path("ogrencigüncelle/<int:pk>/", qorenciyi_guncelle),
    # path("ogrencisil/<int:pk>/", ogrenci_sil),

    #! class views
    #! APIVIEW
    # path("students/", StudentListCreate.as_view()),
    # path("students/<int:pk>/", StudentDetail.as_view()),

    #? GenericApıView
    # path("students/", StudentGAV.as_view()),
    # path("students/<int:pk>/", StudentDetailGAV.as_view()),

    path("students/", StudentCV.as_view())

]