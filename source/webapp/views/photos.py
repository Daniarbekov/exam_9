from django.views.generic import  CreateView, DetailView, UpdateView, DeleteView
from webapp.forms import PhotoForm
from webapp.models import Photo
from django.urls import reverse_lazy


class PhotoCreate(CreateView):
    template_name = 'add_photo.html'
    form_class = PhotoForm
    model = Photo
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PhotoView(DetailView):
    template_name = 'photo_detail.html'
    model = Photo


class PhotoUpdateView(UpdateView):
    template_name = 'photo_update.html'
    form_class = PhotoForm
    model = Photo
    context_object_name = 'photo'
    

class PhotoDeleteView(DeleteView):
    template_name = 'photo_delete.html'
    model = Photo
    success_url = reverse_lazy('index')
