from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# view based on class
# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('dashboard')
#     template_name = 'registration/signup.html'

# view based on function

def SignUpView(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            return redirect('login')
    else:
        user_form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': user_form})


@login_required
def profile(request):
    return render(request, 'profile.html')
