from .models import Person
from .serializers import PersonSerializer
from rest_framework import viewsets

class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows various operations over persons.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
