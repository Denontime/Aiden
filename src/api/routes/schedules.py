"""日程管理API路由"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_schedules():
    """获取日程列表"""
    return {"message": "日程管理功能开发中"}
