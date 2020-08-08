import django_filters
from .models import Job


class JobFiltter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr = 'icontains')
    description = django_filters.CharFilter(lookup_expr = 'icontains')

    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['job_owner','image','slug']