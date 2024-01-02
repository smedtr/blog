import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene import relay

from blog import models
from blog import types
from blog import connections


# The query class
class Query(graphene.ObjectType):
    site = graphene.Field(types.SiteType) 

    all_posts = graphene.List(types.PostType)
    
    all_categories = graphene.List(types.CategoryType)
    all_tags = graphene.List(types.TagType)
    all_users = graphene.List(types.UserType)
    
    posts_by_category = graphene.List(types.PostType, category=graphene.String())
    posts_by_tag = graphene.List(types.PostType, tag=graphene.String())
    #posts_by_slug = graphene.List(types.PostType, slug=graphene.String())
    post_by_slug = graphene.Field(types.PostType, slug=graphene.String())
    posts_tobe_approved = graphene.List(types.PostType)

    current_user = graphene.Field(types.UserType, username=graphene.String())
    ###
    # Relay style met pagination
    ###all_posts_paginated = relay.ConnectionField(connections.PostsPaginatedConnection)  
    all_posts_paginated = DjangoFilterConnectionField(types.PostNode)#   
    #### WorkInProgress    
    relay_post_by_id = relay.Node.Field(types.PostNode)     
    all_posts_by_tag_paginated = DjangoFilterConnectionField(types.PostNode)
    ####
    
    #def resolve_all_posts_paginated(root, info, **kwargs):
    #    return models.Post.objects.all()

    def resolve_posts_by_tag_paginated(root, info, tag, **kwargs):
        return (
            models.Post.objects.filter(tag__slug__iexact=tag)
        )
    
    def resolve_site(root, info):
        return (
            models.Site.objects.first()
        )
    
    def resolve_all_posts(root, info):
        return (
            models.Post.objects.all()
        )
    
    def resolve_all_categories(root, info):
        return (
            models.Category.objects.all()
        )
    
    def resolve_all_tags(root, info):
        return (
            models.Tag.objects.all()
        )
    
    def resolve_posts_by_category(root, info, category):        
        return (            
            models.Post.objects.filter(category__slug__iexact=category)
        )
    
    def resolve_posts_by_tag(root, info, tag):
        return (
            models.Post.objects.filter(tag__slug__iexact=tag)
        )    
       
    def resolve_post_by_slug(root, info, slug):
        return (
            models.Post.objects.filter(slug__iexact=slug).first()
        )
    
    def resolve_posts_tobe_approved(root, info):
        return (
            models.Post.objects.filter(is_published=False)
        )

    def resolve_all_users(root, info):
        return (
            models.User.objects.all()
        )
    
    def resolve_current_user(self, info, username):
        return (
            models.User.objects.get(username__iexact=username)
        )