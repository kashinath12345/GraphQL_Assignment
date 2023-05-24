import graphene
from graphene_django import DjangoObjectType
from .models import Post, Comment

class PostType(DjangoObjectType):
    class Meta:
        model = Post

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment

class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        description = graphene.String()
        publish_date = graphene.Date()
        author = graphene.String()

    post = graphene.Field(PostType)

    def mutate(self, info, title, description, publish_date, author):
        post = Post(title=title, description=description, publish_date=publish_date, author=author)
        post.save()
        return CreatePost(post=post)

class UpdatePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        description = graphene.String()
        publish_date = graphene.Date()
        author = graphene.String()

    post = graphene.Field(PostType)

    def mutate(self, info, id, **kwargs):
        try:
            post = Post.objects.get(pk=id)
            for key, value in kwargs.items():
                setattr(post, key, value)
            post.save()
            return UpdatePost(post=post)
        except Post.DoesNotExist:
            return None

class CreateComment(graphene.Mutation):
    class Arguments:
        post_id = graphene.ID(required=True)
        text = graphene.String(required=True)
        author = graphene.String(required=True)

    comment = graphene.Field(CommentType)

    def mutate(self, info, post_id, text, author):
        try:
            post = Post.objects.get(pk=post_id)
            comment = Comment(post=post, text=text, author=author)
            comment.save()
            return CreateComment(comment=comment)
        except Post.DoesNotExist:
            return None

class DeleteComment(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    comment = graphene.Field(CommentType)

    def mutate(self, info, id):
        try:
            comment = Comment.objects.get(pk=id)
            comment.delete()
            return DeleteComment(comment=comment)
        except Comment.DoesNotExist:
            return None

class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)
    post = graphene.Field(PostType, id=graphene.ID(required=True))

    def resolve_all_posts(self, info):
        return Post.objects.all()

    def resolve_post(self, info, id):
        try:
            return Post.objects.get(pk=id)
        except Post.DoesNotExist:
            return None

class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    create_comment = CreateComment.Field()
    delete_comment = DeleteComment.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
