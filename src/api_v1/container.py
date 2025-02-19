from dependency_injector import containers, providers
import chromadb

from src.interations import RecommendationsInteration
from src.core.use_cases import RecommendationsUseCase
from src.services.vector_store import ChromaRetrieverService
from src.services.preprocessing import SklearnPreprocessingService
from src.services.preprocessing.transformers import (
    GenderBinarizer,
    MilitaryServiceBinarizer,
    ForeignCitizenshipEncoder,
    ApplicantsScaler
)
from src.config import settings


class Container(containers.DeclarativeContainer):
    gender_binarizer = providers.Singleton(
        GenderBinarizer,
        path=settings.transformers.gender_binarizer_path
    )
    military_service_binarizer = providers.Singleton(
        MilitaryServiceBinarizer,
        path=settings.transformers.military_service_binarizer_path
    )
    foreign_citizenship_encoder = providers.Singleton(
        ForeignCitizenshipEncoder,
        path=settings.transformers.foreign_citizenship_encoder_path
    )
    applicants_scaler = providers.Singleton(
        ApplicantsScaler,
        path=settings.transformers.applicants_scaler_path
    )
    preprocessing_service = providers.Singleton(
        SklearnPreprocessingService,
        gender_binarizer=gender_binarizer,
        military_service_binarizer=military_service_binarizer,
        foreign_citizendhip_encoder=foreign_citizenship_encoder,
        applicants_scaler=applicants_scaler
    )
    client_api = providers.Singleton(
        chromadb.PersistentClient,
        path=settings.chroma.path
    )
    retriever_service = providers.Singleton(
        ChromaRetrieverService,
        client_api=client_api,
        collection_name="applicants"
    )
    recommendations_use_case = providers.Singleton(
        RecommendationsUseCase,
        preprocessing_service=preprocessing_service,
        retriever_service=retriever_service
    )
    recommendations_interaction = providers.Factory(
        RecommendationsInteration,
        recommendations_use_case=recommendations_use_case
    )
