# accounts/validators.py
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class ComplexPasswordValidator:
    """
    Validates that password contains uppercase, lowercase, digits, and special characters.
    """
    def validate(self, password, user=None):
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        if not re.match(pattern, password):
            raise ValidationError(
                _("Password must contain at least one uppercase letter, one lowercase letter, "
                  "one number, and one special character (@$!%*?&)."),
                code='password_too_weak',
            )
    
    def get_help_text(self):
        return _(
            "Your password must contain at least one uppercase letter, one lowercase letter, one number, and one special character (@$!%*?&)."
        )