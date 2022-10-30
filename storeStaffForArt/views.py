
from django.views import View, generic
from .models import productForArt
from django.shortcuts import render
from .filters import productForArtFilters
from django.core.paginator import Paginator
# Create your views here.
class startPage(generic.ListView):
    model = productForArt
    paginate_by = 2
    template_name = "startPage.html"
    context_object_name = "productForArt_list"
    queryset = productForArt.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filter'] = productForArtFilters(self.request.GET,queryset=self.get_queryset())
        return context
    def get_queryset(self):
        queryset = super().get_queryset()
        return productForArtFilters(self.request.GET, queryset=queryset).qs

class productForArtDetalsview(generic.DeleteView):
    model = productForArt
    template_name = "ProductCard.html"

def pageInwork(request, *args, **kwargs):
    return  render(request, "pageInwork.html", {})
