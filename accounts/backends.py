from django.contrib.auth.backends import ModelBackend
from .models import CustomUser


class MobileNumberBackend(ModelBackend):
    def _normalize(self, value: str) -> str:
        if not value:
            return ''
        digits = ''.join(ch for ch in value if ch.isdigit())
        return digits[-10:]

    def authenticate(self, request, mobile_number=None, password=None, **kwargs):
        if mobile_number is None or password is None:
            return None
        normalized = self._normalize(mobile_number)
        try:
            user = CustomUser.objects.get(mobile_number=normalized)
        except CustomUser.DoesNotExist:
            print(f"[Auth] No user with mobile: {normalized}")
            return None
        password_ok = user.check_password(password)
        can_auth = self.user_can_authenticate(user)
        print(f"[Auth] Found user id={user.id}, password_ok={password_ok}, can_auth={can_auth}")
        if password_ok and can_auth:
            return user
        return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None


