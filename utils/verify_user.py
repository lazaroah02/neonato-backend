from django.contrib.auth import get_user_model
CustomUser = get_user_model()

def verify_user(username):
    created_user = CustomUser.objects.get(username = username)
    created_user.status.verified = True
    created_user.status.save()