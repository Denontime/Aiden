"""用户管理API Schema"""

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class UserBase(BaseModel):
    """用户基础信息"""
    name: str = Field(..., description="姓名")
    nickname: Optional[str] = Field(None, description="昵称/称谓")
    relation: Optional[str] = Field(None, description="与主人的关系")
    occupation: Optional[str] = Field(None, description="职业")
    phone: Optional[str] = Field(None, description="联系电话")
    email: Optional[str] = Field(None, description="邮箱")
    notes: Optional[str] = Field(None, description="备注信息")


class UserCreate(UserBase):
    """创建用户"""
    pass


class UserUpdate(BaseModel):
    """更新用户"""
    name: Optional[str] = None
    nickname: Optional[str] = None
    relation: Optional[str] = None
    occupation: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    notes: Optional[str] = None


class UserResponse(UserBase):
    """用户响应"""
    id: int
    avatar_url: Optional[str] = None
    is_active: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
