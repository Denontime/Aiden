#!/bin/bash
# Aiden智能AI管家系统 - Linux启动脚本
# 用于在Linux环境下启动Aiden系统

echo "正在启动Aiden智能AI管家系统..."

# 检查Python是否已安装
if ! command -v python3 &> /dev/null; then
    echo "错误: 未找到Python3。请确保Python3已安装。"
    exit 1
fi

# 检查并安装依赖
if ! python3 -c "import fastapi" &> /dev/null; then
    echo "安装依赖..."
    
    # 首先安装核心依赖
    if ! python3 -m pip install "pydantic>=2.5.3" "pydantic-settings>=2.1.0"; then
        echo "核心依赖安装失败"
        exit 1
    fi
    
    # 安装其他依赖
    if ! python3 -m pip install fastapi==0.109.0 uvicorn[standard]==0.27.0 sqlalchemy>=2.0.25 alembic==1.13.1 python-dotenv==1.0.0 python-multipart==0.0.6 python-jose[cryptography]==3.3.0 passlib[bcrypt]==1.7.4 aiofiles==23.2.1 httpx==0.26.0 pyyaml==6.0.1 qdrant-client==1.7.3 paho-mqtt==1.6.1 apscheduler==3.10.4 loguru==0.7.2 email-validator==2.1.0 pytest==7.4.4 pytest-asyncio==0.23.3 black==24.1.1 flake8==7.0.0 mypy==1.8.0; then
        echo "依赖安装失败，尝试使用预编译包..."
        if ! python3 -m pip install --only-binary=all -r requirements.txt; then
            echo "错误: 依赖安装失败"
            exit 1
        fi
    fi
fi

# 检查并创建必要的目录
mkdir -p data logs

# 启动Aiden系统
echo "启动Aiden智能AI管家系统..."
python3 run_app.py
