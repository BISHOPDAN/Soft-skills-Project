from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import Blog
from faq.models import FAQ
from tutor.models import Tutor


class BlogSitemap(Sitemap):
    def items(self):
        return Blog.objects.all()


class FAQSitemap(Sitemap):
    def items(self):
        return FAQ.objects.all()

    def location(self, item):
        return reverse('faq:index')


class TutorSitemap(Sitemap):
    def items(self):
        return Tutor.objects.all()

    def location(self, item):
        return reverse('tutor:index')


class StaticViewSitemap(Sitemap):
    def items(self):
        return [
            'home:about-us',
            'home:index',
            'home:contact-us',
            'home:terms-of-use']

    def location(self, item):
        return reverse(item)
