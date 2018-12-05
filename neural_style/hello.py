import os

from PIL import Image
from resizeimage import resizeimage

def resize_images(img_1, img_2):

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

    data = {
        'source': ifr,
        'style': ifr2
    }

    return data


def make_art(content, style, test=True, fname=''):

    if fname != '':
        fname = fname
        checkpoint = "checkpoint/" + fname + "_checkpoint_%s.jpg"
    else:
        c = content.split("/")
        co = c[len(c)-1].replace(".jpg","")
        s = style.split("/")
        so = s[len(s) - 1].replace(".jpg","")
        fname = "merge_{0}_{1}.jpg".format(co, so)
        checkpoint = "checkpoint/" + fname + "_checkpoint_%s.jpg"

    if test:
        iterations = 100
        cit = 10
    else:
        iterations = 500
        cit = 50

    rst = "python neural_style.py --content {0} --styles {1} --output {2} --iterations {3} --checkpoint-output {4} --checkpoint-iterations {5}".format(content, style, fname, str(iterations), checkpoint, str(cit))
    print(rst)
    os.system(rst)

content = 'kd/suit.jpg'
style = 'kd/gothic.jpg'

d = resize_images(content, style)

make_art(d['source'], d['style'])
