from enum import Enum
from typing import List, Any, Union
from fastapi import FastAPI, APIRouter, Depends


class Method(Enum):
    PUT = "PUT"
    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"


class RealRute:
    def __init__(self, route_path: str, method: Method, call_back: Any):
        self.route = route_path
        self.callBack = call_back
        self.methods: List[str] = [str(method.value)]


INCLUDE_ROUTES: List[RealRute] = [
]


# Dependency
def add_routes(app: FastAPI, router: APIRouter, api_route: str):
    for _route in INCLUDE_ROUTES:
        add_route(_route, app, router.dependencies, api_route)


def add_route(route: RealRute, app: FastAPI, dependencies: Union[List[Depends]], api_route: str):
    _path = route.route
    _ = '/'
    api_route = f"{api_route}/" if api_route else ''
    prefix = '' if _path.startswith(_) else _
    prefix += f"{api_route}{_path}"
    app.add_api_route(prefix, route.callBack, dependencies=dependencies, include_in_schema=True,
                      methods=route.methods)
