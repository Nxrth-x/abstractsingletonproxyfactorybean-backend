import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
        ]


class RegisterMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        password = graphene.String(required=True)

    username = graphene.String(required=True)
    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, username, first_name, last_name, password):
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )

        user.save()

        return RegisterMutation(
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
        )