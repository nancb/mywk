
from django import forms

from user.models import User, Card


class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=100,
                               widget=forms.PasswordInput,
                               label='用户密码')

    class Meta:
        model = User
        fields = '__all__'

class CardForm(forms.ModelForm):
    cardPwd = forms.CharField(max_length=100,
                              widget=forms.PasswordInput,
                              label= '支付密码')

    class Meta:
        model = Card
        fields = '__all__'