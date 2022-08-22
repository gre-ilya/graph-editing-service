from django.shortcuts import render
from neomodel import StructuredNode, StringProperty, DateProperty

class Book(StructuredNode):
    title = StringProperty(unique_index=True)
    published = DateProperty()

b = Book(title="qwe").save()

# Create your views here.
