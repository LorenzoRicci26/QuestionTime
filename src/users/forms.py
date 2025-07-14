from django_registration.forms import RegistrationForm
from users.models import CustomUser

class CustomUserRegistrationForm(RegistrationForm):
    """
    Custom registration form for the CustomUser model.
    This can be extended to include additional fields if necessary.
    """
    class Meta(RegistrationForm.Meta):
        model = CustomUser