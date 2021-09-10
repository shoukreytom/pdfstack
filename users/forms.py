from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User


class AddUserForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email',)


class UpdateUserForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)
