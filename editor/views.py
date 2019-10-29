import cloudinary.api
import cloudinary
import cloudinary.uploader
import secrets
from django.core.files import File
from django.shortcuts import render, redirect
from .models import TShirts


def index(request):
    if request.method == 'POST':
        tshirts = TShirts()
        tshirts.name_TShirts = request.POST['name']
        tshirts.username = request.user.username
        svg_picture = request.POST['url']
        tshirts.price = int(request.POST.get('price_t', False))
        tshirts.description = request.POST.get('description_t', False)
        x = secrets.token_hex(6)
        f = open('d:/image_tshirts/' + x + '.svg', 'w')
        my_file = File(f)
        my_file.write(svg_picture)
        my_file.close()
        y = cloudinary.uploader.upload_image('d:/image_tshirts/' + x + '.svg')
        y = str(y)
        tshirts.link_TShirts = 'https://res.cloudinary.com/danzp4kma/image/upload/v1572271002/' + y + '.jpeg'
        tshirts.save()
        return redirect('editor_index')
    else:
        return render(request, 'editor.html')

