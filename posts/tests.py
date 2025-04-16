from django.test import TestCase
from django.urls import reverse
from .models import Post
from faker import Faker
fake = Faker()

class FirstTestCase(TestCase):
    def setUp(self):
        print("Setup Done!!")
    
    def test_first_case(self):
        self.assertEqual(1,1)

    def test_post_case(self):
        Post.objects.create(title = fake.text, body = fake.texts)

class PostModelTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title="Test Title", body="Test Body")
    
    def test_post_content(self):
        self.assertEqual(self.post.title, "Test Title")
        self.assertEqual(self.post.body, "Test Body")

class PostViewTest(TestCase):
    def test_home_view_status_code_and_template(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

class IntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('homepage')  # Replace 'homepage' with your actual URL name

    def test_homepage_view(self):
        # Test that the homepage loads correctly
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_login_logout_flow(self):
        # Create a test user
        user = User.objects.create_user(username='testuser', password='testpass')
        
        # Simulate a login POST request
        login_response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(login_response.status_code, 302)  # Expect a redirection after login

        # Simulate a logout request
        logout_response = self.client.get(reverse('logout'))
        self.assertEqual(logout_response.status_code, 200)
        self.assertContains(logout_response, "Logged Out Successfully.")