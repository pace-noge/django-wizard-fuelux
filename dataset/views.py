from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from .models import Publication, Article
from django.http import HttpResponse
import json

# Create your views here.

def home(request):
    publications = Publication.objects.all()
    return render(request, "dataset/index.html", {"publications": publications})

def publication(request):
    if request.is_ajax():
        if request.method == "POST":
            title = request.POST.get("title")
            p = Publication(title=title)
            response_data = {}
            try:
                p.save()
                response_data['status'] = "success"
            except:
                response_data["status"] = "failed"
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            publication_id = request.GET.get('id')
            publication = Publication.objects.get(id=publication_id)
            article = publication.article_set.all()
            all_article = Article.objects.all()
            template = "dataset/step_2.html"
            data = {
                "title": publication.title,
                "articles": article,
                "all_articles": all_article
            }
            return render_to_response(template, data, context_instance=RequestContext(request))




def article(request):
    if request.is_ajax():
        article = request.GET.get('publication')
        article = Article.publication.all()
