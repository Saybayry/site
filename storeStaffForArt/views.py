
from django.views import View, generic
from .models import productForArt
from django.shortcuts import render
from .filters import productForArtFilters

# Create your views here.
class startPage(generic.ListView):
    model = productForArt
    template_name = "startPage.html"
    context_object_name = "productForArt_list"
##    queryset = productForArt.objects.all()[:20]
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filter'] = productForArtFilters(self.request.GET,queryset=self.get_queryset())
        return context

def pageInwork(request, *args, **kwargs):
    return  render(request, "pageInwork.html", {})
