from django.db import models

class Reffrences(models.Model):
    baslik = models.CharField(max_length=150)
    aciklama = models.TextField()
    referans_fotografi = models.ImageField(upload_to="reference_images/% Y/% m/% d/")
    date = models.DateField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.title