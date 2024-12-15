from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings  # Import settings instead of individual variables


@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to my drf API!"
    })


@api_view(['POST'])
def logout_route(request):
    response = Response()
    response.set_cookie(
        key=settings.REST_AUTH['JWT_AUTH_COOKIE'],
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=settings.REST_AUTH['JWT_AUTH_SAMESITE'],
        secure=getattr(settings, 'JWT_AUTH_SECURE', False),
    )
    response.set_cookie(
        key=settings.REST_AUTH['JWT_AUTH_REFRESH_COOKIE'],
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=settings.REST_AUTH['JWT_AUTH_SAMESITE'],
        secure=getattr(settings, 'JWT_AUTH_SECURE', False),
    )
    return response
