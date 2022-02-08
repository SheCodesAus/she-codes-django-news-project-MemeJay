from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.shortcuts import render


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/createAccount.html'
    # def get_success_url(self):
    #     user=self.kwargs['pk']
    #     return reverse_lazy('users:userProfile', kwargs={'pk': user})

class ProfileView(generic.DetailView):
    model = CustomUser
    template_name = 'users/userProfile.html'
    context_object_name = 'user'

def get_current_user(request):
    user = request.user
    return render(request, 'users/userProfile.html', {"user":user})

# Create your views here.
