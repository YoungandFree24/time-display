# from django.shortcuts import HttpResponse, redirect
# from django.http import JsonResponse

# # Create your views here.
# # Responses Go here!!!!!!
#  Extra methods
# ----------------------------------------------------------------------
# def root(request):
#     return HttpResponse("String response from root_method")
# # def another_route(request):
# #     return render("/root")

# # def redirected_method(request):
# #     return JsonResponse({"response": "JSON Response from redirected_method", "status": True})

# def root(request):
#     return redirect("/blogs")


# Routing lecture is the method below
# def index(request):
#     return JsonResponse({"responce": "placeholder to later display a list of all blogs with a method named index"})
# use the path('', views.index in the urls.py)


# def new(request):
#     return JsonResponse({"responce": "placeholder to display a new form to create a new blog"})

# def create(request):
#     return redirect("/blogs")

# def show(request):
#     return JsonResponse({"response": "placeholder to display blog number", "status": True})

# def edit(request):
#     return JsonResponse({"response": "placeholder to edit blog number", "status": True})
    
# def destroy(request):
#     return redirect("/blogs")

# def root(request):
#     return render(request, "")


# --------------------------------------------------- Ends extra methods
# from django.shortcuts   import render # notice the import!
# def root(request):
#     return render(request, "index.html")
# Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.


# or

# def root(request):
#     context = {
#     "name": "Noelle",
#     "favorite_color": "turquoise",
#     "pets": ["Bruce", "Fitz", "Georgie"]
#     }
#     return render(request, "index.html", context)

# def second_view(request):
#     context = {
#         'data':[1,2,3]
#     }
#     return render(request, "other_template.html", context)

from django.shortcuts import render
from time import gmtime, strftime
    
def index(request):
    all_the_Users = User.objects.all()
    context = {
        'all_the_Users' : all all_the_Users
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'index.html', context)