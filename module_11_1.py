import requests

res = requests.get('https://www.bookvoed.ru/')
print(res)
print(res.content)
res.encoding = 'utf-8'
print(res.text)

mp = requests.get('https://rus.hitmotop.com/')
with open('song.mp3', 'wb') as f:
    f.write(mp.content)


from PIL import Image

image = Image.open('картинка.png')
new_size = (100, 100)

resized_image = image.resize(new_size)
resized_image.save('resized_картинка.png')

image_2 = Image.open('resized_картинка.png')
blackAndWhite = image_2.convert('L')
blackAndWhite.save('bw_resized_картинка.png')