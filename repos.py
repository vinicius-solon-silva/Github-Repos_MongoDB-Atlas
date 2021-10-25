from mongoengine import Document, StringField


class Repository(Document):
    git_user = StringField(max_length=255)
    repo_name = StringField(max_length=255)
    URL = StringField(max_length=255)
