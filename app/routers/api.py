from fastapi import APIRouter

router = APIRouter()


@router.get("/test")
async def get_mesh_handler():
    return {"status": 1, "msg": "SUCCESS"}


@router.get("/info")
async def check_info():
    import platform
    host_name = platform.node()
    return {"status": 1, "data": host_name}
