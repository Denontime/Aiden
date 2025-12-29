"""对话管理API路由"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_conversations():
    """获取对话历史"""
    return {"message": "对话管理功能开发中"}
