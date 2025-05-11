from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from unittest.mock import patch

class ContactFreelancerAPITestCase(APITestCase):
    def setUp(self):
        # Define the URL for the contact freelancer API
        self.url = reverse('contact_freelancer')  # Ensure this is correct

    @patch('applications.send_email.send_email_via_brevo')  # Mock the email sending function
    def test_contact_form_submission(self, mock_send_email):
        # Prepare the data for the contact form
        data = {
            'subject': 'Test Subject',
            'message': 'Test Message',
            'freelancer_email': 'brozgamers@hotmail.com',
        }

        # Mock the email sending function to just pass without actually sending an email
        mock_send_email.return_value = None

        # Make the POST request to the contact form API (no need for authentication now)
        response = self.client.post(self.url, data)

        # Assert that the status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the success message is in the response content
        self.assertIn(b'Message sent successfully!', response.content)

        # Assert that the email sending function was called with the correct arguments
        mock_send_email.assert_called_with('Test Subject', 'Test Message', 'brozgamers@hotmail.com')
