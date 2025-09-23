from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Application, Interaction
from .forms import InteractionForm
from .models import Tag
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


class Home(LoginView):
    template_name = 'home.html'
    redirect_authenticated_user = True

@login_required
def about(request):
    return render(request, 'about.html')


class ApplicationList(LoginRequiredMixin, ListView):
    model = Application
    template_name = 'applications/index.html'
    context_object_name = 'applications'
    ordering = ['-applied_date']

class ApplicationDetail(LoginRequiredMixin, DetailView):
    model = Application
    template_name = 'applications/detail.html'
    context_object_name = 'app'   

class ApplicationCreate(LoginRequiredMixin, CreateView):
    model = Application
    fields = ['company', 'position', 'description', 'status', 'applied_date']
    template_name = 'main_app/application_form.html'  

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Application created ✅")
        return super().form_valid(form)


class ApplicationUpdate(LoginRequiredMixin, UpdateView):
    model = Application
    fields = ['position', 'description', 'status', 'applied_date']
    template_name = 'main_app/application_form.html' 

class ApplicationDelete(LoginRequiredMixin, DeleteView):
    model = Application
    template_name = 'main_app/application_confirm_delete.html'
    success_url = '/applications/'

@login_required
def add_interaction(request, pk):
    form = InteractionForm(request.POST)
    if form.is_valid():
        new_interaction = form.save(commit=False)
        new_interaction.application_id = pk
        new_interaction.save()
    return redirect('application-detail', pk=pk)

class TagCreate(LoginRequiredMixin, CreateView):
    model = Tag
    fields = '__all__'
    template_name = 'main_app/tag_form.html'

class TagList(LoginRequiredMixin, ListView):
    model = Tag
    template_name = 'main_app/tag_list.html'
    context_object_name = 'tag_list'

class TagDetail(LoginRequiredMixin, DetailView):
    model = Tag
    template_name = 'main_app/tag_detail.html'
    context_object_name = 'tag'

class TagUpdate(LoginRequiredMixin, UpdateView):
    model = Tag
    fields = ['name', 'color']
    template_name = 'main_app/tag_form.html'

class TagDelete(LoginRequiredMixin, DeleteView):
    model = Tag
    template_name = 'main_app/tag_confirm_delete.html'
    success_url = '/tags/'

@login_required
def app_detail(request, app_id):
    app = Application.objects.get(id=app_id)
    available_tags = Tag.objects.exclude(
        id__in=app.tags.all().values_list('id', flat=True)
    )

    return render(
        request,
        'applications/detail.html',
        {
            'app': app,
            'available_tags': available_tags
        }
    )

@login_required
def associate_tag(request, app_id, tag_id):
    Application.objects.get(id=app_id).tags.add(tag_id)
    return redirect('application-detail', app_id=app_id)

@login_required
def remove_tag(request, app_id, tag_id):
    Application.objects.get(id=app_id).tags.remove(tag_id)
    return redirect('application-detail', app_id=app_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('application-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form, 'error_message': error_message})







