from django.shortcuts import render
from .scrap_script import scrape_imdb_news
from django.http import JsonResponse
from .models import News
from .tasks import add
from django.shortcuts import get_object_or_404


def run_scraper(request):
    scrape_imdb_news()
    return JsonResponse({
        "status" : True,
        "message" : "scraper executed"
    })
    # obj = get_object_or_404(News, id)
    # return JsonResponse({
    #     "status" : True,
    #     "message" : "scraper executed"
    # })


def index(request):
    # result  = add(10, 5)
    result  = add.delay(10, 5) # type: ignore
    print(result)
    return render(request, 'index.html', context={
        "news_data" : News.objects.all()
    })