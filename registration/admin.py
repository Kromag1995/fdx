"Forms for creation of new users, editing existing ones and admins config"
from django import forms
from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

#admin.site.register(User)

from .models import CustomUser

class UserCreationForm(forms.ModelForm):
    """A form for creation of new users"""
    username = forms.CharField(label='Username', max_length=200)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_conf = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    email = forms.EmailField()
    def clean(self):
        cleaned_data = super().clean()
        password_1 = cleaned_data.get('password')
        password_2 = cleaned_data.get('password_conf')
        if password_1 != password_2:
            raise forms.ValidationError(("The passwords doenst match"), code='passwords')
        username = cleaned_data.get('username')
        try:
            if User.objects.get(username=username):
                raise forms.ValidationError("The username is taken", code='username')
        except:
            pass
        email = cleaned_data.get('email')
        try:
            if User.objects.get(email=email):
                raise forms.ValidationError("The email is alredy register, you\
         forgot your password?", code='email')
        except:
            pass
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
class UserChangeForm(forms.ModelForm):
    """A form for updating users.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser()
        fields = ('email', 'password', 'username', 'is_admin')


class UserAdmin(BaseUserAdmin):
    "Form to add and change user instances"
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'username', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(CustomUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
