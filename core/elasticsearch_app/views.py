from django.shortcuts import render
from django.http import JsonResponse
from .documents import ProductDocument
from elasticsearch_dsl.query import MultiMatch # type: ignore

def search_product(request):
    data = {
            "status" : 200,
            "message" : "products",
            "products" : []
        }
    if request.GET.get('search'):
        # search = request.GET.get('search')
        
        search = request.GET.get('search').split(',') if ',' in  request.GET.get('search') else request.GET.get('search')
        
        # result = ProductDocument.search().query(
        #     'term',  # Exact match (every character matches)
        #     brand_name__brand_name = search   # 1st 'brand_name' is foreign key and 2nd brand_name is property
        # )
        result = ProductDocument.search().query(
            'term',  # Exact match (every character matches)
            brand_name__brand_name = search   # 1st 'brand_name' is foreign key and 2nd brand_name is property
            # gere search is a list
        ).extra(from_ = 1 , size = 3)   # here it will provide from 1 to 2, and 3rd will exclude
        # extra(size=20)
        # result = ProductDocument.search().query(
        #     'match',  # matches any character
        #     title = search
        # )
        # result = ProductDocument.search().query(
        #     'match',  # matches any character
        #     title = {
        #         "query" : search,
        #         "fuzziness" : "AUTO", # 1, 2, "AUTO" is fuzziness
        #     })
        # result = ProductDocument.search().query(
        #     MultiMatch( 
        #             query = search,
        #             fields = [
        #                 "title",
        #                 "description",
        #                 "category",
        #                 "brand",
        #                 "sku",
        #                 "thumbnail",
        #             ],
        #     )
        # ).sort('_sore')    # .sort('_price')
        # .collapse(field = "price") => Distinct
        
        result = result.execute()
        products = []
        for hit in result:
            products.append({
                "title" : hit.title,
                "description" : hit.description,
                "category" : hit.category,
                "price" : hit.price,
                "brand" : hit.brand,
                "sku" : hit.sku,
                "thumbnail" : hit.thumbnail,
                "score" : hit.meta.score,
            })
        
        data["products"] = products
    return JsonResponse(data=data)