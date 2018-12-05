from django.db import models

# Create your models here.

IMAGE_TYPE = (
    ('photo', 'photo'),
    ('drawing', 'drawing'),
    ('print', 'print'),
    ('landscape', 'landscape'),
)

class Image(models.Model):
    title = models.CharField(max_length=100)
    filename = models.CharField(max_length=800)
    type = models.CharField(max_length=100, choices=IMAGE_TYPE, default='photo')
    file = models.ImageField(upload_to='sources/', default='sources/no-img.jpg')

    # Returns the string representation of the model.
    def __unicode__(self):  # __unicode__ on Python 2
        return str(self.title + ' - ' + self.type)

    def __str__(self):
        return str(self.title + ' - ' + self.type)

class ResizedImage(models.Model):
    original = models.ForeignKey(Image, related_name='resizes', blank=True, null=True, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='resized/', default='sources/no-img.jpg')
    height = models.IntegerField()
    width = models.IntegerField()


    # Returns the string representation of the model.
    def __unicode__(self):  # __unicode__ on Python 2
        return str(self.file.title + ' - ' + str(self.height) + ' x ' + str(self.width))

    def __str__(self):
        return str(self.file.title + ' - ' + str(self.height) + ' x ' + str(self.width))

PROJECT_STATUS = (
    ('queue', 'queue'),
    ('test', 'test'),
    ('pending', 'pending'),
    ('running', 'running'),
    ('completed', 'completed'),
)

class ArtProject(models.Model):
    # source = models.ForeignKey(ResizedImage, related_name='riffed', null=True, blank=True, on_delete=models.SET_NULL)
    source = models.CharField(max_length=500)
    style = models.CharField(max_length=500)
    # style = models.ForeignKey(ResizedImage, related_name='transferred', null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=50, choices=PROJECT_STATUS)
    output_file = models.CharField(max_length=500)
    # file = models.ImageField(upload_to='output/', default='sources/no-img.jpg', blank=True, null=True)
    checkpoint = models.CharField(max_length=500)
    added_at = models.DateTimeField(auto_now_add=True)


    # Returns the string representation of the model.
    def __unicode__(self):  # __unicode__ on Python 2
        return str(self.source + ' - ' + self.style)

    def __str__(self):
        return str(self.source + ' - ' + self.style)
