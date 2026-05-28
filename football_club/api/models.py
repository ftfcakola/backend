from django.db import models
from django.utils import timezone


class Membership(models.Model):
    """Model for club memberships"""
    MEMBERSHIP_TYPES = [
        ('basic', 'Basic Membership'),
        ('premium', 'Premium Membership'),
        ('vip', 'VIP Membership'),
        ('season', 'Season Ticket'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    membership_type = models.CharField(max_length=20, choices=MEMBERSHIP_TYPES)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    expiry_date = models.DateField()
    
    class Meta:
        ordering = ['-date_joined']
        
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.membership_type}"


class Player(models.Model):
    """Model for squad players"""
    POSITIONS = [
        ('GK', 'Goalkeeper'),
        ('DF', 'Defender'),
        ('MF', 'Midfielder'),
        ('FW', 'Forward'),
    ]
    
    TEAM_TYPES = [
        ('first', 'First Team'),
        ('women', "Women's Team"),
        ('junior', 'Junior Team'),
        ('academy', 'Academy'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    jersey_number = models.IntegerField()
    position = models.CharField(max_length=2, choices=POSITIONS)
    team_type = models.CharField(max_length=20, choices=TEAM_TYPES, default='first')
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    height = models.DecimalField(max_digits=4, decimal_places=2, help_text="Height in cm")
    weight = models.DecimalField(max_digits=5, decimal_places=2, help_text="Weight in kg")
    photo = models.URLField(upload_to='players/', blank=True, null=True)
    bio = models.TextField(blank=True)
    joined_date = models.DateField()
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['jersey_number']
        unique_together = ['jersey_number', 'team_type']
        
    def __str__(self):
        return f"#{self.jersey_number} {self.first_name} {self.last_name}"


class CoachingStaff(models.Model):
    """Model for coaching staff members"""
    ROLES = [
        ('head_coach', 'Head Coach'),
        ('assistant_coach', 'Assistant Coach'),
        ('goalkeeper_coach', 'Goalkeeper Coach'),
        ('fitness_coach', 'Fitness Coach'),
        ('physiotherapist', 'Physiotherapist'),
        ('analyst', 'Performance Analyst'),
    ]
    
    TEAM_TYPES = [
        ('first', 'First Team'),
        ('women', "Women's Team"),
        ('junior', 'Junior Team'),
        ('academy', 'Academy'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=30, choices=ROLES)
    team_type = models.CharField(max_length=20, choices=TEAM_TYPES, default='first')
    photo = models.URLField(upload_to='staff/', blank=True, null=True)
    bio = models.TextField(blank=True)
    joined_date = models.DateField()
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    
    class Meta:
        ordering = ['role', 'last_name']
        verbose_name_plural = "Coaching Staff"
        
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_role_display()}"


class Highlight(models.Model):
    """Model for match highlights and videos"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_url = models.URLField(help_text="YouTube or video platform URL")
    thumbnail = models.URLField(upload_to='highlights/', blank=True, null=True)
    match_date = models.DateField()
    opponent = models.CharField(max_length=100)
    score = models.CharField(max_length=20, help_text="e.g., 3-1")
    duration = models.CharField(max_length=10, help_text="e.g., 5:30")
    views = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-match_date', '-created_at']
        
    def __str__(self):
        return f"{self.title} - {self.match_date}"


class Gallery(models.Model):
    """Model for photo gallery"""
    CATEGORIES = [
        ('match', 'Match Photos'),
        ('training', 'Training'),
        ('event', 'Club Events'),
        ('stadium', 'Stadium'),
        ('fans', 'Fans'),
        ('historical', 'Historical'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    image = models.URLField(upload_to='gallery/')
    date_taken = models.DateField()
    photographer = models.CharField(max_length=100, blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_taken', '-created_at']
        verbose_name_plural = "Galleries"
        
    def __str__(self):
        return self.title


class StadiumTour(models.Model):
    """Model for stadium tour bookings"""
    TOUR_TYPES = [
        ('standard', 'Standard Tour'),
        ('premium', 'Premium Tour'),
        ('vip', 'VIP Experience'),
        ('group', 'Group Tour'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    tour_type = models.CharField(max_length=20, choices=TOUR_TYPES)
    tour_date = models.DateField()
    tour_time = models.TimeField()
    number_of_people = models.IntegerField(default=1)
    special_requirements = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    booking_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-tour_date', '-tour_time']
        
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.tour_date}"


class ContactMessage(models.Model):
    """Model for contact form messages"""
    MESSAGE_TYPES = [
        ('general', 'General Inquiry'),
        ('membership', 'Membership Query'),
        ('tickets', 'Ticket Inquiry'),
        ('media', 'Media Request'),
        ('partnership', 'Partnership Opportunity'),
        ('complaint', 'Complaint'),
    ]
    
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message_type = models.CharField(max_length=20, choices=MESSAGE_TYPES, default='general')
    subject = models.CharField(max_length=200)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.subject} - {self.email}"


class ClubRegistration(models.Model):
    """Model for 'Join the Club' registrations"""
    INTEREST_AREAS = [
        ('playing', 'Playing for the Club'),
        ('volunteering', 'Volunteering'),
        ('sponsorship', 'Sponsorship'),
        ('partnership', 'Partnership'),
        ('youth', 'Youth Programs'),
        ('community', 'Community Programs'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    interest_area = models.CharField(max_length=20, choices=INTEREST_AREAS)
    additional_info = models.TextField(blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-registration_date']
        
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_interest_area_display()}"


class AcademyEnrollment(models.Model):
    """Model for academy enrollments"""
    AGE_GROUPS = [
        ('u8', 'Under 8'),
        ('u10', 'Under 10'),
        ('u12', 'Under 12'),
        ('u14', 'Under 14'),
        ('u16', 'Under 16'),
        ('u18', 'Under 18'),
    ]
    
    # Child Information
    child_first_name = models.CharField(max_length=100)
    child_last_name = models.CharField(max_length=100)
    child_date_of_birth = models.DateField()
    age_group = models.CharField(max_length=10, choices=AGE_GROUPS)
    preferred_position = models.CharField(max_length=50, blank=True)
    
    # Parent/Guardian Information
    parent_first_name = models.CharField(max_length=100)
    parent_last_name = models.CharField(max_length=100)
    parent_email = models.EmailField()
    parent_phone = models.CharField(max_length=20)
    
    # Additional Information
    address = models.TextField()
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    medical_conditions = models.TextField(blank=True, help_text="Any medical conditions we should know about")
    previous_experience = models.TextField(blank=True, help_text="Previous football experience")
    
    enrollment_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-enrollment_date']
        
    def __str__(self):
        return f"{self.child_first_name} {self.child_last_name} - {self.get_age_group_display()}"