"""智能设备数据模型"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text, JSON
from src.models.database import Base


class Device(Base):
    """智能设备表"""
    
    __tablename__ = "devices"
    
    id = Column(Integer, primary_key=True, index=True, comment="设备ID")
    device_name = Column(String(100), nullable=False, comment="设备名称")
    device_type = Column(String(50), nullable=False, comment="设备类型: light/ac/curtain/sensor等")
    protocol = Column(String(20), nullable=False, comment="接入协议: mqtt/mijia/xiaoai")
    connection_config = Column(JSON, comment="连接配置")
    current_status = Column(JSON, comment="当前状态")
    supported_commands = Column(JSON, comment="支持的控制指令列表")
    room = Column(String(50), comment="所在房间")
    is_online = Column(Integer, default=0, comment="是否在线(1=是,0=否)")
    last_seen = Column(DateTime, comment="最后在线时间")
    created_at = Column(DateTime, default=datetime.utcnow, comment="创建时间")
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, comment="更新时间")
    
    def __repr__(self):
        return f"<Device(id={self.id}, name='{self.device_name}', type='{self.device_type}')>"
