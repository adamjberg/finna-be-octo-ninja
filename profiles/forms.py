import logging

from django import forms

from crispy_forms.bootstrap import PrependedText, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

from userena.forms import EditProfileForm, SignupForm, AuthenticationForm
from userena.utils import get_profile_model

from profiles.models import *

class SignInForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal form-signin'
        self.helper.form_method = 'post'
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            PrependedText('identification', '<span class="glyphicon glyphicon-user"></span>', active=True, placeholder="Username or Email", autofocus='autofocus'),
            PrependedText('password', '<span class="glyphicon glyphicon-lock"></span>', placeholder="Password"),
            FormActions(
                Submit('submit', 'Sign in', css_class='btn btn-lg btn-primary btn-block'),
            )
        )
        super(SignInForm, self).__init__(*args, **kwargs)

class SignupFormCrispy(SignupForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal form-signin'
        self.helper.form_method = 'post'
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            PrependedText('username', '<span class="glyphicon glyphicon-user"></span>', active=True, placeholder="Username", autofocus='autofocus'),
            PrependedText('email', '<span class="glyphicon glyphicon-user"></span>', placeholder="Email"),
            PrependedText('password1', '<span class="glyphicon glyphicon-lock"></span>', placeholder="Create Password"),
            PrependedText('password2', '<span class="glyphicon glyphicon-lock"></span>', placeholder="Repeat Password"),
            FormActions(
                Submit('submit', 'Sign up', css_class='btn btn-lg btn-primary btn-block'),
            )
        )
        super(SignupFormCrispy, self).__init__(*args, **kwargs)

class EditProfileFormExtra(EditProfileForm):
    class Meta:
        model = get_profile_model()
        exclude = ['user', 'mugshot', 'privacy', 'paid', 'saved_sessions']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.help_text_inline = True
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Field('first_name', placeholder="First Name", autofocus='autofocus', required=True),
            Field('last_name', placeholder="Last Name", required=True),
            Field('affiliation', required=True),
            Field('affil_other'),
            Field('student_num'),
            Field('phone_num', required=True),
            Field('year_of_study'),
            Field('faculty'),
            Field('major'),
            Field('vegan'),
            Field('vegetarian'),
            Field('diet'),
            Field('times_participation'),
            Field('hear'),
            FormActions(
                Submit('submit', 'Submit', css_class='btn btn-lg btn-primary center-block'),
            )
        )
        super(EditProfileFormExtra, self).__init__(*args, **kwargs)
    
    def clean(self):
        cleaned_data = super(EditProfileFormExtra, self).clean()
        if cleaned_data.get('affiliation') in (UBC_STUDENT, UBC_STAFF, UBC_ALUMNI, UBC_FACULTY):
            if len(cleaned_data.get('student_num', "")) != 8:
                raise forms.ValidationError("Please enter a valid student number")
        return cleaned_data
    
    def save(self, force_insert=False, force_update=False, commit=True):
        profile = super(EditProfileFormExtra, self).save(commit=commit)
        profile.check_payment_groups()

        return profile
