import graphene
from blog import models
from blog import types

# The query class
class Query(graphene.ObjectType):
    site = graphene.Field(types.SiteType) 
    
    def resolve_site(root, info):
        return (
            models.Site.objects.first()
        )