from django import forms
from django.contrib.auth.models import User
from .models import Item, Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'phone_number', 'address']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'ПІБ'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Номер телефону'}),
            'address': forms.Textarea(attrs={'placeholder': 'Місце проживання', 'rows': 3}),
        }


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'price', 'sizes', 'type', 'gender']


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        label='Username',
        error_messages={'required': 'This field is required'}
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        label='Password',
        error_messages={'required': 'This field is required'}
    )


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords don't match")

        return password_confirm

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
