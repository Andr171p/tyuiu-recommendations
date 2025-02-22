import logging
from contextlib import (
    asynccontextmanager,
    AbstractAsyncContextManager
)

from fastapi import FastAPI


log = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AbstractAsyncContextManager[None]:
    log.info("Start add vector to chroma")
    from scripts import add_vectors_chroma
    log.info("Vectors added to chroma successfully")
    log.info("Start add directions to sqlite")
    from scripts import create_db
    from scripts import add_directions_sqlite
    log.info("Direction added to sqlite successfully")
