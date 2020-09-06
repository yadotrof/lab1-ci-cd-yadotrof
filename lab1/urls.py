"""
lab1 URL Configuration.
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
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
    path('swagger-ui/', TemplateView.as_view(
        template_name='person/swagger.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('openapi', get_schema_view(title="RSOI lab1",
                                    description="API for person",
                                    version="1.0.0"
                                    ), name='openapi-schema'),
    path('persons/', person_all, name='person-all'),
    path('persons/<int:pk>/', person_concrete, name='person-concrete'),
    path('admin/', admin.site.urls),
]
