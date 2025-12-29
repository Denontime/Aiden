"""配置管理模块

使用Pydantic进行类型安全的配置验证,支持从环境变量和YAML文件加载配置。
"""

from typing import Optional, Literal
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()


class ServerConfig(BaseSettings):
    """服务器配置"""
    
    host: str = Field(default="0.0.0.0", description="服务器监听地址")
    port: int = Field(default=8000, description="服务器端口")
    workers: int = Field(default=1, description="工作进程数")
    debug_mode: bool = Field(default=False, description="调试模式")
    
    model_config = SettingsConfigDict(env_prefix="SERVER_")


class DatabaseConfig(BaseSettings):
    """数据库配置"""
    
    url: str = Field(default="sqlite:///./data/aiden.db", description="数据库连接URL")
    echo: bool = Field(default=False, description="是否打印SQL语句")
    pool_size: int = Field(default=5, description="连接池大小")
    max_overflow: int = Field(default=10, description="最大溢出连接数")
    
    model_config = SettingsConfigDict(env_prefix="DATABASE_")


class QdrantConfig(BaseSettings):
    """Qdrant向量数据库配置"""
    
    host: str = Field(default="localhost", description="Qdrant服务器地址")
    port: int = Field(default=6333, description="Qdrant端口")
    collection_memory: str = Field(default="ai_memory", description="记忆集合名称")
    collection_faces: str = Field(default="face_features", description="人脸特征集合名称")
    vector_size: int = Field(default=512, description="向量维度")
    
    model_config = SettingsConfigDict(env_prefix="QDRANT_")


class MQTTConfig(BaseSettings):
    """MQTT配置"""
    
    broker_host: str = Field(default="localhost", description="MQTT Broker地址")
    broker_port: int = Field(default=1883, description="MQTT端口")
    username: Optional[str] = Field(default=None, description="MQTT用户名")
    password: Optional[str] = Field(default=None, description="MQTT密码")
    client_id: str = Field(default="aiden_assistant", description="客户端ID")
    keepalive: int = Field(default=60, description="心跳间隔(秒)")
    
    model_config = SettingsConfigDict(env_prefix="MQTT_")


class JWTConfig(BaseSettings):
    """JWT认证配置"""
    
    secret_key: str = Field(description="JWT密钥")
    algorithm: str = Field(default="HS256", description="加密算法")
    access_token_expire_minutes: int = Field(default=43200, description="访问令牌过期时间(分钟)")
    
    model_config = SettingsConfigDict(env_prefix="JWT_")


class LLMConfig(BaseSettings):
    """大模型API配置"""
    
    provider: Literal["qwen", "glm", "openai"] = Field(default="qwen", description="模型提供商")
    api_key: str = Field(description="API密钥")
    model: str = Field(default="qwen-max", description="模型名称")
    api_base: Optional[str] = Field(default=None, description="API基础URL")
    temperature: float = Field(default=0.7, description="温度参数")
    max_tokens: int = Field(default=2000, description="最大生成token数")
    timeout: int = Field(default=30, description="请求超时时间(秒)")
    
    model_config = SettingsConfigDict(env_prefix="LLM_")


class TTSConfig(BaseSettings):
    """TTS语音合成配置"""
    
    provider: Literal["xunfei", "azure", "edge"] = Field(default="xunfei", description="TTS提供商")
    api_key: Optional[str] = Field(default=None, description="API密钥")
    app_id: Optional[str] = Field(default=None, description="应用ID")
    voice_name: str = Field(default="xiaoyan", description="音色名称")
    speed: int = Field(default=50, description="语速(0-100)")
    volume: int = Field(default=50, description="音量(0-100)")
    pitch: int = Field(default=50, description="音调(0-100)")
    
    model_config = SettingsConfigDict(env_prefix="TTS_")


class MijiaConfig(BaseSettings):
    """米家开放平台配置"""
    
    client_id: Optional[str] = Field(default=None, description="客户端ID")
    client_secret: Optional[str] = Field(default=None, description="客户端密钥")
    redirect_uri: Optional[str] = Field(default=None, description="OAuth回调地址")
    
    model_config = SettingsConfigDict(env_prefix="MIJIA_")


class LogConfig(BaseSettings):
    """日志配置"""
    
    level: str = Field(default="INFO", description="日志级别")
    file_path: str = Field(default="logs/aiden.log", description="日志文件路径")
    rotation: str = Field(default="10 MB", description="日志滚动大小")
    retention: str = Field(default="7 days", description="日志保留时间")
    
    model_config = SettingsConfigDict(env_prefix="LOG_")


class CameraConfig(BaseSettings):
    """摄像头配置"""
    
    device_id: int = Field(default=0, description="摄像头设备ID")
    width: int = Field(default=1280, description="图像宽度")
    height: int = Field(default=720, description="图像高度")
    fps: int = Field(default=30, description="帧率")
    
    model_config = SettingsConfigDict(env_prefix="CAMERA_")


class FaceRecognitionConfig(BaseSettings):
    """人脸识别配置"""
    
    threshold: float = Field(default=0.6, description="识别阈值")
    detection_interval_sec: float = Field(default=1.0, description="检测间隔(秒)")
    model_path: str = Field(default="models/", description="模型文件路径")
    
    model_config = SettingsConfigDict(env_prefix="FACE_RECOGNITION_")


class SystemConfig(BaseSettings):
    """系统配置"""
    
    timezone: str = Field(default="Asia/Shanghai", description="时区")
    language: str = Field(default="zh_CN", description="语言")
    
    model_config = SettingsConfigDict(env_prefix="SYSTEM_")


class Settings(BaseSettings):
    """全局配置"""
    
    server: ServerConfig = Field(default_factory=ServerConfig)
    database: DatabaseConfig = Field(default_factory=DatabaseConfig)
    qdrant: QdrantConfig = Field(default_factory=QdrantConfig)
    mqtt: MQTTConfig = Field(default_factory=MQTTConfig)
    jwt: JWTConfig = Field(default_factory=JWTConfig)
    llm: LLMConfig = Field(default_factory=LLMConfig)
    tts: TTSConfig = Field(default_factory=TTSConfig)
    mijia: MijiaConfig = Field(default_factory=MijiaConfig)
    log: LogConfig = Field(default_factory=LogConfig)
    camera: CameraConfig = Field(default_factory=CameraConfig)
    face_recognition: FaceRecognitionConfig = Field(default_factory=FaceRecognitionConfig)
    system: SystemConfig = Field(default_factory=SystemConfig)
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        case_sensitive=False,
    )


# 全局配置实例
settings = Settings()
