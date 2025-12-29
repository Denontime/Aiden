# Aiden - 智能AI管家系统

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 项目简介

Aiden是一个基于边缘计算的智能AI管家系统,部署在家庭环境中,通过云端大模型API实现自然语言理解,结合本地的记忆管理、人脸识别、日程管理、智能家居控制等能力,为用户提供有温度的智能助理服务。

### 核心特性

- 🎤 **语音交互**: 支持唤醒词激活和连续对话,低延迟响应(<3秒)
- 👤 **人脸识别**: 本地实时人脸检测和识别,提供个性化问候
- 🧠 **记忆管理**: 维护短期和长期记忆,基于向量检索提供上下文
- 📅 **日程管理**: 语音创建日程,智能冲突检测和主动提醒
- 🏠 **智能家居**: 集成MQTT、米家开放平台、小爱同学语音桥接
- 🔌 **插件扩展**: 支持自定义插件和MCP协议接口

## 技术架构

### 核心技术栈

- **后端框架**: FastAPI + Uvicorn
- **数据库**: SQLite (关系数据) + Qdrant (向量数据)
- **AI/ML**: InsightFace (人脸识别) + Whisper (ASR)
- **消息队列**: MQTT (Mosquitto)
- **任务调度**: APScheduler
- **日志**: Loguru

### 系统架构

```
├── 语音交互层 (ASR + TTS + 唤醒词检测)
├── 视觉感知层 (人脸检测 + 人脸识别)
├── 业务逻辑层 (对话管理 + 记忆管理 + 日程管理)
├── 设备控制层 (MQTT + 米家 + 小爱)
└── 数据持久层 (SQLite + Qdrant)
```

## 快速开始

### 环境要求

- Python 3.10+
- Docker & Docker Compose (可选)
- 树莓派5 或 英伟达Jetson Orin Nano (推荐)

### 本地开发

1. **克隆项目**

```bash
git clone https://github.com/yourusername/Aiden.git
cd Aiden
```

2. **创建虚拟环境**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **安装依赖**

```bash
pip install -r requirements.txt
```

4. **配置环境变量**

```bash
cp .env.example .env
# 编辑.env文件,填入必要的API密钥
```

5. **初始化数据库**

```bash
python -c "from src.models import init_db; init_db()"
```

6. **启动服务**

```bash
python src/main.py
```

访问 http://localhost:8000/docs 查看API文档

### Docker部署

```bash
# 构建并启动所有服务
docker-compose up -d

# 查看日志
docker-compose logs -f

# 停止服务
docker-compose down
```

## 项目结构

```
Aiden/
├── src/
│   ├── api/              # API路由和Schema
│   │   ├── routes/       # 路由文件
│   │   └── schemas/      # Pydantic模型
│   ├── core/             # 核心配置
│   │   ├── config.py     # 配置管理
│   │   └── logger.py     # 日志配置
│   ├── models/           # 数据模型
│   │   ├── user.py       # 用户模型
│   │   ├── schedule.py   # 日程模型
│   │   ├── device.py     # 设备模型
│   │   └── ...
│   ├── services/         # 业务逻辑服务
│   ├── utils/            # 工具函数
│   ├── plugins/          # 插件目录
│   └── main.py           # 应用入口
├── config/               # 配置文件
├── data/                 # 数据目录
├── logs/                 # 日志目录
├── tests/                # 测试文件
├── docker-compose.yml    # Docker编排
├── Dockerfile            # Docker镜像
├── requirements.txt      # Python依赖
└── README.md             # 项目说明
```

## 配置说明

主要配置项在`.env`文件中,包括:

- **服务器配置**: 端口、调试模式
- **数据库配置**: SQLite路径、Qdrant连接
- **大模型API**: 阿里云通义千问/智谱GLM/OpenAI
- **TTS配置**: 讯飞语音/Azure TTS
- **MQTT配置**: Broker地址和认证
- **米家配置**: OAuth认证信息
- **摄像头配置**: 设备ID、分辨率、帧率
- **人脸识别**: 识别阈值、模型路径

详细配置请参考`.env.example`

## API文档

启动服务后访问:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### 主要API端点

- `GET /api/users` - 获取用户列表
- `POST /api/users` - 创建用户
- `GET /api/schedules` - 获取日程
- `POST /api/schedules` - 创建日程
- `GET /api/devices` - 获取设备列表
- `GET /api/conversations` - 获取对话历史

## 开发路线图

### 第一阶段 (已完成)

- [x] 项目框架搭建
- [x] 数据库模型设计
- [x] FastAPI后台框架
- [x] Docker部署配置

### 第二阶段 (进行中)

- [ ] 语音交互模块
- [ ] 人脸识别模块
- [ ] 日程管理完整实现
- [ ] 记忆管理系统

### 第三阶段 (计划中)

- [ ] MQTT设备控制
- [ ] 米家开放平台接入
- [ ] 小爱同学语音桥接

### 第四阶段 (未来)

- [ ] 插件机制
- [ ] MCP协议接口
- [ ] 性能优化
- [ ] Web管理界面

## 贡献指南

欢迎提交Issue和Pull Request!

1. Fork本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启Pull Request

## 许可证

本项目采用MIT许可证 - 详见 [LICENSE](LICENSE) 文件

## 致谢

- [FastAPI](https://fastapi.tiangolo.com/) - 现代Web框架
- [InsightFace](https://github.com/deepinsight/insightface) - 人脸识别
- [Qdrant](https://qdrant.tech/) - 向量数据库
- [Whisper](https://github.com/openai/whisper) - 语音识别

## 联系方式

- 项目主页: https://github.com/yourusername/Aiden
- 问题反馈: https://github.com/yourusername/Aiden/issues

---

**注意**: 本项目仍在开发中,部分功能尚未完成。欢迎Star和关注项目进展!
