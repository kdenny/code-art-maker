from PIL import Image
from resizeimage import resizeimage


img_1 = 'kd/suit.jpg'
img_2 = 'kd/gothic.jpg'

i1 = Image.open(img_1)
i2 = Image.open(img_2)

image_1 = {
    'file': img_1,
    'width': i1.size[0],
    'height': i1.size[1],
}

image_2 = {
    'file': img_2,
    'width': i2.size[0],
    'height': i2.size[1],
}

if image_1['width'] > image_2['width']:
    min_width = image_2['width']
else:
    min_width = image_1['width']

if image_1['height'] > image_2['height']:
    min_height = image_2['height']
else:
    min_height = image_1['height']

ifr = image_1['file'].replace(".","_resize.")
ifr2 = image_2['file'].replace(".","_resize.")

with open(image_1['file'], 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [min_width, min_height])
        cover.save(ifr, image.format)

with open(image_2['file'], 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [min_width, min_height])
        cover.save(ifr2, image.format)

image_1['resized'] = ifr
image_2['resized'] = ifr2
