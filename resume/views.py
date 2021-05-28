from django.http import HttpResponse


ind_file = open("/home/Alashmony/django_projects/mysite/resume/index.html", "r")
pro_file = open("/home/Alashmony/django_projects/mysite/resume/index1.html", "r")
exp_file = open("/home/Alashmony/django_projects/mysite/resume/index2.html", "r")
edu_file = open("/home/Alashmony/django_projects/mysite/resume/index3.html", "r")
skl_file = open("/home/Alashmony/django_projects/mysite/resume/index4.html", "r")
crs_file = open("/home/Alashmony/django_projects/mysite/resume/index5.html", "r")
ext_file = open("/home/Alashmony/django_projects/mysite/resume/index6.html", "r")
prs_file = open("/home/Alashmony/django_projects/mysite/resume/index7.html", "r")


def index(request):
    return HttpResponse(ind_file.read())

def pro(request):
    return HttpResponse(pro_file.read())

def exp(request):
    return HttpResponse(exp_file.read())

def edu(request):
    return HttpResponse(edu_file.read())

def skl(request):
    return HttpResponse(skl_file.read())

def crs(request):
    return HttpResponse(crs_file.read())

def ext(request):
    return HttpResponse(ext_file.read())

def prs(request):
    return HttpResponse(prs_file.read())