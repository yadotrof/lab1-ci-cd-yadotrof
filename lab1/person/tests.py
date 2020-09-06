from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Person

class PersonTests(APITestCase):
    def test_create_person(self):
        """
        Ensure we can create a new person object.
        """
        url = reverse('person-all')
        data = {"name": "Test name",
                "age": 13,
                "address": "Test address",
                "work": "Test work"
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.get().name, 'Test name')
        self.assertEqual(Person.objects.get().age, 13)
        self.assertEqual(Person.objects.get().address, 'Test address')
        self.assertEqual(Person.objects.get().work, 'Test work')

    def test_create_person_bad_age(self):
        """
        Ensure we can not create a new person object with string age.
        """
        url = reverse('person-all')
        data = {"name": "Test name",
                "age": "SORRY",
                "address": "Test address",
                "work": "Test work"
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_person(self):
        """
        Ensure we can retrieve the person object.
        """
        url = reverse('person-all')
        data = {"name": "Test name",
                "age": 13,
                "address": "Test address",
                "work": "Test work"
                }
        self.client.post(url, data, format='json')
        url = reverse('person-concrete', kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test name')
        self.assertEqual(response.data['age'], 13)
        self.assertEqual(response.data['address'], 'Test address')
        self.assertEqual(response.data['work'], 'Test work')

    def test_retrieve_not_exists_person(self):
        """
        Ensure we can not retrieve not exists person object.
        """
        url = reverse('person-concrete', kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_retrieve_person_list(self):
        """
        Ensure we can retrieve person objects list.
        """
        url = reverse('person-all')
        data = {"name": "Test name",
                "age": 13,
                "address": "Test address",
                "work": "Test work"
                }
        self.client.post(url, data, format='json')
        self.client.post(url, data, format='json')
        url = reverse('person-all')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'Test name')
        self.assertEqual(response.data[0]['age'], 13)
        self.assertEqual(response.data[0]['address'], 'Test address')
        self.assertEqual(response.data[0]['work'], 'Test work')
        self.assertEqual(response.data[1]['name'], 'Test name')
        self.assertEqual(response.data[1]['age'], 13)
        self.assertEqual(response.data[1]['address'], 'Test address')
        self.assertEqual(response.data[1]['work'], 'Test work')


    def test_delete_person(self):
        """
        Ensure we can delete the person object.
        """
        url = reverse('person-all')
        data = {"name": "Test name",
                "age": 13,
                "address": "Test address",
                "work": "Test work"
                }
        self.client.post(url, data, format='json')
        url = reverse('person-concrete', kwargs={'pk': 1})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Person.objects.count(), 0)

    def test_delete_not_exists_person(self):
        """
        Ensure we can not delete not exists person object.
        """
        url = reverse('person-concrete', kwargs={'pk': 1})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_person(self):
        """
        Ensure we can patch the person object.
        """
        url = reverse('person-all')
        data = {"name": "Test name",
                "age": 13,
                "address": "Test address",
                "work": "Test work"
                }
        self.client.post(url, data, format='json')
        url = reverse('person-concrete', kwargs={'pk': 1})
        data = {"name": "Name test",
                "age": 31,
                "address": "Address test",
                "work": "Work test"
                }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.get().name, 'Name test')
        self.assertEqual(Person.objects.get().age, 31)
        self.assertEqual(Person.objects.get().address, 'Address test')
        self.assertEqual(Person.objects.get().work, 'Work test')

    def test_patch_person_bad_age(self):
        """
        Ensure we can not patch the person object with bad age.
        """
        url = reverse('person-all')
        data = {"name": "Test name",
                "age": 13,
                "address": "Test address",
                "work": "Test work"
                }
        self.client.post(url, data, format='json')
        url = reverse('person-concrete', kwargs={'pk': 1})
        data = {"name": "Name test",
                "age": "SORRY",
                "address": "Address test",
                "work": "Work test"
                }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.get().name, 'Test name')
        self.assertEqual(Person.objects.get().age, 13)
        self.assertEqual(Person.objects.get().address, 'Test address')
        self.assertEqual(Person.objects.get().work, 'Test work')

    def test_patch_not_exists_person(self):
        """
        Ensure we can not patch not exists person object.
        """
        url = reverse('person-concrete', kwargs={'pk': 1})
        data = {"name": "Name test",
                "age": 31,
                "address": "Address test",
                "work": "Work test"
                }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
