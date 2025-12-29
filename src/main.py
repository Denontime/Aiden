"""FastAPI应用主文件"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from src.core import settings, log
from src.models import init_db
from src.api import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期管理"""
    # 启动时执行
    log.info("正在启动Aiden智能AI管家系统...")
    log.info(f"服务器配置: {settings.server.host}:{settings.server.port}")
    
    # 初始化数据库
    log.info("正在初始化数据库...")
    init_db()
    log.info("数据库初始化完成")
    
    yield
    
    # 关闭时执行
    log.info("正在关闭Aiden智能AI管家系统...")


# 创建FastAPI应用
app = FastAPI(
    title="Aiden智能AI管家",
    description="基于边缘计算的语音交互系统,提供记忆管理、人脸识别、日程管理、智能家居控制等能力",
    version="0.1.0",
    lifespan=lifespan,
)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(router, prefix="/api")


@app.get("/")
async def root():
    """根路径"""
    return {
        "message": "欢迎使用Aiden智能AI管家系统",
        "version": "0.1.0",
        "status": "running"
    }


@app.get("/health")
async def health_check():
    """健康检查"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.server.host,
        port=settings.server.port,
        reload=settings.server.debug_mode,
        workers=settings.server.workers,
    )
