from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()


@register.simple_tag
def total_blogs():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_blogs(count=5):
    latest_blogs = Post.published.order_by('-publish')[:count]
    return {'latest_blogs': latest_blogs}


@register.simple_tag
def get_most_commented_blogs(count=5):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
