from django.shortcuts import render, HttpResponse
from .forms import ImageUploadForm
from .models import Image, ArtProject
from rest_framework.response import Response
from rest_framework.views import APIView
from resizeimage import resizeimage
from PIL import Image

# Create your views here.

def upload_pic(request):
    if request.method == 'POST':
        i = (request.FILES)['image']
        data = {
            'image': i,
            'title': request.POST['title']
        }

        i = Image.objects.create(
            file = data['image'],
            title = data['title'],
            filename = data['title'],
            type = 'photo'
        )
        i.save()
        print(i.file.width)
        il = Image.objects.all()
        data = {
            'message': 'success',
            'images': il
        }
        return render(request, 'art/home.html', data)

def homepage(request):
    i = Image.objects.all()
    data = {
        'images': i
    }
    return render(request, 'art/home.html', data)

class ImageList(APIView):
    def get(self, request, image_type='None'):
        if image_type == 'None':
            a = list(Image.objects.all().values('title', 'width', 'photo', 'filename'))
            data = {
                'data': a
            }
            return Response(a)

    def post(self, request):
        df = None

        return Response(None)

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

class ProjectsList(APIView):
    def get(self, request, status='all'):
        if status == 'all':
            data = {}
            statuses = list(ArtProject.objects.all().values_list('status', flat=True).distinct())
            for s in statuses:
                data[s] = ArtProject.objects.filter(status=s).values('id', 'source' 'style', 'file', 'checkpoint')
        else:
            d = ArtProject.objects.filter(status=status).values('id', 'source' 'style', 'file', 'checkpoint')
            data = {
                'projects': d
            }

        return Response(data)

    def post(self, request):
        od = {}
        d = request.data
        if 'id' not in d:
            og_source = str(d['source'])
            og_style = str(d['style'])
            m = resize_images(og_source, og_style)
            ape = ArtProject.objects.filter(source=m['source'], style=m['style'])
            if len(ape) == 0:
                np = ArtProject.objects.create(
                    source = m['source'],
                    style = m['style'],
                    status = 'queue'
                )
                if 'output_file' in d:
                    np.output_file = d['output_file']
                    np.checkpoint = d['output_file'].replace(".","_checkpoint_%s.")
                    pe = ArtProject.objects.filter(output_file=str(d['output_file']))
                    if len(pe) > 0:
                        fn = str(d['output_file']).replace(".", "_2.")
                    else:
                        fn = str(d['output_file'])
                    np.output_file = fn
                else:
                    l1 = str(d['source']).split("/")
                    l1d = l1[len(l1)-1].split(".")[0]
                    l2 = str(d['style']).split("/")
                    l2d = l2[len(l2) - 1].split(".")[0]

                    merge = l1d + "_" + l2d + "_merge.jpg"
                    pe = ArtProject.objects.filter(output_file=merge)
                    if len(pe) > 0:
                        fn = merge.replace(".", "_2.")
                    else:
                        fn = merge
                    np.output_file = fn
                    np.checkpoint = l1d + "_" + l2d + "_check_%s.jpg"
                np.save()
                od = {
                    'msg': 'Added to queue'
                }
            else:
                apf = ape[0]
                if apf.status == 'queue':
                    od = {
                        'msg': 'Already in queue!'
                    }
                else:
                    od = {
                        'msg': 'Already ran for these two files. Please add a new title.'
                    }
        else:
            ide = ArtProject.objects.filter(id=d['id'])
            if len(ide) == 0:
                p = ide[0]
                p.status = str(d['status'])
                p.save()

            od = {
                'msg': 'Updated status'
            }

        return Response(od)