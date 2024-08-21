from typing import Any, Dict, Tuple
from uuid import UUID, uuid4
from datetime import datetime
from sqlmodel import SQLModel, Field


class BaseModel(SQLModel):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    updated_at: datetime = Field(default_factory=datetime.now)
    deleted_at: datetime | None = None
