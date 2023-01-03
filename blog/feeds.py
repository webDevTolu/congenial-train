import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from .models import Post


class LatestBlogFeed(Feed):
    title = 'techBlog'
    link = reverse_lazy('blog:post_list')
    description = ' Latest blogs of techBlog '

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords_html(markdown.markdown(item.body), 30)

    def item_publish_date(self, item):
        return item.publish
