from django.urls import reverse_lazy

from .forms import WordForm
from .logic import count_words
from django.contrib import messages
from django.views.generic import TemplateView, FormView


class HomeView(FormView):
    template_name = "wordcounter/home.html"
    form_class = WordForm
    success_url = reverse_lazy('wordcount:home-form')

    def form_valid(self, form):
        self.count_words(form.cleaned_data)
        return super().form_valid(form)

    def count_words(self, valid_data):
        words = count_words(valid_data["message"])
        messages.success(self.request, f"The number of words in the provided message is {words}.")


class AboutView(TemplateView):
    template_name = "wordcounter/about.html"
