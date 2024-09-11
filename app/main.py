import uvicorn
from fastapi import FastAPI
from app.routers.api import router
from app.routers.routes import add_routes
from contextlib import asynccontextmanager
from starlette.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(_app: FastAPI):
    print("Server startup")
    yield
    print("Server shutdown")


def create_app() -> FastAPI:
    _app = FastAPI(lifespan=lifespan)
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )
    return _app


def run_app(_app: FastAPI):
    try:
        uvicorn.run(
            "main:app",
            host="0.0.0.0",
            port=8000,
            log_level="info",
            reload=True,
            workers=1000,
            limit_concurrency=1000
        )
        print("STOPPED")
    except Exception as ex:
        print("ERROR STARTING APP", ex)


def add_dependencies(_app: FastAPI):
    _app.include_router(router)
    add_routes(_app, router, "")


def create_server() -> FastAPI:
    _app = create_app()
    add_dependencies(_app)
    return _app


app = create_server()


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("./favicon.ico")


if __name__ == '__main__':
    print("RUNNING")
    run_app(app)
