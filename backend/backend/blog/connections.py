import graphene
from graphene import relay

from blog import types

class PostsPaginatedConnection(relay.Connection):
    class Meta:
        node = types.PostsPaginatedType
#
class PostsTagPaginatedConnection(relay.Connection):
    class Meta:
        node = types.PostsTagPaginatedType
        
