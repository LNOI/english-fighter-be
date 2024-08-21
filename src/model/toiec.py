from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, Relationship
from enum import Enum
from datetime import datetime


class ToiecLevel(str, Enum):
    A1 = "A1"
    A2 = "A2"
    B1 = "B1"
    B2 = "B2"
    C1 = "C1"
    C2 = "C2"


class TypeQuestion(str, Enum):
    AUDIO = "AUDIO"
    TEXT = "TEXT"


class ConfigToiec(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str
    type: str
    audio: str | None = None
    image: str | None = None
    description: str | None = None
    updated_at: datetime = Field(default_factory=datetime.now)
    deleted_at: datetime | None = None
    default: bool = False
    extend_config: str | None = None


class ToiecType(str, Enum):
    LISTENING = "LISTENING"
    READING = "READING"
    WRITING = "WRITING"
    SPEAKING = "SPEAKING"
    LISTENING_READING = "LISTENING_READING"
    WRITING_SPEAKING = "WRITING_SPEAKING"


class QuestionToiec(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    toiec_id: UUID = Field(foreign_key="toiec.id")
    part_id: UUID = Field(foreign_key="parttoiec.id")
    group_id: UUID = Field(foreign_key="groupquestion.id")
    order: int
    question: str
    type_input: str = TypeQuestion.TEXT
    type_toiec: str
    direction: str | None = None
    audio: str | None = None
    list_answer: str | None = None
    suggest_answer: str | None = None
    updated_at: datetime = Field(default_factory=datetime.now)
    deleted_at: datetime | None = None


class GroupQuestion(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    title: str
    toiec_id: UUID = Field(foreign_key="toiec.id")
    part_id: UUID = Field(foreign_key="parttoiec.id")
    question: str | None = None
    updated_at: datetime = Field(default_factory=datetime.now)
    deleted_at: datetime | None = None


class Toiec(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    title: str
    description: str | None = None
    level: str
    type_toiec: str
    author: str | None = None
    updated_at: datetime = Field(default_factory=datetime.now)
    deleted_at: datetime | None = None


class PartToiec(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    toiec_id: UUID = Field(foreign_key="toiec.id")
    part: int
    directions: str | None = None
    updated_at: datetime = Field(default_factory=datetime.now)
    deleted_at: datetime | None = None


# Listening and Reading have 7 parts
# First call endpoint -> get a toiec test ->
