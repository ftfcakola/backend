from rest_framework import serializers
from .models import (
    Membership, Player, CoachingStaff, Highlight, Gallery,
    StadiumTour, ContactMessage, ClubRegistration, AcademyEnrollment
)


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = '__all__'
        read_only_fields = ['date_joined']


class PlayerSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Player
        fields = '__all__'
        
    def get_age(self, obj):
        from datetime import date
        today = date.today()
        return today.year - obj.date_of_birth.year - (
            (today.month, today.day) < (obj.date_of_birth.month, obj.date_of_birth.day)
        )
    
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class CoachingStaffSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = CoachingStaff
        fields = '__all__'
        
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class HighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Highlight
        fields = '__all__'
        read_only_fields = ['views', 'created_at']


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'
        read_only_fields = ['created_at']


class StadiumTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = StadiumTour
        fields = '__all__'
        read_only_fields = ['booking_date']
        
    def validate_tour_date(self, value):
        from datetime import date
        if value < date.today():
            raise serializers.ValidationError("Tour date cannot be in the past.")
        return value


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'status']


class ClubRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubRegistration
        fields = '__all__'
        read_only_fields = ['registration_date', 'is_processed']


class AcademyEnrollmentSerializer(serializers.ModelSerializer):
    child_age = serializers.SerializerMethodField()
    
    class Meta:
        model = AcademyEnrollment
        fields = '__all__'
        read_only_fields = ['enrollment_date', 'is_approved']
        
    def get_child_age(self, obj):
        from datetime import date
        today = date.today()
        return today.year - obj.child_date_of_birth.year - (
            (today.month, today.day) < (obj.child_date_of_birth.month, obj.child_date_of_birth.day)
        )