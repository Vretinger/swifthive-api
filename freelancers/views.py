from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Freelancer
from .serializers import FreelanceSerializer
from swifthive_api.permissions import IsOwnerOrReadOnly


class FreelanceList(APIView):
    def get(self, request):
        freelancers = Freelancer.objects.all() 
        serializers = FreelanceSerializer(
            freelancers, many=True
        )
        return Response(serializers.data)


class FreelancerDetail(APIView):
    def get_object(self, pk):
        try:
            freelancers = Freelancer.objects.get(pk=pk) 
            return freelancers
        except Freelancer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        freelancer = self.get_object(pk)
        serializer = FreelanceSerializer(
            freelancer
        )
        return Response(serializer.data)

    def put(self, request, pk):
        freelancer = self.get_object(pk)
        serializer = FreelanceSerializer(
            freelancer, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
