from django.shortcuts import render
from textsearch.models import TextSearchProduct
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline # type: ignore

# Create your views here.

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

        search_query = SearchQuery(search, search_type='phrase') | SearchQuery(search, search_type='phrase')
        search_vector = (
            SearchVector('title', weight = 'A') +    # Will have higher priority in rank
            SearchVector('description', weight = 'B') +
            SearchVector('brand', weight = 'C')      # Will have lower priority
        )
        search_rank = SearchRank(search_vector, search_query)
        results = TextSearchProduct.objects.annotate(
            headline = SearchHeadline(
                'search in html'
            )
        ).filter(rank__gte = 0.0).order_by('-rank')


    else:
        results = TextSearchProduct.objects.all()

    return render(request, 'index.html', { 'results' : results, 'search': search})