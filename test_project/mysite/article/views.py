from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from .models import ActicleColumn,ArticlePost
from .forms import ActicleColumnForm,ArticlePostForm


# Create your views here.

@login_required(login_url='/account/login/')
@csrf_exempt
def article_column(request):
    if request.method == "GET" :
        columns = ActicleColumn.objects.filter(user=request.user)
        column_form=ActicleColumnForm()
        return render(request, "article/column/article_column.html", {"columns": columns,"column_form":column_form})

    if request.method == "POST":
        column_name = request.POST['column']
        print("view",request.POST)
        columns = ActicleColumn.objects.filter(user_id=request.user.id,column=column_name)
        if columns:
            return HttpResponse('2')
        else:
            ActicleColumn.objects.create(user=request.user,column=column_name)
            return HttpResponse('1')


@login_required(login_url='/account/login/')
@require_POST
@csrf_exempt
def rename_article(request):
    print("POST:",request.POST)
    column_name = request.POST['column_name']
    column_id = request.POST['column_id']
    try:
        line = ActicleColumn.objects.get(id=column_id)
        line.column = column_name
        line.save()
        return HttpResponse("1")
    except:
        return HttpResponse("0")


@login_required(login_url='/account/login/')
@require_POST
@csrf_exempt
def delete_article_column(request):
    print("POST:",request.POST)
    column_id = request.POST['column_id']
    try:
        line = ActicleColumn.objects.get(id=column_id)
        line.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("2")



@login_required(login_url='/account/login')
@csrf_exempt
def article_post(request):
    if request.method=="POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            cd = article_post_form.cleaned_data
            try:
                new_article = article_post_form.save(commit=False)
                new_article.author = request.user
                new_article.column = request.user.article_column.get(id=request.POST['column_id'])
                new_article.save()
                return HttpResponse('1')
            except:
                return HttpResponse('2')
        else:
            return HttpResponse('3')
    else:
        article_post_form = ArticlePostForm()
        article_columns = request.user.article_column.all()
        return render(request,"article/column/article_post.html",{"article_post_form":article_post_form,"article_columns":article_columns})