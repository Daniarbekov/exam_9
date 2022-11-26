from django.views.generic import  CreateView, DetailView, UpdateView, DeleteView
from webapp.forms import PhotoForm
from webapp.models import Photo
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import  UserPassesTestMixin, LoginRequiredMixin


class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.pk})


class PhotoCreate(LoginRequiredMixin,SuccessDetailUrlMixin,CreateView):
    template_name = 'add_photo.html'
    form_class = PhotoForm
    model = Photo
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PhotoView(DetailView):
    template_name = 'photo_detail.html'
    model = Photo


class PhotoUpdateView(UserPassesTestMixin, SuccessDetailUrlMixin,UpdateView):
    template_name = 'photo_update.html'
    form_class = PhotoForm
    model = Photo
    context_object_name = 'photo'
    
    def test_func(self):
        return self.get_object().author == self.request.user or self.request.user.has_perm('webapp.change_photo')
    

class PhotoDeleteView(UserPassesTestMixin,DeleteView):
    template_name = 'photo_delete.html'
    model = Photo
    success_url = reverse_lazy('index')

    def test_func(self):
        return self.get_object().author == self.request.user or self.request.user.has_perm('webapp.delete_photo')