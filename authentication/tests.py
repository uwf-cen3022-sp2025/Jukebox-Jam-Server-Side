from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from authentication.views import send_email_confirmation, email_confirm
from django.urls import reverse
from django.core import mail

class TestEmailConfirmation(TestCase):
    def setUserUp(self):
            """ Set up test user and Request Factory """
            self.factory = RequestFactory()
            self.user = User.objects.create_user(username="testUser", email="testemail@gmail.com", password="Test@12233")
            self.user.is_active=False
            self.user.save()


    def test_SendConfirmationEmail(self):
          """ Test if email is sent to the inbox of user email """
          request = self.factory.get('/')
          send_email_confirmation(request, self.user)

          #check email status
          self.assertEqual(len(mail.outbox), 1) # 1 means it was sent (or something was)
          self.assertIn("Confirm your Email", mail.outbox[0].subject) # the subject is correct
          self.assertIn("http://", mail.outbox[0].body) # checks the actual link

    def Test_view_emailConfirmation(self):
          """ Test if email confirmation """
          token = default_token_generator.make_token(self.user)
          uid = urlsafe_base64_encode(force_bytes(self.user.pk))

    # make the user get the confirmation email
          confirm_url = reverse('confirm_email', kwargs={'uidb64': uid, 'token': token})
          response = self.client.get(confirm_url)

        # refresh the database and activate user
          self.user.refresh_from_db()
          self.assertEqual(response.status_code, 302)
          # activate the user
          self.assertTrue(self.user.is_active) 