from django.contrib.auth import get_user_model


class PhoneAuthBackend:
    def authenticate(self, request, username=None, password=None):
        try:
            user = get_user_model().objects.get(phone=username)
            if user.check_password(password):  # type: ignore
                return user
            return None

        except (
            get_user_model().DoesNotExist,
            get_user_model().MultipleObjectsReturned,
        ):
            return None

    def get_user(self, uid):
        try:
            return get_user_model().objects.get(pk=uid)
        except:
            return None
