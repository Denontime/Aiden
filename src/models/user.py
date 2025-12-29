"""用户档案数据模型"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text, JSON
from src.models.database import Base


class User(Base):
    """用户档案表"""
    
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True, comment="用户ID")
    name = Column(String(100), nullable=False, comment="姓名")
    nickname = Column(String(100), comment="昵称/称谓")
    relation = Column(String(50), comment="与主人的关系")
    occupation = Column(String(100), comment="职业")
    phone = Column(String(20), comment="联系电话")
    email = Column(String(100), comment="邮箱")
    avatar_url = Column(String(500), comment="头像URL")
    face_encoding = Column(Text, comment="人脸特征向量(JSON格式)")
    preferences = Column(JSON, comment="用户偏好设置")
    notes = Column(Text, comment="备注信息")
    is_active = Column(Integer, default=1, comment="是否激活(1=是,0=否)")
    created_at = Column(DateTime, default=datetime.utcnow, comment="创建时间")
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, comment="更新时间")
    
    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', relation='{self.relation}')>"
