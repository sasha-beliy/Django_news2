from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import News


class NewsList(ListView):
    model = News
    ordering = 'name'
    template_name = 'News.html'
    context_object_name = 'News'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_news'] = "Обновление ежедневно"
        return context

class NewsDetail(DetailView):
    model = News
    template_name = 'News.html'
    context_object_name = 'News'