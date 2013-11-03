import logging

from crispy_forms.bootstrap import PrependedText, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

from userena.forms import EditProfileForm, SignupFormOnlyEmail, AuthenticationForm
from userena.utils import get_profile_model

class SignInForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal form-signin'
        self.helper.form_method = 'post'
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            PrependedText('identification', '<span class="glyphicon glyphicon-user"></span>', active=True, placeholder="Email", autofocus='autofocus'),
            PrependedText('password', '<span class="glyphicon glyphicon-lock"></span>', active=True, placeholder="Password"),
            FormActions(
                Submit('submit', 'Sign in', css_class='btn btn-lg btn-primary btn-block'),
            )
        )
        super(SignInForm, self).__init__(*args, **kwargs)

class SignupFormOnePassword(SignupFormOnlyEmail):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal form-signin'
        self.helper.form_method = 'post'
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            PrependedText('email', '<span class="glyphicon glyphicon-user"></span>', active=True, placeholder="Email", autofocus='autofocus'),
            PrependedText('password1', '<span class="glyphicon glyphicon-lock"></span>', active=True, placeholder="Create Password"),
            PrependedText('password2', '<span class="glyphicon glyphicon-lock"></span>', active=True, placeholder="Repeat Password"),
            FormActions(
                Submit('submit', 'Signup', css_class='btn btn-lg btn-primary btn-block'),
            )
        )
        super(SignupFormOnePassword, self).__init__(*args, **kwargs)

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
            Field('first_name', placeholder="First Name", autofocus='autofocus'),
            Field('last_name', placeholder="Last Name"),
            Field('gender'),
            Field('birth_date'),
            Field('affiliation'),
            Field('affil_other'),
            Field('student_num'),
            Field('phone_num'),
            Field('year_of_study'),
            Field('faculty'),
            Field('other_faculty'),
            Field('major'),
            Field('graduating'),
            Field('nut_allergy'),
            Field('vegan'),
            Field('vegetarian'),
            Field('gluten'),
            Field('lactose'),
            Field('diet'),
            Field('times_participation'),
            Field('hear'),
            FormActions(
                Submit('submit', 'Submit', css_class='btn btn-lg btn-primary btn-block'),
            )
        )
        super(EditProfileFormExtra, self).__init__(*args, **kwargs)
    
    def save(self, force_insert=False, force_update=False, commit=True):
        profile = super(EditProfileFormExtra, self).save(commit=commit)
        logger = logging.getLogger(__name__)
        logger.error("MADE IT hERE")
        profile.check_payment_groups()

        return profile
