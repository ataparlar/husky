Artık kamera kalibrasyon dosyamız var bu sebeple gerekli json dosyamızı kodunuz ile aynı klasörde bulundurmanız gereklidir
eğer değilse kod içinde params içindeki configFilePath adlı parametreyi ayarlamalısınız

Aşağıdaki duyuru kodun üst kısmında da vardır, lakin buraya koymakta da yarar olduğunu düşünüyorum
"""
KODA BAKMADAN ÖNCE

Yeşil ile gösterilenler adaylardır 
Mavi ile gösterilenler ise onaylanmış adaylardır(markers)                                                                                                            
Bu kod 5x5 lik kodları algılamak için tasarlanmıştır tags isimli sınıfta "valids" isimli listede
kabul edilen her artag'in iç kodları tanımlanmışır. İsterseniz yeni kodlar ekleyebilirsiniz.

*PARAMETRELER
params klasörü hemen hemen bütün parametrelerin depolandığı yerdir

-threshConstant: eşiklemenin hassasiyeti ile oynar ne kadar düşük o kadar hassaslaşır
-threshWinSize: parametleri ile oynanabilir ama tek sayı olmasına dikkat ediniz
-minAreaRate: belirlenen adayların sahip olması gereken en küçük alanın hesaplanmasında kullanılır
              bunu azaltmanız daha küçük adaylar görmenizi sağlar
-maxAreaRate: minAreaRate parametresine benzer ama ters etkiye neden olur
-resizeRate: bu parammetrenin artırılması belli bir noktaya kadar algoritma kesinliğini arttırır lakin 
             işlem gücü harcamasına neden olur
-cellMarginRate: her bite bakarken onun tamamına değil de biraz daha içine bakarız. Bu parametre her hücrenin 
                 yüzde kaç içine bakmamız gerekiğini belirler
-markerSizeInBits & borderSizeInBits: Artag'in sınırlarının ve iç kodunun bit boyutu yazılmıştır lakin bunun
                                      değiştirilmesi tavsiye edinilmez çünkü tanımlı bütün artaglar bu iki 
                                      parametreye göre tanımlı.
-configFilePath: kamera kalibrasyon dosyasının bulunduğu konum(eğer aynı klasörde ise ismi yetiyor
-undistortImg: kamera kalibrasyonu hala deneme aşamasında oluğu için isterseniz undistortion işlemini engelleyebilirsiniz
-showCandidate showMarkers: showTresholded bu üçü isminden de anlaşıacağı üzere istediğiniz şeyleri kapatıp açabilirsiniz

"""

kullanılan paketler: json - opencv - numpy
