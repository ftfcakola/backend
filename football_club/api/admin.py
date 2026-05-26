from django.contrib import admin
from .models import (
    Membership, Player, CoachingStaff, Highlight, Gallery,
    StadiumTour, ContactMessage, ClubRegistration, AcademyEnrollment
)


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'membership_type', 'is_active', 'expiry_date']
    list_filter = ['membership_type', 'is_active', 'date_joined']
    search_fields = ['first_name', 'last_name', 'email']
    date_hierarchy = 'date_joined'


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['jersey_number', 'first_name', 'last_name', 'position', 'team_type', 'is_active']
    list_filter = ['position', 'team_type', 'is_active', 'nationality']
    search_fields = ['first_name', 'last_name', 'nationality']
    ordering = ['jersey_number']


@admin.register(CoachingStaff)
class CoachingStaffAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'role', 'team_type', 'joined_date']
    list_filter = ['role', 'team_type']
    search_fields = ['first_name', 'last_name', 'role']
    date_hierarchy = 'joined_date'


@admin.register(Highlight)
class HighlightAdmin(admin.ModelAdmin):
    list_display = ['title', 'opponent', 'score', 'match_date', 'views', 'is_featured']
    list_filter = ['is_featured', 'match_date']
    search_fields = ['title', 'opponent', 'description']
    date_hierarchy = 'match_date'
    readonly_fields = ['views']


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'date_taken', 'is_featured']
    list_filter = ['category', 'is_featured', 'date_taken']
    search_fields = ['title', 'description', 'photographer']
    date_hierarchy = 'date_taken'


@admin.register(StadiumTour)
class StadiumTourAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'tour_type', 'tour_date', 'status', 'number_of_people']
    list_filter = ['tour_type', 'status', 'tour_date']
    search_fields = ['first_name', 'last_name', 'email']
    date_hierarchy = 'tour_date'


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['subject', 'first_name', 'last_name', 'message_type', 'status', 'created_at']
    list_filter = ['message_type', 'status', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'subject', 'message']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at', 'updated_at']


@admin.register(ClubRegistration)
class ClubRegistrationAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'interest_area', 'is_processed', 'registration_date']
    list_filter = ['interest_area', 'is_processed', 'registration_date']
    search_fields = ['first_name', 'last_name', 'email']
    date_hierarchy = 'registration_date'


@admin.register(AcademyEnrollment)
class AcademyEnrollmentAdmin(admin.ModelAdmin):
    list_display = ['child_first_name', 'child_last_name', 'age_group', 'parent_email', 'is_approved', 'enrollment_date']
    list_filter = ['age_group', 'is_approved', 'enrollment_date']
    search_fields = ['child_first_name', 'child_last_name', 'parent_email']
    date_hierarchy = 'enrollment_date'