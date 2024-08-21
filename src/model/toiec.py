from uuid import UUID, uuid4
from sqlmodel import Field, Relationship
from enum import Enum
from datetime import datetime
from src.model.base import BaseModel


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


class ToiecType(str, Enum):
    LISTENING = "LISTENING"
    READING = "READING"
    WRITING = "WRITING"
    SPEAKING = "SPEAKING"
    LISTENING_READING = "LISTENING_READING"
    WRITING_SPEAKING = "WRITING_SPEAKING"


class ConfigToiec(BaseModel, table=True):
    name: str
    type: str
    audio: str | None = None
    image: str | None = None
    description: str | None = None
    default: bool = False
    extend_config: str | None = None


class QuestionToiec(BaseModel, table=True):
    toiec_id: UUID = Field(foreign_key="toiec.id")
    part_id: UUID = Field(foreign_key="parttoiec.id")
    group_id: UUID = Field(foreign_key="groupquestion.id")
    order: int = Field(min_items=1, max_items=200)
    question_text: str
    question_audio: str | None = None
    answer_choices: str | None = None
    correct_answer: str | None = None  # A, B, C, D
    type_input: str = TypeQuestion.TEXT
    type_toiec: str
    suggest_answer: str | None = None


class Toiec(BaseModel, table=True):
    name: str
    description: str | None = None
    level: str
    type_toiec: str
    total_part: int
    total_questions: int
    total_time: int
    author: str | None = None


class PartToiec(BaseModel, table=True):
    name: str
    toiec_id: UUID = Field(foreign_key="toiec.id")
    part: int
    directions: str | None = None


class GroupQuestion(BaseModel, table=True):
    name: str
    toiec_id: UUID = Field(foreign_key="toiec.id")
    part_id: UUID = Field(foreign_key="parttoiec.id")
    question_text: str | None = None
    question_audio: str | None = None
