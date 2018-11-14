from django.contrib.auth.backends import RemoteUserBackend


class MyRemoteUserBackend(RemoteUserBackend):
    def clean_username(self, username):
        return username.split('\\')[1]
