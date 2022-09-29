
from django.forms import ModelForm
from captcha.fields import CaptchaField

from django.contrib.auth import get_user_model
User = get_user_model()

from django.contrib.auth import authenticate, login

class LoginModelForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = User
        fields = ['username','password']

    def clean(self):
        cleaned_data = self.cleaned_data
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            self.add_error('username','نـام کاربـری یا رمـز عـبور اشـتباه اسـت')
        elif user.is_staff == False:
            self.add_error('username', 'User is not admin (super user) !')
        return cleaned_data