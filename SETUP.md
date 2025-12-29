# 开发环境搭建指南

## Windows环境快速启动

### 1. 环境准备

确保已安装:
- Python 3.10 或更高版本
- Git

### 2. 克隆项目

```bash
git clone <repository-url>
cd Aiden
```

### 3. 创建虚拟环境

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 4. 安装依赖

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. 配置环境变量

```powershell
Copy-Item .env.example .env
```

编辑 `.env` 文件,配置必要的API密钥:
- `LLM_API_KEY`: 大模型API密钥(阿里云通义千问)
- `JWT_SECRET_KEY`: JWT加密密钥(随机生成)

### 6. 初始化数据库

```powershell
python -c "from src.models import init_db; init_db()"
```

### 7. 启动服务

```powershell
python src/main.py
```

或使用uvicorn:

```powershell
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

访问 http://localhost:8000/docs 查看API文档

## Docker部署(推荐)

### 1. 安装Docker Desktop

从 https://www.docker.com/products/docker-desktop 下载安装

### 2. 启动服务

```powershell
docker-compose up -d
```

### 3. 查看日志

```powershell
docker-compose logs -f ai-assistant-core
```

### 4. 停止服务

```powershell
docker-compose down
```

## 常见问题

### Q1: 找不到模块 'pydantic_settings'

确保虚拟环境已激活并安装了所有依赖:
```powershell
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### Q2: Qdrant连接失败

如果不使用Docker,需要单独启动Qdrant:
```powershell
docker run -p 6333:6333 qdrant/qdrant
```

或在配置中禁用Qdrant集成

### Q3: MQTT连接失败

如果不使用Docker,需要单独启动Mosquitto:
```powershell
docker run -p 1883:1883 eclipse-mosquitto
```

或在配置中禁用MQTT集成

## 开发建议

- 使用VS Code并安装Python扩展
- 启用自动格式化(black)
- 运行测试: `pytest tests/`
- 代码检查: `flake8 src/`
