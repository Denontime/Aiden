"""设备管理API路由"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_devices():
    """获取设备列表"""
    return {"message": "设备管理功能开发中"}
