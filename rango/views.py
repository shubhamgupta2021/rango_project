from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    #return  HttpResponse("<h1>Hello World</h1> <br><br>Click <a href=/rango/about/>here </a> for About page ")
    category_list = Category.objects.order_by("-views")[:20]
    context_dict = {'categories': category_list}
    return render(request, "rango/index.html", context_dict)

def about(request):
    return render(request, "rango/about.html", {})

def category(request,category_name_slug ):
    context_dict = {'category_name_slug' : category_name_slug}

    try:
        categories = Category.objects.get(slug = category_name_slug)
        context_dict['category_name'] = categories.name

        pages = Page.objects.filter(category = categories)

        context_dict['pages'] = pages

    except Category.DoesNotExist:
        pass

    return render(request, 'rango/category.html', context_dict)

@login_required
def add_category(request):

    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print form.errors
    else:
        form = CategoryForm()

    return render(request, "rango/add_category.html", {"form": form})

@login_required
def add_page(request, category_name_slug):

    try:
        cat=  Category.objects.get(slug = category_name_slug)
    except Category.DoesNotExist:
        cat = None

    if request.method == "POST":
        form = PageForm(request.POST)

        if form.is_valid():
            if cat:
                page = form.save(commit= False)
                page.category = cat
                page.views = 0
                page.save()

            return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()
    content_dict =  {'form' : form, 'category': cat }
    return render(request, "rango/add_page.html", content_dict)




def register(request):

    registered = False
    context_dict = {}
    if request.method == "POST":
        user_form  = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid() :
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save( commit= False)
            profile.user = user

            if 'image' in request.FILES:
                profile.image = request.FILES['image']
            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context_dict['user_form'] = user_form
    context_dict['profile_form'] = profile_form
    context_dict['registered'] = registered
    return render(request, 'rango/register.html',context_dict )

# def user_login(request):
#
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         user = authenticate(username=username, password=password)
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect("/rango/")
#             else:
#                 return HttpResponse("Your account is disabled.")
#
#         else:
#             return HttpResponse("Invalid Credentials")
#     else:
#
#         return render(request, "rango/login.html")

@login_required
def user_logout(request):

    logout(request)

    return HttpResponseRedirect("/linkfair/")

def user_login(request):

    if request.method == "POST":
        loginform = LoginForm(request.POST)
        print loginform
        username = loginform.cleaned_data['username']
        password = loginform.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/linkfair/")
            else:
                return HttpResponse("Your account is disabled.")

        else:
            return HttpResponse("Invalid Credentials")
    else:
        loginform = LoginForm()
        return render(request, "rango/login.html", {'form' : loginform})