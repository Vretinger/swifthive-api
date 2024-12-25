from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Freelancer
from .serializers import FreelanceSerializer


class FreelanceList(APIView):
    def get(self, request):
        freelancer = Freelancer.objects.all()
        serializers = FreelanceSerializer(freelancer, many=True)
        return Response(serializers.data)