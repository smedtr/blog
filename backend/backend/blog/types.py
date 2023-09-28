import graphene
from graphene_django import DjangoObjectType
from blog import models

# Define type
class SiteType(DjangoObjectType):
    class Meta:
        model = models.Site

