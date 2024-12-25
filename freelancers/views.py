from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Freelancer
from .serializers import FreelanceSerializer


class FreelanceList(APIView):
    def get(self, request):
        freelancers = Freelancer.objects.all() 
        serializers = FreelanceSerializer(freelancers, many=True)
        return Response(serializers.data)


class FreelancerDetail(APIView):
    serializer_class = FreelanceSerializer
    def get_object(self, pk):
        try:
            return Freelancer.objects.get(pk=pk)
        except Freelancer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        freelancer = self.get_object(pk)
        serializer = FreelanceSerializer(freelancer)
        return Response(serializer.data)

    def put(self, request, pk):
        freelancer = self.get_object(pk)
        serializer = FreelanceSerializer(freelancer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
