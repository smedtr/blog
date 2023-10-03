import graphene
from blog import models
from blog import types

# The query class
class Query(graphene.ObjectType):
    site = graphene.Field(types.SiteType) 

    all_posts = graphene.List(types.PostType)
    all_categories = graphene.List(types.CategoryType)
    all_tags = graphene.List(types.TagType)
    all_users = graphene.List(types.UserType)
    
    posts_by_category = graphene.List(types.PostType, category=graphene.String())
    posts_by_tag = graphene.List(types.PostType, tag=graphene.String())
    posts_by_slug = graphene.List(types.PostType, slug=graphene.String())

    current_user = graphene.Field(types.UserType, username=graphene.String())
    

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
            models.Posts.objects.filter(category__slug__iexact=category)
        )
    
    def resolve_posts_by_tag(root, info, tag):
        return (
            models.Posts.objects.filter(tag__slug__iexact=tag)
        )
    
    def resolve_posts_by_slug(root, info, slug):
        return (
            models.Posts.objects.get(slug__iexact=slug)
        )
    
    def resolve_all_users(root, info):
        return (
            models.User.objects.all()
        )
    
    def resolve_current_user(self, info, username):
        return (
            models.User.objects.get(username__iexact=username)
        )