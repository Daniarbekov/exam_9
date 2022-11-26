from django.views.generic import  CreateView
from webapp.forms import PhotoForm
from webapp.models import Photo


class PhotoCreate(CreateView):
    template_name = 'add_photo.html'
    form_class = PhotoForm
    model = Photo
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)