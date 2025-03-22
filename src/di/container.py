from dishka import make_async_container

from src.di.providers import RecommendationsProvider, DirectionsProvider, DatabaseProvider


container = make_async_container(
    DatabaseProvider(),
    DirectionsProvider(),
    RecommendationsProvider()
)
