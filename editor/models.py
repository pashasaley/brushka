import cloudinary.api
import cloudinary
import cloudinary.uploader
import secrets
from django.db import models
from django.core.files import File
from admin_page.models import get_user


class TShirts(models.Model):
    name_TShirts = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    link_TShirts = models.CharField(max_length=512)
    price = models.IntegerField()
    description = models.TextField()


class Tags(models.Model):
    tag = models.CharField(max_length=64)
    id_ts = models.ForeignKey(TShirts, on_delete=models.CASCADE)


def sending_picture(picture):
    x = secrets.token_hex(6)
    f = open('d:/image_tshirts/' + x + '.svg', 'w')
    my_file = File(f)
    my_file.write(picture)
    my_file.close()
    return cloudinary.uploader.upload_image('d:/image_tshirts/' + x + '.svg')


def save_t_shirts(name, username, name_in_cloud, price, description):
    link = 'https://res.cloudinary.com/danzp4kma/image/upload/v1572271002/' + name_in_cloud + '.jpeg'
    t_shirts = TShirts(name_TShirts=name, username=username,
                       link_TShirts=link, price=price, description=description)
    t_shirts.save()
    return t_shirts


def save_tags(tags, t_shirt):
    for tag in tags:
        tags_ts = Tags(tag=tag, id_ts=t_shirt)
        tags_ts.save()


def get_username(id_user):
    user = get_user(id_user)
    return user.username


def get_tags():
    return Tags.objects.distinct('tag')[:20]
