from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MembershipViewSet, PlayerViewSet, CoachingStaffViewSet,
    HighlightViewSet, GalleryViewSet, StadiumTourViewSet,
    ContactMessageViewSet, ClubRegistrationViewSet, AcademyEnrollmentViewSet
)

router = DefaultRouter()

# Register all viewsets
router.register(r'memberships', MembershipViewSet, basename='membership')
router.register(r'players', PlayerViewSet, basename='player')
router.register(r'coaching-staff', CoachingStaffViewSet, basename='coaching-staff')
router.register(r'highlights', HighlightViewSet, basename='highlight')
router.register(r'gallery', GalleryViewSet, basename='gallery')
router.register(r'stadium-tours', StadiumTourViewSet, basename='stadium-tour')
router.register(r'contact-messages', ContactMessageViewSet, basename='contact-message')
router.register(r'club-registrations', ClubRegistrationViewSet, basename='club-registration')
router.register(r'academy-enrollments', AcademyEnrollmentViewSet, basename='academy-enrollment')

urlpatterns = [
    path('', include(router.urls)),
]

"""
API Endpoints Documentation:

MEMBERSHIPS (Become a Member):
- GET    /api/memberships/                  - List all memberships
- POST   /api/memberships/                  - Create new membership
- GET    /api/memberships/{id}/             - Get specific membership
- PUT    /api/memberships/{id}/             - Update membership
- DELETE /api/memberships/{id}/             - Delete membership
- GET    /api/memberships/active_members/   - Get all active members

PLAYERS (View Full Squad, Women's Team, Junior Team, Academy, First Team):
- GET    /api/players/                      - List all players
- POST   /api/players/                      - Create new player
- GET    /api/players/{id}/                 - Get specific player
- PUT    /api/players/{id}/                 - Update player
- DELETE /api/players/{id}/                 - Delete player
- GET    /api/players/first_team/           - Get first team squad
- GET    /api/players/womens_team/          - Get women's team
- GET    /api/players/junior_team/          - Get junior team
- GET    /api/players/academy/              - Get academy players
- GET    /api/players/by_position/?position=GK  - Get players by position

COACHING STAFF:
- GET    /api/coaching-staff/               - List all coaching staff
- POST   /api/coaching-staff/               - Create new staff member
- GET    /api/coaching-staff/{id}/          - Get specific staff member
- PUT    /api/coaching-staff/{id}/          - Update staff member
- DELETE /api/coaching-staff/{id}/          - Delete staff member
- GET    /api/coaching-staff/by_team/?team=first - Get staff by team

HIGHLIGHTS (Watch Highlights):
- GET    /api/highlights/                   - List all highlights
- POST   /api/highlights/                   - Create new highlight
- GET    /api/highlights/{id}/              - Get specific highlight
- PUT    /api/highlights/{id}/              - Update highlight
- DELETE /api/highlights/{id}/              - Delete highlight
- GET    /api/highlights/featured/          - Get featured highlights
- POST   /api/highlights/{id}/increment_views/ - Increment view count
- GET    /api/highlights/recent/?limit=10   - Get recent highlights

GALLERY:
- GET    /api/gallery/                      - List all gallery images
- POST   /api/gallery/                      - Upload new image
- GET    /api/gallery/{id}/                 - Get specific image
- PUT    /api/gallery/{id}/                 - Update image
- DELETE /api/gallery/{id}/                 - Delete image
- GET    /api/gallery/by_category/?category=match - Get by category
- GET    /api/gallery/featured/             - Get featured images

STADIUM TOURS:
- GET    /api/stadium-tours/                - List all tour bookings
- POST   /api/stadium-tours/                - Create new tour booking
- GET    /api/stadium-tours/{id}/           - Get specific booking
- PUT    /api/stadium-tours/{id}/           - Update booking
- DELETE /api/stadium-tours/{id}/           - Delete booking
- PATCH  /api/stadium-tours/{id}/confirm/   - Confirm booking
- PATCH  /api/stadium-tours/{id}/cancel/    - Cancel booking
- GET    /api/stadium-tours/available_dates/ - Get available dates

CONTACT MESSAGES (Send Message):
- GET    /api/contact-messages/             - List all messages
- POST   /api/contact-messages/             - Send new message
- GET    /api/contact-messages/{id}/        - Get specific message
- PUT    /api/contact-messages/{id}/        - Update message
- DELETE /api/contact-messages/{id}/        - Delete message
- PATCH  /api/contact-messages/{id}/mark_resolved/ - Mark as resolved

CLUB REGISTRATIONS (Join the Club):
- GET    /api/club-registrations/           - List all registrations
- POST   /api/club-registrations/           - Create new registration
- GET    /api/club-registrations/{id}/      - Get specific registration
- PUT    /api/club-registrations/{id}/      - Update registration
- DELETE /api/club-registrations/{id}/      - Delete registration
- PATCH  /api/club-registrations/{id}/mark_processed/ - Mark as processed

ACADEMY ENROLLMENTS:
- GET    /api/academy-enrollments/          - List all enrollments
- POST   /api/academy-enrollments/          - Create new enrollment
- GET    /api/academy-enrollments/{id}/     - Get specific enrollment
- PUT    /api/academy-enrollments/{id}/     - Update enrollment
- DELETE /api/academy-enrollments/{id}/     - Delete enrollment
- PATCH  /api/academy-enrollments/{id}/approve/ - Approve enrollment
- GET    /api/academy-enrollments/by_age_group/?age_group=u12 - Get by age
"""