'''from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$', views.flower_view, name='flower'),
url(r'^$', views.flowers_view, name='flowers'),
url(r'^$', views.create_flower, name='create_flower'),
url(r'^$', views.LoginFormView, name='login'),
url(r'^$', views.LogoutView, name='logout'),
url(r'^$', views.RegisterFormView, name='register'),
url(r'^$', views.add, name='add'),
]def avatar_upload_to(instance, filename):
    return os.path.join('uploads', instance.name + os.path.splitext(filename)[1])

class Flowers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    size = models.CharField(max_length=30)
    picture = models.ImageField(upload_to=avatar_upload_to)
# Create your models here.

class Flower_user(models.Model):
    flower_id = models.ForeignKey(Flowers, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

'''
from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$', views.flowers, name='flowers'),
url(r'^$', views.flower_user, name='flower_user')
]