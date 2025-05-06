from django_elasticsearch_dsl import Document, fields # type: ignore
from django_elasticsearch_dsl.registries import registry # type: ignore
from .models import Product

@registry.register_document
class ProductDocument(Document):
    class Index:
        name = 'products'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}
    
    ''' For Foreign Fields '''
    brand_name = fields.ObjectField(properties = {
        "brand_name" : fields.KeywordField() # Exact Match
    })
        
    class Django:
        model = Product
        fields = [
            "title",
            "description",
            "category",
            "price",
            "brand",
            "sku",
            "thumbnail",
        ]
        

'''  Only for Single table, not for relationships '''

# @registry.register_document
# class ProductDocument(Document):
#     class Index:
#         name = 'products'
#         settings = {'number_of_shards': 1,
#                     'number_of_replicas': 0}
        
#     class Django:
#         model = Product
#         fields = [
#             "title",
#             "description",
#             "category",
#             "price",
#             "brand",
#             "sku",
#             "thumbnail",
#         ]