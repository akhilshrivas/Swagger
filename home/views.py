from rest_framework.views import APIView
from rest_framework.response import Response

class TestAPIView(APIView):  # <--- Note the name here
    def get(self, request):
        return Response({"message": "API is live!"})
    # In home/views.py
class TestView(APIView):
    def get(self, request):
        return Response({"message": "Fetching data..."})

    def post(self, request):
        username = request.data.get("username")
        return Response({"message": f"User {username} created!"}, status=201)