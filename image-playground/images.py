from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img = img.convert('L')
# print(img.format)
# crooked = filtered_img.rotate(180)
# resize = filtered_img.resize((300, 300))
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("grey.png", 'png') 

img = Image.open('./astro.jpg')
# new_img = img.resize((400, 400))
img.thumbnail((400, 400))
img.save('thumbnail.jpg')
