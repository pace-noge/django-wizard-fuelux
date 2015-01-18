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
            step = request.GET.get('step')
            publication = Publication.objects.get(id=publication_id)
            selected_articles = publication.article_set.all()
            articles = Article.objects.all()
            if step == "2":
                template = "dataset/step_2.html"
            elif step == "3":
                template = "dataset/step_3.html"
            data = {
                "title": publication.title,
                "publication_id": publication_id,
                "articles": articles,
                "selected_articles": selected_articles
            }
            return render_to_response(template, data, context_instance=RequestContext(request))




def article(request):
    if request.is_ajax():
        response_data = {}
        if request.method == "POST":
            if request.POST.get('action') == "new":
                article = request.POST.get('headline')
                a = Article(headline=article)
                a.save()

                response_data['status'] = "success"
                response_data["article"] = {'id': a.id, 'headline': a.headline}
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            elif request.POST.get('action') == "update_publication":
                pub_id = request.POST.get('publication_id')
                p = Publication.objects.get(id=pub_id)
                # clear publication relation
                p.article_set.clear()
                articles = request.POST.getlist('articles[]')
                # print len(articles)
                if articles[0] != "":
                    for article in articles:
                        a = Article.objects.get(id=article)
                        p.article_set.add(a)
                    response_data["status"] = "success"
                    return HttpResponse(json.dumps(response_data), content_type='application/json')
    response_data["status"] = "Unknown request"
    return HttpResponse(json.dumps(response_data), content_type='application/json')


