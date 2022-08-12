from django.shortcuts import render, HttpResponse
from posts.forms import CreateForm

# Create your views here.


def home(request):
    # print(request.user)
    return render(request, 'posts/base.html')


def posts(request, post_id: int):
    print(type(post_id), post_id)
    if request.method == 'GET':
        print("Параметры", request.GET)
    # elif request.method == 'POST':
    #     print("Параметры", request.POST)
    post_content = request.headers
    return render(request, 'posts/posts.html', {'content': request.GET})


def about(request):
    return render(request, 'posts/about.html', {'content': '<h1>About</h1>'})

# def create(request):
#     return render(request, 'posts/create.html', {'content': '<h1>Create</h1>'})

def create_post(request):
    print('create')
    user_form = CreateForm()

    if request.method == 'GET':
        return render(request, 'posts/create.html', {'form': user_form, 'qwert': 'asdfdsad'})
    elif request.method == 'POST':
        user_form = CreateForm(request.POST)
        if user_form.is_valid():
            return redirect('/')
        return render(request, 'posts/create.html', {'form': user_form})

    return render(request, 'posts/create.html', {'form': user_form})
