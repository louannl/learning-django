from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    '''
    our devsearch settings file comes here to UsersConfig to initialise,
    hence when we added the signal file we needed to 'activate' it by adding
    it here.
    '''

    def ready(self):
        import users.signals
