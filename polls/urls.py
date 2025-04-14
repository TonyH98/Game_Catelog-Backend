from rest_framework.routers import DefaultRouter
from django.urls import path, include

from rest_framework_nested.routers import NestedDefaultRouter
from .views import UsersListCreate, UsersDetail, UsersGamesListCreate, UsersGamesDetail, GameReviewListCreate, GameReviewDetails

router = DefaultRouter()
router.register(r'users', UsersListCreate, basename='user')
router.register(r'games', UsersGamesListCreate, basename='game')

# Nested router for game reviews
game_router = NestedDefaultRouter(router, r'games', lookup='game')
game_router.register(r'reviews', GameReviewListCreate, basename='game-review')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(game_router.urls)),
]
