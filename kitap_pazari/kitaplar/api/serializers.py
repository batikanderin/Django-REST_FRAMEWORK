from rest_framework import serializers 
from kitaplar.models import Kitap,Yorum

class YorumSerializer(serializers.ModelSerializer):
    # Kitap classi icin serializer olusturmak icin bu kodlari yaziyoruz
    # Fields kismi alanlari gosteriyor.
    yorum_sahibi = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Yorum
        # fields = '__all__'
        # Yeni bir yorum eklerden hangi kitaba yorum yapmak istedigimizi belirtmemize gerek yok cunku zaten pk ile kitabi aliyoruz.
        exclude = ['kitap']





class KitapSerializer(serializers.ModelSerializer):    
    yorumlar = YorumSerializer(many=True,read_only=True)

    # Kitaplardaki yorumlar kismini yorum serializerdan aliyoruz
    # Databaseden kitaplari getirdigimizde, kitaplara yapilan yorumlari da getirir.
    # many=True diyerek ben sana birden cok bilgi gondeceregim bilgisini dataya verir.
    # read_only ile yeni bir kitap datasi olustururken, yorum bilgisi istemez.Mantik olarak kitap olustururken yorumu bilemeyiz.
    class Meta:
        model = Kitap
        fields = '__all__'

