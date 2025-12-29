"""Qdrant向量数据库客户端"""

from typing import List, Optional
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

from src.core import settings, log


class QdrantService:
    """Qdrant向量数据库服务"""
    
    def __init__(self):
        """初始化Qdrant客户端"""
        try:
            self.client = QdrantClient(
                host=settings.qdrant.host,
                port=settings.qdrant.port,
            )
            self._ensure_collections()
            log.info("Qdrant向量数据库连接成功")
        except Exception as e:
            log.warning(f"Qdrant连接失败: {e},向量数据库功能将不可用")
            self.client = None
    
    def _ensure_collections(self):
        """确保集合存在"""
        collections = self.client.get_collections().collections
        collection_names = [c.name for c in collections]
        
        # 创建记忆集合
        if settings.qdrant.collection_memory not in collection_names:
            self.client.create_collection(
                collection_name=settings.qdrant.collection_memory,
                vectors_config=VectorParams(
                    size=settings.qdrant.vector_size,
                    distance=Distance.COSINE
                )
            )
            log.info(f"创建记忆集合: {settings.qdrant.collection_memory}")
        
        # 创建人脸特征集合
        if settings.qdrant.collection_faces not in collection_names:
            self.client.create_collection(
                collection_name=settings.qdrant.collection_faces,
                vectors_config=VectorParams(
                    size=settings.qdrant.vector_size,
                    distance=Distance.COSINE
                )
            )
            log.info(f"创建人脸特征集合: {settings.qdrant.collection_faces}")
    
    def add_memory(self, memory_id: str, vector: List[float], payload: dict):
        """添加记忆向量"""
        if not self.client:
            log.warning("向量数据库不可用,跳过记忆添加")
            return
        self.client.upsert(
            collection_name=settings.qdrant.collection_memory,
            points=[
                PointStruct(
                    id=memory_id,
                    vector=vector,
                    payload=payload
                )
            ]
        )
    
    def search_memory(self, query_vector: List[float], limit: int = 5) -> List[dict]:
        """搜索相似记忆"""
        results = self.client.search(
            collection_name=settings.qdrant.collection_memory,
            query_vector=query_vector,
            limit=limit
        )
        return [
            {
                "id": r.id,
                "score": r.score,
                "payload": r.payload
            }
            for r in results
        ]
    
    def add_face(self, face_id: str, vector: List[float], payload: dict):
        """添加人脸特征向量"""
        self.client.upsert(
            collection_name=settings.qdrant.collection_faces,
            points=[
                PointStruct(
                    id=face_id,
                    vector=vector,
                    payload=payload
                )
            ]
        )
    
    def search_face(self, query_vector: List[float], threshold: float = 0.6) -> Optional[dict]:
        """搜索匹配的人脸"""
        results = self.client.search(
            collection_name=settings.qdrant.collection_faces,
            query_vector=query_vector,
            limit=1
        )
        if results and results[0].score >= threshold:
            return {
                "id": results[0].id,
                "score": results[0].score,
                "payload": results[0].payload
            }
        return None
    
    def delete_memory(self, memory_id: str):
        """删除记忆"""
        self.client.delete(
            collection_name=settings.qdrant.collection_memory,
            points_selector=[memory_id]
        )
    
    def delete_face(self, face_id: str):
        """删除人脸特征"""
        self.client.delete(
            collection_name=settings.qdrant.collection_faces,
            points_selector=[face_id]
        )


# 全局Qdrant服务实例
qdrant_service = QdrantService()
