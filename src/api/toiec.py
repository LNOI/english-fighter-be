from uuid import UUID, uuid4
from fastapi import APIRouter, Depends, HTTPException
from src.model.toiec import Toiec, PartToiec, QuestionToiec, GroupQuestion, ConfigToiec
from src.utils.db import get_session, Session
from sqlmodel import select
from pydantic import BaseModel
from enum import Enum

router = APIRouter(prefix="/toiec", tags=["Toiec"])


class ToiecType(str, Enum):
    LISTENING = "LISTENING"
    READING = "READING"
    WRITING = "WRITING"
    SPEAKING = "SPEAKING"
    LISTENING_READING = "LISTENING_READING"
    WRITING_SPEAKING = "WRITING_SPEAKING"


class ToiecInput(BaseModel):
    name: str
    description: str
    level: str
    total_part: int
    total_questions: int
    total_time: int
    type_toiec: str
    author: str


class PartToiecInput(BaseModel):
    toiec_id: UUID
    part: int
    name: str
    directions: str


class GroupQuestionInput(BaseModel):
    name: str
    question_text: str | None = None
    question_audio: str | None = None


class QuestionToiecInput(BaseModel):
    order: int
    question_text: str | None = None
    question_audio: str | None = None
    answer_choices: str | None = None
    correct_answer: str | None = None
    type_input: str = "TEXT"
    type_toiec: str | None = None
    suggest_answer: str | None = None


@router.post("/")
async def create_toiec(input: ToiecInput, db: Session = Depends(get_session)):
    """
    Create Toiec
    """
    toiec = Toiec(
        name=input.name,
        description=input.description,
        level=input.level,
        total_part=input.total_part,
        total_questions=input.total_questions,
        total_time=input.total_time,
        author=input.author,
        type_toiec=input.type_toiec,
    )
    db.add(toiec)
    db.commit()
    db.refresh(toiec)
    return toiec


class ConfigToiecInput(BaseModel):
    name: str
    type: ToiecType
    audio: str | None = None
    image: str | None = None
    description: str | None = None
    extend_config: str | None = None
    default: bool = False


@router.get("/")
async def list_toiec(db: Session = Depends(get_session)):
    """
    List Toiec
    """
    return db.scalars(select(Toiec)).all()


@router.post("/config")
async def create_config_toiec(
    input: ConfigToiecInput, db: Session = Depends(get_session)
):
    """
    Create Config Toiec
    """
    config = ConfigToiec(
        name=input.name,
        type=input.type.value,
        audio=input.audio,
        image=input.image,
        description=input.description,
        extend_config=input.extend_config,
        default=input.default,
    )
    db.add(config)
    db.commit()
    db.refresh(config)
    return config


@router.get("/{toiec_id}")
async def get_toiec(toiec_id: UUID, db: Session = Depends(get_session)):
    """
    Get Toiec
    """
    toiec = db.get(Toiec, toiec_id)
    if toiec is None:
        raise HTTPException(status_code=404, detail="Toiec not found")

    parts = db.scalars(select(PartToiec).where(PartToiec.toiec_id == toiec_id)).all()
    if not parts:
        raise HTTPException(status_code=404, detail="Parts not found")

    groups = db.scalars(
        select(GroupQuestion).where(GroupQuestion.toiec_id == toiec_id)
    ).all()
    if not groups:
        raise HTTPException(status_code=404, detail="Groups not found")

    questions = db.scalars(
        select(QuestionToiec).where(QuestionToiec.toiec_id == toiec_id)
    ).all()
    if not questions:
        raise HTTPException(status_code=404, detail="Questions not found")

    # combine all data
    data = {
        "id": toiec.id,
    }


@router.get("/config/{type}/default")
async def get_default_config_toiec(db: Session = Depends(get_session)):
    """
    Get Default Config Toiec
    """
    query = select(ConfigToiec).where(ConfigToiec.default)
    return db.scalars(query).first()


@router.post("/{toiec_id}/part")
async def create_part_toiec(
    toiec_id: str, part: PartToiecInput, db: Session = Depends(get_session)
):
    """
    Create Part Toiec
    """
    part = PartToiec(
        toiec_id=toiec_id,
        part=part.part,
        name=part.name,
        directions=part.directions,
    )
    db.add(part)
    db.commit()
    db.refresh(part)
    return part


@router.post("/{toiec_id}/part/{part_id}/group")
async def create_group_question_toiec(
    toiec_id: str,
    part_id: str,
    input: GroupQuestionInput,
    db: Session = Depends(get_session),
):
    """
    Create Group Question Toiec
    """
    group = GroupQuestion(
        toiec_id=toiec_id,
        part_id=part_id,
        name=input.name,
        question_text=input.question_text,
        question_audio=input.question_audio,
    )
    db.add(group)
    db.commit()
    db.refresh(group)
    return group


@router.post("/{toiec_id}/part/{part_id}/group/{group_id}/question")
async def create_question_toiec(
    toiec_id: UUID,
    part_id: UUID,
    group_id: UUID,
    question: QuestionToiecInput,
    db: Session = Depends(get_session),
):
    """
    Create Question Toiec
    """
    question = QuestionToiec(
        toiec_id=toiec_id,
        part_id=part_id,
        group_id=group_id,
        order=question.order,
        question_text=question.question_text,
        question_audio=question.question_audio,
        answer_choices=question.answer_choices,
        correct_answer=question.correct_answer,
        type_input=question.type_input,
        type_toiec=question.type_toiec,
        suggest_answer=question.suggest_answer,
    )
    db.add(question)
    db.commit()
    db.refresh(question)
    return question


def convert_data_database_to_json(questions):
    converted_data = {}
    for q in questions:
        if "id" not in converted_data:
            converted_data["id"] = q.id
            converted_data["title"] = q.title
            converted_data["description"] = q.description
            converted_data["level"] = q.level
            converted_data["type_toiec"] = q.type_toiec
            converted_data["author"] = q.author
            converted_data["parts"] = []

        if len(converted_data["parts"]) < q["part"]:
            converted_data["parts"].append(
                {
                    "part": q["part"],
                    "title": q["title"],
                    "directions": q["directions"],
                    "groups": [],
                }
            )

        group = filter(lambda x: x["id"] == q[""], converted_data["parts"]["groups"])


@router.get("/type/{type_toiec}")
async def list_toiec_by_type(
    type_toiec: str, page: int = 1, db: Session = Depends(get_session)
):
    """
    List Toiec by Type
    """
    query = (
        select(Toiec)
        .where(Toiec.type_toiec == type_toiec)
        .offset((page - 1) * 10)
        .limit(10)
    )
    return db.scalars(query).all()


# Load all parts of a Toiec
@router.get("/{toiec_id}/part")
async def list_parts_of_toiec(toiec_id: UUID, db: Session = Depends(get_session)):
    """
    List Parts of Toiec
    """
    query = select(PartToiec).where(PartToiec.toiec_id == toiec_id)
    return db.scalars(query).all()
