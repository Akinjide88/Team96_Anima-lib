from django.contrib.auth.tokens import passwordResetTokenGeneration
from six import text_type

class TokenGenerator(passwordResetTokenGeneration):
    def _make_hash_value(self, user, timestamp):
        return(
            text_type(user.pk) + text_type(timestamp)
        )
    
generate_token = TokenGenrator()