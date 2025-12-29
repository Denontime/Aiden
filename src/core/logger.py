"""日志管理模块"""

import sys
from pathlib import Path
from loguru import logger

from src.core.config import settings


def setup_logger():
    """配置日志系统"""
    
    # 移除默认处理器
    logger.remove()
    
    # 添加控制台处理器
    logger.add(
        sys.stdout,
        level=settings.log.level,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        colorize=True,
    )
    
    # 创建日志目录
    log_path = Path(settings.log.file_path)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    
    # 添加文件处理器
    logger.add(
        settings.log.file_path,
        level=settings.log.level,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        rotation=settings.log.rotation,
        retention=settings.log.retention,
        compression="zip",
        encoding="utf-8",
    )
    
    logger.info("日志系统初始化完成")
    return logger


# 全局日志实例
log = setup_logger()
