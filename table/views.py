from django.shortcuts import render
from table.models import Table
from table.forms.form import Form
import json

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
    
def index(request):
    if not request.method == "POST" and 'page' in request.GET:
        if 'search-query' in request.session:
            request.POST = request.session['search-query']
            request.method = 'POST'
    if request.method == 'POST':
        form = Form(request.POST)
        request.session['search-query'] = request.POST
        if form.is_valid():
            if not form.cleaned_data.get('value'):
                table_list=Table.objects.all()
            else:
                if form.cleaned_data.get('statement') == '=':
                    table_list = Table.objects.filter(**{form.cleaned_data.get('col'): form.cleaned_data.get('value')})
                if form.cleaned_data.get('statement') == '<':
                    table_list = Table.objects.filter(**{form.cleaned_data.get('col')+'__lte':form.cleaned_data.get('value')})
                if form.cleaned_data.get('statement') == '>':
                    table_list = Table.objects.filter(**{form.cleaned_data.get('col')+'__gte':form.cleaned_data.get('value')})
            page = request.GET.get('page', 1)
            paginator = Paginator(table_list, 5)

            try:
                table = paginator.page(page)
            except PageNotAnInteger:
                table = paginator.page(1)
            except EmptyPage:
                table = paginator.page(paginator.num_pages)
            return render(request, 'template.html', {'table': table,'form':form})
    else:
        table_list = Table.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(table_list, 5)
        try:
            table = paginator.page(page)
        except PageNotAnInteger:
            table = paginator.page(1)
        except EmptyPage:
            table = paginator.page(paginator.num_pages)
            
        context = {
            'form': Form(),
            'table':table,
        }
        return render(request, 'template.html', context)