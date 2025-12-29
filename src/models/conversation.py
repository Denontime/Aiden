"""对话历史数据模型"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text
from src.models.database import Base


class Conversation(Base):
    """对话历史表"""
    
    __tablename__ = "conversations"
    
    id = Column(Integer, primary_key=True, index=True, comment="对话ID")
    session_id = Column(String(100), nullable=False, index=True, comment="会话ID")
    user_id = Column(Integer, comment="用户ID")
    role = Column(String(20), nullable=False, comment="角色: user/assistant/system")
    content = Column(Text, nullable=False, comment="对话内容")
    timestamp = Column(DateTime, default=datetime.utcnow, index=True, comment="时间戳")
    
    def __repr__(self):
        return f"<Conversation(id={self.id}, session='{self.session_id}', role='{self.role}')>"
