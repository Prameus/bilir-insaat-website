from django.db import models


class Reffrences(models.Model):
    # category_choices = [
    #     ["Yol ve Köprü İnşaatı", "Yol ve Köprü İnşaatı"],
    #     ["Binalar", "Binalar"],
    #     ["Bakım ve Onarım", "Bakım ve Onarım"],
    #     ["Tesisat İnşaatı", "Tesisat İnşaatı"],
    # ]

    baslik = models.CharField(
        max_length=150,
        null=False,
    )
    aciklama = models.TextField(max_length=400, null=True)
    # kategori = models.CharField(
    #     max_length=50, choices=category_choices, default="Yol ve Köprü İnşaatı"
    # )
    referans_fotografi_1 = models.ImageField(
        default="", upload_to=f"media/reference_images/", null=False, blank=True
    )
    referans_fotografi_2 = models.ImageField(
        default="", upload_to=f"media/reference_images/", null=False, blank=True
    )
    referans_fotografi_3 = models.ImageField(
        default="", upload_to=f"media/reference_images/", null=False, blank=True
    )
    referans_fotografi_4 = models.ImageField(
        default="", upload_to=f"media/reference_images/", null=False, blank=True
    )
    referans_fotografi_5 = models.ImageField(
        default="", upload_to=f"media/reference_images/", null=False, blank=True
    )
    referans_fotografi_6 = models.ImageField(
        default="", upload_to=f"media/reference_images/", null=False, blank=True
    )
    referans_fotografi_7 = models.ImageField(
        default="", upload_to=f"media/reference_images/", null=False, blank=True
    )
    referans_fotografi_8 = models.ImageField(
        default="", upload_to=f"media/reference_images/", null=False, blank=True
    )
    referans_fotografi_9 = models.ImageField(
        default="", upload_to=f"media/reference_images/", null=False, blank=True
    )
    referans_fotografi_10 = models.ImageField(
        default="", upload_to=f"media/reference_images/", null=False, blank=True
    )
    date = models.DateField(auto_now=False, auto_now_add=True, null=False)

    class Meta:
        verbose_name = "Referans Yonetimi"
        verbose_name_plural = "Referans Yonetimi"

    def __str__(self):
        return self.baslik
