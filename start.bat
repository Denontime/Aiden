@echo off
REM Aiden智能AI管家系统 - Windows启动脚本
REM 用于在Windows环境下启动Aiden系统

echo 正在启动Aiden智能AI管家系统...

REM 检查Python是否已安装
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未找到Python。请确保Python已安装并添加到PATH环境变量中。
    pause
    exit /b 1
)

REM 检查并安装依赖，处理Windows上pydantic-core编译问题
echo 检查依赖...
python -c "import fastapi" >nul 2>&1
if errorlevel 1 (
    echo 安装依赖（处理Windows兼容性问题）...
    echo 首先安装核心依赖...
    python -m pip install "pydantic>=2.5.3" "pydantic-settings>=2.1.0"
    
    echo 安装其他依赖...
    python -m pip install fastapi==0.109.0 uvicorn[standard]==0.27.0 sqlalchemy>=2.0.25 alembic==1.13.1 python-dotenv==1.0.0 python-multipart==0.0.6 python-jose[cryptography]==3.3.0 passlib[bcrypt]==1.7.4 aiofiles==23.2.1 httpx==0.26.0 pyyaml==6.0.1 qdrant-client==1.7.3 paho-mqtt==1.6.1 apscheduler==3.10.4 loguru==0.7.2 email-validator==2.1.0 pytest==7.4.4 pytest-asyncio==0.23.3 black==24.1.1 flake8==7.0.0 mypy==1.8.0
    
    if errorlevel 1 (
        echo 尝试使用预编译包安装依赖...
        python -m pip install --only-binary=all -r requirements.txt
        if errorlevel 1 (
            echo 错误: 依赖安装失败
            pause
            exit /b 1
        )
    )
)

REM 检查并创建必要的目录
if not exist "data" mkdir data
if not exist "logs" mkdir logs

REM 检查并配置环境变量
if not exist ".env" (
    echo 创建环境配置文件...
    copy .env.example .env >nul
    echo 请编辑 .env 文件配置API密钥等信息
)

REM 修复环境变量配置
echo 修复环境变量配置...
powershell -Command "(gc .env) -replace 'DEBUG=true', 'SERVER_DEBUG_MODE=true' | Out-File -encoding UTF8 .env.tmp"
powershell -Command "(gc .env.tmp) -replace 'FACE_DETECTION_INTERVAL=1.0', 'FACE_RECOGNITION_DETECTION_INTERVAL_SEC=1.0' | Out-File -encoding UTF8 .env"
del .env.tmp

REM 初始化数据库
echo 初始化数据库...
python -c "from src.models import init_db; init_db()" 2>nul
if errorlevel 1 (
    echo 数据库初始化失败，正在尝试更新SQLAlchemy...
    python -m pip install "sqlalchemy>=2.0.35"
    python -c "from src.models import init_db; init_db()"
)

REM 启动Aiden系统
echo 启动Aiden智能AI管家系统...
python run_app.py

pause
