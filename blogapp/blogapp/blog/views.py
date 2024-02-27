from django.shortcuts import render,redirect
from blog.models import*
from django.contrib.auth import authenticate



# data = {
#     "blogs":[
#         {
#             "id":1,
#             "title":"react",
#             "image":"react.png",
#             "is_active":True,
#             "is_home":True,
#             "description":"güzel dil",
#         },
#                 {
#             "id":2,
#             "title":"node",
#             "image":"node.png",
#             "is_active":True,
#             "is_home":True,
#             "description":"güzel dil",
#         },        {
#             "id":3,
#             "title":"php",
#             "image":"php.png",
#             "is_active":False,
#             "is_home":False,
#             "description":"güzel dil",
#         },
#     ]
# }


# Create your views here.


def index(request):
    context = {
        "languages":Language.objects.filter(is_home = True , is_active = True),
        "frameworks":Frameworks.objects.filter(is_home = True , is_active = True),
        "categories":Category.objects.all(),
    }
    return render(request,'blog/index.html',context)


def blogs(request):
    context = {
        "languages":Language.objects.filter(is_active = True),
        "frameworks":Frameworks.objects.filter(is_active = True),
        "categories":Category.objects.all(),
    }
    return render(request,'blog/blogs.html',context)


def blog_details(request,slug):
    language = Language.objects.get(slug = slug)
    return render(request,'blog/blog_details.html' ,{"language":language})



def blogs_by_category(request,slug):
    context = {
    "languages":Language.objects.filter(is_active = True , category__slug = slug),
    "frameworks":Frameworks.objects.filter(is_active = True),
    "categories":Category.objects.all(),
    "selected_language":slug,
    }
    return render(request,'blog/blogs.html',context)



# languages = data["blogs"]
# selectedLanguage = [language for language in languages if language["id"]==id][0] (152.bölüm)


# selectedLanguage = None
# for language in languages:
# if language["id"] == id:
# selectedLanguage = language
