from rest_framework import serializers
from .models import Candidate, Recruiter, Offer


class CandidateSerializer(serializers.ModelSerializer):
    applied_offers = serializers.PrimaryKeyRelatedField(
        many=True, 
        queryset=Offer.objects.all(), 
        required=False
    )

    class Meta:
        model = Candidate
        fields = '__all__'


class RecruiterSerializer(serializers.ModelSerializer):
    posted_offers = serializers.PrimaryKeyRelatedField(
        many=True, 
        queryset=Offer.objects.all(), 
        required=False
    )

    class Meta:
        model = Recruiter
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    candidate = CandidateSerializer(read_only=True)  
    recruiter = RecruiterSerializer(read_only=True)  
    candidate_id = serializers.PrimaryKeyRelatedField(
        queryset=Candidate.objects.all(), 
        write_only=True
    )
    recruiter_id = serializers.PrimaryKeyRelatedField(
        queryset=Recruiter.objects.all(), 
        write_only=True
    )

    class Meta:
        model = Offer
        fields = '__all__'
