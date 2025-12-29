"""记忆数据模型"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text, Float
from src.models.database import Base


class Memory(Base):
    """记忆表"""
    
    __tablename__ = "memories"
    
    id = Column(Integer, primary_key=True, index=True, comment="记忆ID")
    memory_type = Column(String(20), nullable=False, comment="记忆类型: short/long/fact/event")
    content = Column(Text, nullable=False, comment="记忆内容")
    user_id = Column(Integer, comment="关联用户ID")
    importance = Column(Float, default=0.5, comment="重要性评分(0-1)")
    vector_id = Column(String(100), comment="向量数据库中的ID")
    created_at = Column(DateTime, default=datetime.utcnow, index=True, comment="创建时间")
    accessed_at = Column(DateTime, default=datetime.utcnow, comment="最后访问时间")
    access_count = Column(Integer, default=0, comment="访问次数")
    
    def __repr__(self):
        return f"<Memory(id={self.id}, type='{self.memory_type}', importance={self.importance})>"
