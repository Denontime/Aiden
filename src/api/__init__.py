"""API路由模块初始化"""

from fastapi import APIRouter

# 创建主路由
router = APIRouter()

# 导入子路由
from src.api.routes import users, schedules, devices, conversations

# 注册子路由
router.include_router(users.router, prefix="/users", tags=["用户管理"])
router.include_router(schedules.router, prefix="/schedules", tags=["日程管理"])
router.include_router(devices.router, prefix="/devices", tags=["设备管理"])
router.include_router(conversations.router, prefix="/conversations", tags=["对话管理"])

__all__ = ["router"]
