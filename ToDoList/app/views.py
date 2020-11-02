from django.urls import reverse_lazy
from django.views import generic
from .models import Category, ToDo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

class IndexView(generic.ListView):
    model = ToDo

class DetailView(generic.DetailView):
    model = ToDo

class CreateView(LoginRequiredMixin, generic.CreateView):
    model = ToDo
    fields = ['name', 'content', 'date','category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)

class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = ToDo
    fields = ['name', 'content', 'date','category']

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('You do not have permission to edit.')
        return super(UpdateView, self).dispatch(request, *args, **kwargs)

class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = ToDo
    success_url = reverse_lazy('toDoList:index')
