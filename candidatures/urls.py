from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CandidateViewSet, RecruiterViewSet, OfferViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'candidates', CandidateViewSet)
router.register(r'recruiter', RecruiterViewSet)
router.register(r'offer', OfferViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Recruitment API",
        default_version="v1",
        description="API pour gérer les candidats",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
