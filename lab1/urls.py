"""
lab1 URL Configuration.
"""
from django.contrib import admin
from django.urls import include, path
from lab1.person.views import PersonViewSet

person_all = PersonViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

person_concrete = PersonViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('persons/', person_all, name='person-all'),
    path('persons/<int:pk>/', person_concrete, name='person-concrete'),
    path('admin/', admin.site.urls),
]