import django_filters
from .models import productForArt

class productForArtFilters(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    titleFiltrt = django_filters.Filter(field_name='title',lookup_expr='icontains')
    class Meta:
        model = productForArt
        fields = ['min_price', 'max_price', 'titleFiltrt']