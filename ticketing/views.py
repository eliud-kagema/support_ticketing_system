from django.shortcuts import render

def index(request):
    context = {}
    template_name = 'index.html'
    return render(request, template_name, context)



def clients(request):
    context = {}
    template_name = 'clients/index.html'
    return render(request, template_name, context)


def support(request):
    context = {}
    template_name = 'support/index.html'
    return render(request, template_name, context)


def administrator(request):
    context = {}
    template_name = 'admin/index.html'
    return render(request, template_name, context)
