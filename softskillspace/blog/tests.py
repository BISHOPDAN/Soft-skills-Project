import shutil

from django.test import TestCase, override_settings
from django.urls import reverse_lazy

from blog.models import Blog, BlogImage, Category
from softskillspace.base_settings import BASE_DIR
from softskillspace.utils.tests import create_user, generate_image_file

TEST_DIR = f"{BASE_DIR}/softskillspace/uploads/test_data"


class BlogTest(TestCase):
    @classmethod
    def tearDown(cls):
        """
        run this setup after all test has finished running
        """
        try:
            shutil.rmtree(TEST_DIR)
        except OSError:
            pass

    @classmethod
    @override_settings(MEDIA_ROOT=(TEST_DIR + '/media'))
    def setUpTestData(cls):
        """
        run this setup before any test
        """
        create_user(cls)

        cls.category = Category.objects.create(
            name='news'
        )

        cls.blog = Blog.objects.create(
            name="test blog",
            content="test blog content",
            category=cls.category,
            author=cls.user,
        )

        BlogImage.objects.create(
            blog=cls.blog,
            image=generate_image_file("test_image.jpg")
        )

    def test_blog_list_page_loads_successfully(self):
        """
        Test that the blog list page loads successfully
        """
        res = self.client.get(reverse_lazy("blog:index"))
        self.assertEqual(res.status_code, 200)

    def test_blog_detail_page_loads_successfully(self):
        """
        Test that the blog detail page loads successfully
        """
        res = self.client.get(reverse_lazy(
            "blog:detail", args=[self.blog.slug]))
        self.assertEqual(res.status_code, 200)

    def test_new_blog_has_no_image_returns_default_image(self):
        """
        Test that the new blog has no image returns the default image
        """

        blog = Blog.objects.create(
            name="test blog 2",
            content="test blog content 2",
            category=self.category,
            author=self.user,
        )

        self.assertEqual(
            blog.image_url, "/assets/images/avatar/blog_placeholder.png")

    def test_blog_category_page_functions_correctly(self):
        """
        Test that the blog category page functions correctly
        """
        res = self.client.get(reverse_lazy(
            "blog:category", args=[self.category]))
        self.assertEqual(res.status_code, 200)
