from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileEditForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Profile
from quiz.models import Quiz, Result


# view SignUpView based on class
# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('dashboard')
#     template_name = 'registration/signup.html'


# view SignUpViewbased on function
def SignUpView(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            profile = Profile.objects.create(user=user)
            print(profile)
            return redirect('login')
    else:
        user_form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': user_form})


@login_required
def profile(request):
    quizzes = Quiz.objects.filter(owner=request.user.profile)
    results = Result.objects.filter(user=request.user.profile)
    return render(request, 'profile.html', {'quizzes': quizzes, 'results': results})


@login_required
def edit_photo(request):
    if request.method == 'POST':
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
        return redirect('profile')
    else:
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request, 'edit_photo.html', {'profile_form': profile_form})