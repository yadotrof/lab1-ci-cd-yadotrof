from .models import Person
from .serializers import PersonSerializer
from rest_framework import viewsets
from django.conf import settings
from rest_framework.reverse import reverse


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows various operations over persons.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get_success_headers(self, data):
        url = reverse("person-concrete", kwargs={"pk": data["id"]})
        return {'Location': f'https://{settings.URL}{url}'}
