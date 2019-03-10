from PIL import Image

aimage = Image.open('a.jpg')

print(aimage.size)

new_a_image = aimage.resize((7, 10))
print(new_a_image.size)
new_a_image.save('new_a.jpg')

bimage = Image.open('b.jpg')

print(bimage.size)

new_b_image = bimage.resize((7, 13))
print(new_b_image.size)
new_b_image.save('new_b.jpg')

cimage = Image.open('c.jpg')

print(cimage.size)

new_c_image = cimage.resize((7, 10))
print(new_c_image.size)
new_c_image.save('new_c.jpg')