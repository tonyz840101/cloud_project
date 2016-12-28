from django.db import models
# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return './another/txt/user_{0}/{1}'.format(instance.filename, filename)

class Table(models.Model):
    filename = models.CharField(max_length=100)
    file = models.FileField(upload_to=user_directory_path)



    def __str__(self):
        return self.filename


