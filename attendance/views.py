from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Attendance
from django.contrib.auth.models import User


@api_view(['POST'])
def mark_attendance(request):
    card_id = request.data.get('card_id')
    print(card_id)
    try:
        employee = User.objects.get(username=card_id)
        Attendance.objects.create(employee=employee)
        return Response({"status": "success", "message": "ba movafaghiyat anjam shod!"})
    except User.DoesNotExist:
        return Response({"status": "error", "message": "user peyda nashod"}, status=404)

