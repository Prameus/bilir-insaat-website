from django.db import models


class Reffrences(models.Model):
    category_choices = [
        ["Yol ve Köprü İnşaatı", "Yol ve Köprü İnşaatı"],
        ["Binalar", "Binalar"],
        ["Bakım ve Onarım", "Bakım ve Onarım"],
        ["Tesisat İnşaatı", "Tesisat İnşaatı"]
    ]

    baslik = models.CharField(max_length=150)
    aciklama = models.TextField()
    kategori = models.CharField(
        max_length=50, choices=category_choices, default="Yol ve Köprü İnşaatı")
    referans_fotografi = models.ImageField(
        upload_to="media/reference_images/")
    date = models.DateField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = "Referans Yonetimi"
        verbose_name_plural = "Referans Yonetimi"

    def __str__(self):
        return self.baslik
