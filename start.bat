@echo off
REM Aiden智能AI管家启动脚本

echo 正在启动Aiden智能AI管家系统...
echo.

REM 检查Python环境
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未找到Python，请确保已安装Python 3.10+
    pause
    exit /b 1
)

REM 检查虚拟环境
if not exist "venv" (
    echo 创建虚拟环境...
    python -m venv venv
)

REM 激活虚拟环境
call venv\Scripts\activate.bat

REM 检查依赖是否已安装
python -c "import fastapi, uvicorn, sqlalchemy, loguru" >nul 2>&1
if errorlevel 1 (
    echo 安装依赖包...
    python -m pip install -r requirements.txt
)

REM 启动应用
echo 启动Aiden服务...
python -c "import sys; sys.path.insert(0, '.'); from src.main import app; import uvicorn; uvicorn.run(app, host='0.0.0.0', port=8000, reload=False)"

pause