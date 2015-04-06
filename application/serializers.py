from marshmallow import Serializer, fields


class UserSerializer(Serializer):
    class Meta:
        fields = ("id", "email", "last_sync")


class BookSerializer(Serializer):
    user = fields.Nested(UserSerializer)

    class Meta:
        fields = ("id", "guid", "title", "user", "date_created", "last_sync")


class NoteSerializer(Serializer):
    book = fields.Nested(BookSerializer)

    class Meta:
        fields = ("id", "guid", "title", "body", "date_created", "date_updated", "last_sync")