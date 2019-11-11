from django.shortcuts import render, redirect
from .models import sending_picture, save_t_shirts, save_tags, get_username
from furl import furl


def index(request):
    if request.method == 'POST':
        data = get_data_t_shirts(request)
        f = furl(data['path'])
        if data['path'] == '/editor/':
            username = request.user.username
        else:
            username = get_username(f.args['user'])
        tags = data['string_tags'].split(' ')
        y = str(sending_picture(data['svg_picture']))
        t_shirt = save_t_shirts(data['name_t_shirts'], username, y, data['price'], data['description'])
        if tags[0] != '':
            save_tags(tags, t_shirt)
        return redirect('editor_index')
    else:
        return render(request, 'editor.html')


def get_data_t_shirts(request):
    name_t_shirts = request.POST['name']
    string_tags = request.POST['tags_t']
    svg_picture = request.POST['url']
    price = int(request.POST.get('price_t', False))
    description = request.POST.get('description_t', False)
    path = request.get_full_path()
    data = {'name_t_shirts': name_t_shirts, 'string_tags': string_tags, 'svg_picture': svg_picture,
            'price': price, 'description': description, 'path': path}
    return data
