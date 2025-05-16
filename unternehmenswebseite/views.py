from django.http import JsonResponse
from django.db import connection

def db_status(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return JsonResponse({"db_status": "ok"})
    except Exception as e:
        return JsonResponse({"db_status": "error", "details": str(e)}, status=500)
