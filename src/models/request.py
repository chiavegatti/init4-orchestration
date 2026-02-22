import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text, Numeric
from sqlalchemy.dialects.postgresql import UUID
from src.db.base import Base


class RequestLog(Base):
    __tablename__ = "requests"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)
    tenant_id = Column(String, nullable=True, index=True)
    task_type = Column(String, nullable=False, index=True)
    requested_model = Column(String, nullable=True)
    routed_model = Column(String, nullable=False)
    input_tokens = Column(Integer, default=0, nullable=False)
    output_tokens = Column(Integer, default=0, nullable=False)
    estimated_cost = Column(Numeric(10, 6), default=0.0, nullable=False)
    latency_ms = Column(Integer, default=0, nullable=False)
    status = Column(String, nullable=False, index=True)
    error_message = Column(Text, nullable=True)
