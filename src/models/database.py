"""数据库基础配置"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

from src.core.config import settings

# 创建数据库引擎
engine = create_engine(
    settings.database.url,
    echo=settings.database.echo,
    pool_size=settings.database.pool_size,
    max_overflow=settings.database.max_overflow,
    connect_args={"check_same_thread": False} if "sqlite" in settings.database.url else {},
)

# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建基类
Base = declarative_base()


def get_db():
    """获取数据库会话的依赖注入函数"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@contextmanager
def get_db_context():
    """获取数据库会话的上下文管理器"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """初始化数据库,创建所有表"""
    from src.models import user, schedule, device, conversation, memory
    Base.metadata.create_all(bind=engine)
