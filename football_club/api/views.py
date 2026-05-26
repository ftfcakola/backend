from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    Membership, Player, CoachingStaff, Highlight, Gallery,
    StadiumTour, ContactMessage, ClubRegistration, AcademyEnrollment
)
from .serializers import (
    MembershipSerializer, PlayerSerializer, CoachingStaffSerializer,
    HighlightSerializer, GallerySerializer, StadiumTourSerializer,
    ContactMessageSerializer, ClubRegistrationSerializer, AcademyEnrollmentSerializer
)


class MembershipViewSet(viewsets.ModelViewSet):
    """
    API endpoint for memberships (Become a Member)
    """
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['membership_type', 'is_active']
    search_fields = ['first_name', 'last_name', 'email']
    ordering_fields = ['date_joined', 'expiry_date']
    
    @action(detail=False, methods=['get'])
    def active_members(self, request):
        """Get all active members"""
        active = self.queryset.filter(is_active=True)
        serializer = self.get_serializer(active, many=True)
        return Response(serializer.data)


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint for squad players (View Full Squad)
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['position', 'team_type', 'is_active']
    search_fields = ['first_name', 'last_name', 'nationality']
    ordering_fields = ['jersey_number', 'last_name']
    
    @action(detail=False, methods=['get'])
    def first_team(self, request):
        """Get first team squad"""
        first_team = self.queryset.filter(team_type='first', is_active=True)
        serializer = self.get_serializer(first_team, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def womens_team(self, request):
        """Get women's team squad"""
        womens = self.queryset.filter(team_type='women', is_active=True)
        serializer = self.get_serializer(womens, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def junior_team(self, request):
        """Get junior team squad"""
        junior = self.queryset.filter(team_type='junior', is_active=True)
        serializer = self.get_serializer(junior, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def academy(self, request):
        """Get academy players"""
        academy = self.queryset.filter(team_type='academy', is_active=True)
        serializer = self.get_serializer(academy, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def by_position(self, request):
        """Get players grouped by position"""
        position = request.query_params.get('position', None)
        if position:
            players = self.queryset.filter(position=position, is_active=True)
            serializer = self.get_serializer(players, many=True)
            return Response(serializer.data)
        return Response({"error": "Position parameter is required"}, status=400)


class CoachingStaffViewSet(viewsets.ModelViewSet):
    """
    API endpoint for coaching staff (Coaching Staff)
    """
    queryset = CoachingStaff.objects.all()
    serializer_class = CoachingStaffSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['role', 'team_type']
    search_fields = ['first_name', 'last_name', 'role']
    ordering_fields = ['role', 'last_name']
    
    @action(detail=False, methods=['get'])
    def by_team(self, request):
        """Get coaching staff by team type"""
        team_type = request.query_params.get('team', 'first')
        staff = self.queryset.filter(team_type=team_type)
        serializer = self.get_serializer(staff, many=True)
        return Response(serializer.data)


class HighlightViewSet(viewsets.ModelViewSet):
    """
    API endpoint for match highlights (Watch Highlights)
    """
    queryset = Highlight.objects.all()
    serializer_class = HighlightSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_featured']
    search_fields = ['title', 'opponent', 'description']
    ordering_fields = ['match_date', 'views', 'created_at']
    
    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured highlights"""
        featured = self.queryset.filter(is_featured=True)
        serializer = self.get_serializer(featured, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def increment_views(self, request, pk=None):
        """Increment view count for a highlight"""
        highlight = self.get_object()
        highlight.views += 1
        highlight.save()
        serializer = self.get_serializer(highlight)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def recent(self, request):
        """Get most recent highlights"""
        limit = request.query_params.get('limit', 10)
        recent = self.queryset.order_by('-match_date')[:int(limit)]
        serializer = self.get_serializer(recent, many=True)
        return Response(serializer.data)


class GalleryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for photo gallery (Gallery)
    """
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'is_featured']
    search_fields = ['title', 'description', 'photographer']
    ordering_fields = ['date_taken', 'created_at']
    
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """Get gallery images by category"""
        category = request.query_params.get('category', None)
        if category:
            images = self.queryset.filter(category=category)
            serializer = self.get_serializer(images, many=True)
            return Response(serializer.data)
        return Response({"error": "Category parameter is required"}, status=400)
    
    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured gallery images"""
        featured = self.queryset.filter(is_featured=True)
        serializer = self.get_serializer(featured, many=True)
        return Response(serializer.data)


class StadiumTourViewSet(viewsets.ModelViewSet):
    """
    API endpoint for stadium tour bookings (Stadium Tour)
    """
    queryset = StadiumTour.objects.all()
    serializer_class = StadiumTourSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['tour_type', 'status', 'tour_date']
    search_fields = ['first_name', 'last_name', 'email']
    ordering_fields = ['tour_date', 'booking_date']
    
    @action(detail=True, methods=['patch'])
    def confirm(self, request, pk=None):
        """Confirm a tour booking"""
        tour = self.get_object()
        tour.status = 'confirmed'
        tour.save()
        serializer = self.get_serializer(tour)
        return Response(serializer.data)
    
    @action(detail=True, methods=['patch'])
    def cancel(self, request, pk=None):
        """Cancel a tour booking"""
        tour = self.get_object()
        tour.status = 'cancelled'
        tour.save()
        serializer = self.get_serializer(tour)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def available_dates(self, request):
        """Get available tour dates (simplified - you can customize logic)"""
        from datetime import date, timedelta
        available = []
        for i in range(30):
            check_date = date.today() + timedelta(days=i)
            if check_date.weekday() not in [6]:  # Exclude Sundays
                available.append(check_date.isoformat())
        return Response({"available_dates": available})


class ContactMessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint for contact messages (Send Message)
    """
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['message_type', 'status']
    search_fields = ['first_name', 'last_name', 'email', 'subject']
    ordering_fields = ['created_at', 'updated_at']
    
    @action(detail=True, methods=['patch'])
    def mark_resolved(self, request, pk=None):
        """Mark a message as resolved"""
        message = self.get_object()
        message.status = 'resolved'
        message.save()
        serializer = self.get_serializer(message)
        return Response(serializer.data)


class ClubRegistrationViewSet(viewsets.ModelViewSet):
    """
    API endpoint for club registrations (Join the Club)
    """
    queryset = ClubRegistration.objects.all()
    serializer_class = ClubRegistrationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['interest_area', 'is_processed']
    search_fields = ['first_name', 'last_name', 'email']
    ordering_fields = ['registration_date']
    
    @action(detail=True, methods=['patch'])
    def mark_processed(self, request, pk=None):
        """Mark a registration as processed"""
        registration = self.get_object()
        registration.is_processed = True
        registration.save()
        serializer = self.get_serializer(registration)
        return Response(serializer.data)


class AcademyEnrollmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for academy enrollments (Academy)
    """
    queryset = AcademyEnrollment.objects.all()
    serializer_class = AcademyEnrollmentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['age_group', 'is_approved']
    search_fields = ['child_first_name', 'child_last_name', 'parent_email']
    ordering_fields = ['enrollment_date', 'child_date_of_birth']
    
    @action(detail=True, methods=['patch'])
    def approve(self, request, pk=None):
        """Approve an academy enrollment"""
        enrollment = self.get_object()
        enrollment.is_approved = True
        enrollment.save()
        serializer = self.get_serializer(enrollment)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def by_age_group(self, request):
        """Get enrollments by age group"""
        age_group = request.query_params.get('age_group', None)
        if age_group:
            enrollments = self.queryset.filter(age_group=age_group)
            serializer = self.get_serializer(enrollments, many=True)
            return Response(serializer.data)
        return Response({"error": "Age group parameter is required"}, status=400)