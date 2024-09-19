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

new_size = (100, 100)
with Image.open('картинка.png') as image:
    resized_image = image.resize(new_size)
    resized_image.save('resized_картинка.png')

with Image.open('resized_картинка.png') as image_2:
    blackAndWhite = image_2.convert('L')
    blackAndWhite.save('bw_resized_картинка.png')
blackAndWhite.save('bw_resized_картинка.png')
