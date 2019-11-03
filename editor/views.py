import cloudinary.api
import cloudinary
import cloudinary.uploader
import secrets
from django.core.files import File
from django.shortcuts import render, redirect
from .models import TShirts, Tags


def index(request):
    if request.method == 'POST':
        name_TShirts = request.POST['name']
        username = request.user.username
        string_tags = request.POST['tags_t']
        tags = string_tags.split(' ')
        svg_picture = request.POST['url']
        price = int(request.POST.get('price_t', False))
        description = request.POST.get('description_t', False)
        x = secrets.token_hex(6)
        f = open('d:/image_tshirts/' + x + '.svg', 'w')
        my_file = File(f)
        my_file.write(svg_picture)
        my_file.close()
        y = cloudinary.uploader.upload_image('d:/image_tshirts/' + x + '.svg')
        y = str(y)
        link_TShirts = 'https://res.cloudinary.com/danzp4kma/image/upload/v1572271002/' + y + '.jpeg'
        tshirt = TShirts(name_TShirts=name_TShirts, username=username,
                         link_TShirts=link_TShirts, price=price, description=description)
        tshirt.save()
        for tag in tags:
            tags_ts = Tags(tag=tag, id_ts=tshirt)
            tags_ts.save()
        return redirect('editor_index')
    else:
        return render(request, 'editor.html')

