
from django.test import TestCase
from .forms import RegistrationForm
from django.contrib.auth.models import User
# Create your mytest here.

class RegistrationFormTestCase(TestCase):
    def test_form_fields(self):
        form_data = {'first_name': 'Joey', 'last_name': 'Tribbiani',
                     'username': 'joeyT', 'email': 'joeyT@gmail.com',
                     'phone_number': '1234567891', 'password1': 'pass@1234',
                     'password2': 'pass@1234'}

        form = RegistrationForm(data=form_data)
        if form.errors:
            for field in form:
                for error in field.errors:
                    print(field.label, error)
        self.assertTrue(form.is_valid())

    def test_invalid_email(self):
        form_data = {'first_name': 'Joey', 'last_name': 'Tribbiani',
                     'Username': 'joeyT', 'email': 'joeymail.com',
                     'phone_number': '1234567891', 'password1': 'pass@1234',
                     'password2': 'pass@1234'}

        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_username(self):
        form_data = {'first_name': 'Joey', 'last_name': 'Tribbiani',
                     'Username': 'joeyT', 'email': 'joeymail@gmail.com',
                     'phone_number': '1234567891', 'password1': 'pass@1234',
                     'password2': 'pass@1234'}

        User.objects.create_user(username='joeyT', email='joeymail@gmail.com')
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_blank_field(self):
        form_data = {'first_name': '', 'last_name': 'Tribbiani',
                     'Username': 'joeyT', 'email': 'joeymail.com',
                     'phone_number': '1234567891', 'password1': 'pass@1234',
                     'password2': 'pass@1234'}

        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())




