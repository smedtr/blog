import graphene
from graphene_django import DjangoObjectType
from graphene import relay
from blog import models


# Define type
class SiteType(DjangoObjectType):
    class Meta:
        model = models.Site

class UserType(DjangoObjectType):
    class Meta:
        model = models.User

class CategoryType(DjangoObjectType):
    class Meta:
        model = models.Category

class TagType(DjangoObjectType):
    class Meta:
        model = models.Tag

class PostType(DjangoObjectType):
    class Meta:
        model = models.Post        

    number_of_likes = graphene.String()    

    def resolve_number_of_likes(self, info):
        return self.get_number_of_likes()
    
class PostsPaginatedType(DjangoObjectType):
    class Meta:
        model = models.Post
        interfaces = (relay.Node,)  # make sure you add this
        fields = "__all__"

    number_of_likes = graphene.String()    

    def resolve_number_of_likes(self, info):
        return self.get_number_of_likes()

class CommentType(DjangoObjectType):
    class Meta:
        model = models.Comment
    
    number_of_likes = graphene.String()

    def resolve_number_of_likes(self, info):
        return self.get_number_of_likes()
    

