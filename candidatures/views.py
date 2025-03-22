from rest_framework import viewsets
from .models import Candidate, Recruiter, Offer
from .serializers import CandidateSerializer, RecruiterSerializer, OfferSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        experience = self.request.query_params.get('experience', None)
        email = self.request.query_params.get('email', None)

        if experience:
            queryset = queryset.filter(experience__icontains=experience)
        if email:
            queryset = queryset.filter(email=email)

        return queryset


class RecruiterViewSet(viewsets.ModelViewSet):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        recruiter_id = self.request.query_params.get('recruiter_id', None)
        candidate_id = self.request.query_params.get('candidate_id', None)

        if recruiter_id:
            queryset = queryset.filter(recruiter_id=recruiter_id)
        if candidate_id:
            queryset = queryset.filter(candidate_id=candidate_id)

        return queryset
