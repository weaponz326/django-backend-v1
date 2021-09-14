from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        user.first_name = request.data.get('first_name')
        user.last_name = request.data.get('last_name')
        user.location = request.data.get('location')
        user.about = request.data.get('about')
        user.save()

        return user
