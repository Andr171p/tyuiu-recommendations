import chromadb
from dependency_injector import containers, providers

from src.config import settings
from src.core.use_cases import RecommendationsUseCase
from src.vector_store.chroma import ChromaRetriever
from src.database.crud import DirectionCRUD, PointsCRUD
from src.database.database_manager import DatabaseManager
from src.preprocessing import SklearnPipeline
from src.preprocessing.sklearn_transformers import (
    ZerosImputer,
    GenderBinarizer,
    MilitaryServiceBinarizer,
    ForeignCitizenshipEncoder,
    ApplicantsScaler
)
from src.repository.database import DirectionRepository, PointsRepository
from src.repository.vector_store import VectorStoreRepository
from src.services.preprocessing import PreprocessingService


class Container(containers.DeclarativeContainer):
    zeros_imputer = ZerosImputer()
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
    sklearn_pipeline = providers.Singleton(
        SklearnPipeline,
        zeros_imputer=zeros_imputer,
        gender_binarizer=gender_binarizer,
        military_service_binarizer=military_service_binarizer,
        foreign_citizenship_encoder=foreign_citizenship_encoder,
        applicants_scaler=applicants_scaler
    )
    client_api = providers.Singleton(
        chromadb.PersistentClient,
        path=r"C:\Users\andre\IdeaProjects\TyuiuDirectionsRecSys\chroma"
    )
    chroma_retriever = providers.Singleton(
        ChromaRetriever,
        client_api=client_api,
        collection_name="applicants"
    )
    vector_store_repository = providers.Singleton(
        VectorStoreRepository,
        retriever=chroma_retriever
    )
    database_manager = DatabaseManager()
    database_manager.init(settings.sqlite.url)
    directions_crud = providers.Singleton(
        DirectionCRUD,
        manager=database_manager
    )
    points_crud = providers.Singleton(
        PointsCRUD,
        manager=database_manager
    )
    directions_repository = providers.Singleton(
        DirectionRepository,
        crud=directions_crud
    )
    points_repository = providers.Singleton(
        PointsRepository,
        crud=points_crud
    )
    preprocessing_service = providers.Singleton(
        PreprocessingService,
        pipeline=sklearn_pipeline
    )
    recommendations_use_case = providers.Factory(
        RecommendationsUseCase,
        preprocessing_service=preprocessing_service,
        vector_store_repository=vector_store_repository
    )
