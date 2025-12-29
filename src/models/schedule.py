"""日程管理数据模型"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text, JSON
from src.models.database import Base


class Schedule(Base):
    """日程表"""
    
    __tablename__ = "schedules"
    
    id = Column(Integer, primary_key=True, index=True, comment="日程ID")
    event_name = Column(String(200), nullable=False, comment="事件名称")
    start_time = Column(DateTime, nullable=False, index=True, comment="开始时间")
    end_time = Column(DateTime, comment="结束时间")
    location = Column(String(200), comment="地点")
    participants = Column(JSON, comment="参与人列表")
    remind_times = Column(JSON, comment="提醒时间列表")
    status = Column(String(20), default="pending", comment="状态: pending/in_progress/completed/cancelled")
    description = Column(Text, comment="详细描述")
    created_by = Column(Integer, comment="创建者用户ID")
    created_at = Column(DateTime, default=datetime.utcnow, comment="创建时间")
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, comment="更新时间")
    
    def __repr__(self):
        return f"<Schedule(id={self.id}, event='{self.event_name}', start={self.start_time})>"
