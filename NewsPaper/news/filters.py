from django_filters import FilterSet  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {'post_author__author__username': ['icontains'],
                  'news_title': ['icontains'],
                  'news_rating': ['gt'],
                  'create_time': ['gt']}


