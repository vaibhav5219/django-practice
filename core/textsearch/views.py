from django.shortcuts import render
from textsearch.models import TextSearchProduct
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, TrigramSimilarity # type: ignore
from django.db.models import Q
from django.views.decorators.cache import cache_page
from django.core.cache import cache

# Create your views here.

# @cache_page(60 * 15)
def index(request):
    search = request.GET.get('search')

    if search:
        # results = TextSearchProduct.objects.filter(title__search = search)
        # results = TextSearchProduct.objects.annotate(
        #     # search = SearchVector('title', 'description')  # Rank wise search together
        #     search = SearchVector('title') + SearchVector('title')  # Rank wise search 
        # ).filter(search = search)

        # search_query = SearchQuery(search)
        # results = TextSearchProduct.objects.annotate(
        #     # search = SearchVector('title', 'description')
        #     search = SearchVector('title') + SearchVector('title')
        # ).filter(search = search_query)

        # search_query = SearchQuery(search)
        # # search_vector = SearchVector('title', 'description', 'brand')
        # search_vector = (
        #     SearchVector('title', weight = 'A') +    # Will have higher priority in rank
        #     SearchVector('description', weight = 'B') +
        #     SearchVector('brand', weight = 'C')      # Will have lower priority
        # )
        # search_rank = SearchRank(search_vector, search_query)
        # results = TextSearchProduct.objects.annotate(
        #     rank = search_rank                          # Will create a rank field
        # ).filter(rank__gte = 0.0).order_by('-rank')

        ## Search Headline in any html field

        # search_query = SearchQuery(search, search_type='phrase') | SearchQuery(search, search_type='phrase')
        # search_vector = (
        #     SearchVector('title', weight = 'A') +    # Will have higher priority in rank
        #     SearchVector('description', weight = 'B') +
        #     SearchVector('brand', weight = 'C')      # Will have lower priority
        # )
        # search_rank = SearchRank(search_vector, search_query)
        # results = TextSearchProduct.objects.annotate(
        #     headline = SearchHeadline(
        #         'search in html'
        #     )
        # ).filter(rank__gte = 0.0).order_by('-rank')

        # TrigamSimilarity
        print('1. ', search)
        search_query = SearchQuery(search, search_type="raw")
        search_vector = SearchVector(
            'title', 'description',  'category', 'brand'
        )
        search_rank = SearchRank(search_vector, search_query)
        print('2. ', search)
        results = TextSearchProduct.objects.annotate(
            rank = search_rank,
            similarity = (
                TrigramSimilarity('title', search) +
                TrigramSimilarity('description', search) +
                TrigramSimilarity('category', search) +
                TrigramSimilarity('brand', search)
            )
        ).filter(Q(rank__gte=0.01) | Q(similarity__gte=0.1)).distinct().order_by("-rank", "-similarity")


    else:
        results = TextSearchProduct.objects.all()
    
    if request.GET.get('min_price') and request.GET.get('max_price'):
        min_price = float(request.GET.get('min_price'))
        max_price = float(request.GET.get('max_price'))
        results = results.filter(
            price__gte=min_price, price__lte=max_price
        )
    if request.GET.get('brand'):
        results = results.filter(
            brand = request.GET.get('brand')
        )
    if request.GET.get('category'):
        results = results.filter(
            brand = request.GET.get('category')
        )
    
    
    if cache.get('brands'):
        brands = cache.get('brands')
        print("FROM CACHE")
    else:
        cache.set("brands", TextSearchProduct.objects.all().distinct('brand').order_by('brand'), 60 * 10 )
        brands = TextSearchProduct.objects.all().distinct('brand').order_by('brand')
    
    # Deleting cache => cache.delete("key")
    
    if cache.get('categories'):
        categories = cache.get('categories')
        print("FROM CACHE")
    else:
        cache.set("categories", TextSearchProduct.objects.all().distinct('category').order_by('category'), 60 * 10 )       
        categories = TextSearchProduct.objects.all().distinct('category').order_by('category')

    return render(request, 'index.html', { 'results' : results, 'search': search, 'brands': brands, 'categories': categories})