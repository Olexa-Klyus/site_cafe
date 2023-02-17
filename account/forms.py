# from django import forms
# from django.contrib.auth import get_user_model, authenticate
#
# # доступу напряму до моделі користувачів у нас немає
# # доступ тільки через функцію get_user_model
#
# User = get_user_model()
#
#
# # форма для логінації не має моделі
# class UserLogin(forms.Form):
#     username = forms.CharField(widget=forms.TextInput())
#     password = forms.CharField(widget=forms.PasswordInput())
#
#     def clean(self):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')
#
#         if username and password:
#             user = authenticate(username=username, password=password)
#             if not user or not user.check_password(password):
#                 raise forms.ValidationError('Error in Login or Password')
#         else:
#             raise forms.ValidationError('Error in Login or Password')
#
#         return super().clean()
#
#
# # форма для реєстрації привязана до вбудованої моделі User,
# class UserRegistration(forms.ModelForm):
#     # пароль і логін в базі зберігаються в різних таблицях
#     # до пароля ми доступу не маємо
#     class Meta:
#         model = User
#         fields = ('username',)
#
#     username = forms.CharField(widget=forms.TextInput())
#     password = forms.CharField(widget=forms.PasswordInput())
#     password2 = forms.CharField(widget=forms.PasswordInput())
#
#     # інформацію яка буде в POST запиті можна витягнути
#     # за допомогою метода clean
#     # дані попадуть в словник cleaned_data
#     def clean_password2(self):
#         data = self.cleaned_data
#         if data.get('password') == data.get('password2'):
#             return data['password2']
#         raise forms.ValidationError('Error in password')
