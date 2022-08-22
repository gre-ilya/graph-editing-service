from django.db import models
from neomodel import StructuredNode, StringProperty, DateProperty

class Book(StructuredNode):
    title = StringProperty(unique_index=True)
    published = DateProperty()


# Create your models here.
