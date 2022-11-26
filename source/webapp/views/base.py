
from django.views.generic import ListView
from webapp.models import Photo



class IndexView(ListView):
    template_name = 'index.html'
    model = Photo
    context_object_name = 'photos'
    ordering = ('-created_at',)
