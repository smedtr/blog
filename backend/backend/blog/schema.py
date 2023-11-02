import graphene
from graphene_django.filter import DjangoFilterConnectionField
from blog import queries, mutations

schema = graphene.Schema(
    query=queries.Query, 
    mutation=mutations.Mutation
    )
