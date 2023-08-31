# İlk olarak, "PIL" kütüphanesinden "Image" ve "ImageDraw" sınıflarını içe aktarıyoruz.
# Bu sınıflar resim oluşturma ve çizim işlemleri için kullanılacaktır.
from PIL import Image, ImageDraw

# "width" ve "height" değişkenleri ile oluşturulacak GIF'in genişlik ve yüksekliğini belirliyoruz.
# Ardından "background_color" değişkeniyle arka plan rengini belirliyoruz.
width, height = 300, 300
background_color = (255, 255, 255)  # Beyaz

# "frames" adında boş bir liste oluşturuyoruz.
# Bu liste, her bir karenin temsil edildiği resim nesnelerini içerecektir
frames = []
for i in range(10):
    #  Bir döngü içinde 10 kare oluşturuyoruz. Her bir karede:
    # Image.new("RGB", (width, height), background_color) kodu ile belirttiğimiz boyutlarda ve arka plan renginde yeni bir resim nesnesi oluşturuyoruz.
    image = Image.new("RGB", (width, height), background_color)

    # ImageDraw.Draw(image) ile resim üzerinde çizim yapmak için bir ImageDraw nesnesi oluşturuyoruz.
    draw = ImageDraw.Draw(image)

    # draw.rectangle(shape_box, outline=(0, 0, 0)) kodu ile her bir karede bir dikdörtgen çiziyoruz. shape_box değişkeni, dikdörtgenin koordinatlarını belirtir.
    shape_box = (i * 10, i * 10, width - i * 10, height - i * 10)
    draw.rectangle(shape_box, outline=(0, 0, 0))

    # Her bir kareyi frames listesine ekliyoruz.
    # Bu, her bir kareyi birer resim nesnesi olarak saklamamıza yardımcı olacak.
    frames.append(image)

# Son olarak, frames[0].save(...) kodu ile GIF'i kaydediyoruz. 
# save_all=True ile tüm resimleri kaydedeceğimizi belirtiyoruz. 
# append_images parametresi ile resimlerin listesini veriyoruz. 
# duration parametresi her bir karenin görüntülenme süresini milisaniye cinsinden belirler. 
# loop parametresi 0 olarak ayarlanmış, yani sonsuz döngü anlamına gelir.
frames[0].save("simple_shape.gif", save_all=True,
               append_images=frames[1:], duration=100, loop=0)
