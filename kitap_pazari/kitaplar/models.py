from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.

class Kitap(models.Model):
    isim = models.CharField(max_length=100)
    yazar = models.CharField(max_length=100)
    aciklama = models.TextField(blank=True, null=True)

    yaratilma_tarihi = models.DateTimeField(auto_now_add=True) ## auto_now_add=True yaratilma tarihi olur ve degistirilemez
    guncellenme_tarihi = models.DateTimeField(auto_now=True) ## auto_now=True her guncelleme yapildiktan sonra degisir.
    yayin_tarihi = models.DateTimeField()

    def __str__(self):
        return f'{self.isim}-{self.yazar}'

class Yorum(models.Model):
    kitap = models.ForeignKey(Kitap, on_delete=models.CASCADE , related_name= 'yorumlar')
    
    #yorum_sahibi = models.CharField(max_length=225)
    
    #Yorum sahibini djangoda otomatik gelen User classiyla bagliyoruz    
    yorum_sahibi = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'kullanici_yorumlari')
     
    yorum = models.TextField(blank=True, null=True)

    yaratilma_tarihi = models.DateTimeField(auto_now_add=True)
    guncellenme_tarihi = models.DateTimeField(auto_now=True)

    degerlendirme = models.PositiveIntegerField(
        # Validatora asagidaki classlari vererek aralik belirledik.
        validators = [MinValueValidator(1),MaxValueValidator(5)],
    )

    def __str__(self):
        return str(self.degerlendirme)