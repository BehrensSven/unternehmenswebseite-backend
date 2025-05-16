from django.urls import path
from django.http import JsonResponse
from django.contrib.auth.models import User

def test_db(request):
    users = list(User.objects.values("id", "username", "email"))
    return JsonResponse({"users": users})

urlpatterns = [
    path("test-db/", test_db),
]
