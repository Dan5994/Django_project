from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post
from django.shortcuts import get_object_or_404

# Create your views here.
def parsing_data(post:Post):
    return ({'id':post.id, 'title':post.title, 'text':post.text, 'counter':post.counter})


@csrf_exempt 
def get_post(request):
    result = {
        'data':[],
        'filt_by_count':[]
    }
    post = Post.objects.all().order_by('-title')
    for item in post:
        result['data'].append(parsing_data(item))
    for item in post.filter(counter=3):
        result['filt_by_count'].append(parsing_data(item))
    result['count']=post.count()
    return JsonResponse(result)


@csrf_exempt 
def create_post(request):
    title = request.POST.get('title')
    text = request.POST.get('text')
    new_post = Post(title = title, text = text)
    new_post.save()
    return HttpResponse('Post created')


csrf_exempt
def one_post(request,_id):
    new = get_object_or_404(Post, id=_id)
    return JsonResponse(parsing_data(new))

@csrf_exempt 
def post_delete(request,_id):
    post = Post.objects.get(id=_id)
    post.delete()
    return HttpResponse('Post deleted')


@csrf_exempt 
def post_update(request, _id):
    upd_post = Post.objects.filter(id=_id).update(title = 'title', text = 'hfghkdda')
    return HttpResponse('Post update')


def check_if_exist(request, counter):
    post = Post.objects.filter(counter=counter).exists()
    result = {'is_exist':post}
    return JsonResponse(result)

def get_or_create(request, counter):
    post, is_created = Post.objects.get_or_create(counter=3, title='news', text = 'first news')
    return JsonResponse(parsing_data(post))