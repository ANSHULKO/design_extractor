# -*- encoding: utf-8 -*-


from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import *
from .forms import *
from django.shortcuts import redirect, render
from django.contrib import messages



@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    websites = Project.objects.all()
    ctx = {
            'websites':websites
    }
    return render(request,'home/index.html',ctx)

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

def add_website(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        title = request.POST.get('title')
        # print(name, url)
        if not url:
            messages.error(request, 'enter valid url!')
        elif not title:
            messages.error(request, 'enter valid title!')
        elif url and title:
            project = Project(title=title,url=url,user=request.user)
            project.save()
            messages.success(request, 'website success.')
    
    return redirect('/')


def project_details(request,id):
    ctx = {
        'project': Project.objects.get(id=id)
    }
    return render(request, 'home/project.html',ctx)


def project_reviews(request,id):
    ctx = {
        'reviews': Review.objects.filter(project__id=id).get()
    }
    return render(request, 'home/review.html',ctx)



def profile_detail(request):
    try:
        profile =Profile.objects.get(user=request.user)
        ctx = {'profile': profile}
        return render(request, 'home/profile.html',ctx)
    except:
        return redirect('/profile/edit')

def edit_profile(request):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST,request.user,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user= request.user
            profile.save()
            messages.success(request,"profile created successfully")
            return redirect('/profile')
        else:
            messages.error(request,"profile could not be created!")
    ctx = {'form':ProfileForm(),}
    return render(request, 'home/profile_edit.html',ctx)

    

def project_css(request,id):
    ctx = {
        'project': Project.objects.get(id=id),
        'cssfiles' : Css.objects.filter(project__id=id).all()
    }
    return render(request, 'home/css.html',ctx)


def project_js(request,id):
    ctx = {
        'project': Project.objects.get(id=id),
        'jsfiles' : Js.objects.filter(project__id=id).all()
    }
    return render(request, 'home/js.html',ctx)




