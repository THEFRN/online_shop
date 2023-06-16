from django.views import generic
from django.urls import reverse_lazy

from .forms import UserCreationForm


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/sign_up.html'
    success_url = reverse_lazy('home')
