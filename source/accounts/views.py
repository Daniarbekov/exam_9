from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from accounts.forms import UserRegistrationForm


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserRegistrationForm
    success_url= '/'
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        context = {}
        context['form'] = form
        return self.render_to_response(context)
