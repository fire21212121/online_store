from django.shortcuts import render, redirect
from .forms import ProfileForm, UserForm, UserRegistrationForm
from django.views import View
from .models import Profile
from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from django.urls import reverse_lazy

User = get_user_model()

    # def profile(request):
    #     form = ProfileForm()
    #     user_form = UserForm()
    #     return render(request, 'accounts/profile.html', context = {'form': form, 'user_form': user_form]})

class ProfileView(View):
    def get(self, request, user_name):
        user = User.objects.get(username=user_name)
        profile = Profile.objects.get(user = user.pk)
        form = ProfileForm(instance=profile)
        user_form = UserForm(instance=user)
        uploaded_image = profile.image
        print(uploaded_image, 1111)
        return render(request, 'accounts/profile.html', context = {'form': form, 'user_form': user_form, 'uploaded_image':uploaded_image})

    def post(self, request, user_name):
        user = User.objects.get(username=user_name)
        profile = Profile.objects.get(user = user.pk)
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        user_form = UserForm(request.POST, instance=user)
        uploaded_image = profile.image
        if user_form.is_valid() and form.is_valid():
            form.save()
            user_form.save()
            return redirect("index")
        return render(request, 'accounts/profile.html', context = {'form': form, 'user_form': user_form, 'uploaded_image':uploaded_image})

class UserRegistrationView(CreateView):
    template_name = 'accounts/user_registration.html'
    success_url = reverse_lazy('login')
    form_class = UserRegistrationForm
    def form_valid(self, form):
        responce = super().form_valid(form)
        Profile.objects.create(user=self.object)
        return responce

def user_registration_view_done(request):
    return render(request, 'accounts/user_registration_done.html')
