# from rest_framework.generics import GenericAPIView
# ## Listelemek ve yaratmak icin 2 tane mixine ihtiyacimiz var.
# from rest_framework.mixins import ListModelMixin,CreateModelMixin

from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from kitaplar.api.permissions import IsAdminUserorReadOnly,IsYorumSahibiOrReadOnly
from kitaplar.api.serializers import KitapSerializer,YorumSerializer
from kitaplar.models import Kitap,Yorum
from rest_framework.exceptions import ValidationError

## List Create View sayesinde tum bilgileri api olarak listelemek icin sadece asagidaki islemleri yapariz.
class KitapListCreateAPIView(generics.ListCreateAPIView):
    queryset = Kitap.objects.all()    
    serializer_class = KitapSerializer
    permission_classes = [IsAdminUserorReadOnly]



## RetrieveDestroyAPIView sayesinde apideki her bir elemanin bilgerini bu sekilde alabiliriz.Urlye pk vermeyi unutma!!
class KitapDetailAPIViews(generics.RetrieveDestroyAPIView):
    queryset = Kitap.objects.all()    
    serializer_class = KitapSerializer
    permission_classes = [IsAdminUserorReadOnly]


 
class YorumCreateAPIViews(generics.CreateAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def perform_create(self,serializer):
        
        #Kitap icin pkyi aliyoruz
        kitap_pk = self.kwargs.get('kitap_pk')

        # Kitap icin aldigimiz pknin var olup olmadigini kontrol etmek icin
        kitap = get_object_or_404(Kitap, pk=kitap_pk)
        kullanici=self.request.user
        #yorumlar ile yorum datasindaki bilgileri filtreleyerek boyle bir kitap ve kullanici var olup olmadigina bakariz.

        yorumlar = Yorum.objects.filter(kitap = kitap,yorum_sahibi=kullanici)
        # Bu sorgu ile eger yorum varsa 1 kullanicini daha fazla yorum yapmasini engelleriz
        if yorumlar.exists():
            raise ValidationError('Bir kitaba sadece bir yorum yapabilirsiniz')
        
        #Eger yorum yoksa asagidaki komutu calistirir ve ilgili kitap ve kullanici sahibi yorumu yapar.
        serializer.save(kitap=kitap,yorum_sahibi=kullanici)
        

class YorumDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer
    permission_classes = [IsYorumSahibiOrReadOnly]
    





# #ListModelMixini ve CreateModelMixini classimiza verdik
# class KitapListCreateAPIView(ListModelMixin,CreateModelMixin,GenericAPIView):
#     queryset = Kitap.objects.all()    
#     serializer_class = KitapSerializer
#     ## serializer_class kismina kitap serializeri veriyoruz.
    
#     # Kitaplari Listelemek
#     def get(self,request,*args, **kwargs):
#         # ListModelMixindeki tanima gore self,listi cagirip asagidaki parametleri verdigimizde bizim icin tum islemleri yapar. args ve kwargsi get methodund tanit.
#         return self.list(request, *args, **kwargs)

#     # Yeni kitap yaratabilmek
#     def post(self,request,*args, **kwargs):
#         return  self.create(request, *args, **kwargs)