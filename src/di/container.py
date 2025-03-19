from dishka import make_async_container

from src.di.providers import RecommendationsProvider


container = make_async_container(RecommendationsProvider())
