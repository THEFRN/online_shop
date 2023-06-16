from django.test import TestCase
from django.urls import reverse


class TestPages(TestCase):
    # Home Page Tests -----------------------------------------------
    def test_home_page_view_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_view_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_view_containments(self):
        response = self.client.get('/')
        self.assertContains(response, 'Home Page')

    # About Us Page Tests -----------------------------------------------
    def test_about_us_view_url(self):
        response = self.client.get('/aboutus/')
        self.assertEqual(response.status_code, 200)

    def test_about_us_view_url_by_name(self):
        response = self.client.get(reverse('about_us'))
        self.assertEqual(response.status_code, 200)

    def test_about_us_view_template(self):
        response = self.client.get('/aboutus/')
        self.assertTemplateUsed(response, 'pages/aboutus.html')

    def test_about_us_view_containments(self):
        response = self.client.get('/aboutus/')
        self.assertContains(response, 'About Us Page')

