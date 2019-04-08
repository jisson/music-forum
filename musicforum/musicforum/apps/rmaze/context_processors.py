from django.conf import settings


def rmaze_dsn(request):
    return {
        'RMAZE_DSN': settings.RMAZE_DSN,
        'RMAZE_CLIENT_URL': settings.RMAZE_CLIENT_URL,
    }
