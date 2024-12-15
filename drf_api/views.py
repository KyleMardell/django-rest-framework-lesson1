from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings  # Import settings instead of individual variables


@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to my drf API!"
    })


# dj-rest-auth logout view fix
@api_view(['POST'])
def logout_route(request):
    response = Response()
    response.set_cookie(
        key=settings.REST_AUTH['JWT_AUTH_COOKIE'],  # Access dictionary keys properly
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=settings.REST_AUTH['JWT_AUTH_SAMESITE'],  # Same here
        secure=getattr(settings, 'JWT_AUTH_SECURE', False),  # Handle `JWT_AUTH_SECURE` dynamically
    )
    response.set_cookie(
        key=settings.REST_AUTH['JWT_AUTH_REFRESH_COOKIE'],  # Same fix
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=settings.REST_AUTH['JWT_AUTH_SAMESITE'],
        secure=getattr(settings, 'JWT_AUTH_SECURE', False),
    )
    return response
