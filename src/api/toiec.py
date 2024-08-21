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
    title: str
    description: str
    level: str
    author: str
    type_toiec: str


@router.post("/")
async def create_toiec(toiec: ToiecInput, db: Session = Depends(get_session)):
    """
    Create Toiec
    """
    toiec = Toiec(
        title=toiec.title,
        description=toiec.description,
        level=toiec.level,
        author=toiec.author,
        type_toiec=toiec.type_toiec,
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
    # Get all questions attributes
    query = (
        select(Toiec, PartToiec, GroupQuestion, QuestionToiec)
        .where(
            Toiec.id == toiec_id,
            PartToiec.toiec_id == toiec_id,
            GroupQuestion.toiec_id == toiec_id,
            QuestionToiec.toiec_id == toiec_id,
        )
        .order_by(QuestionToiec.order)
    )
    results = db.exec(query)

    data = {}
    for toiec, part, group, question in results:
        if "id" not in data:
            data["id"] = toiec.id
            data["title"] = toiec.title
            data["description"] = toiec.description
            data["level"] = toiec.level
            data["type_toiec"] = toiec.type_toiec
            data["author"] = toiec.author
            data["parts"] = []

        if len(data["parts"]) < part.part:
            data["parts"].append(
                {
                    "part": part.part,
                    "title": part.title,
                    "directions": part.directions,
                    "groups": [],
                }
            )

        exist_index = -1
        for g in data["parts"][-1]["groups"]:
            if g["id"] == group.id:
                exist_index = data["parts"][-1]["groups"].index(g)
                break

        if exist_index == -1:
            data["parts"][-1]["groups"].append(
                {
                    "id": group.id,
                    "title": group.title,
                    "question": group.question,
                    "questions": [],
                }
            )
            exist_index = 0

        data["parts"][-1]["groups"][exist_index]["questions"].append(
            {
                "id": question.id,
                "order": question.order,
                "question": question.question,
                "type_input": question.type_input,
                "type_toiec": question.type_toiec,
                "direction": question.direction,
                "audio": question.audio,
                "list_answer": question.list_answer,
                "suggest_answer": question.suggest_answer,
            }
        )
        # print(toiec, part, group, question)
    return data


@router.get("/config/{type}/default")
async def get_default_config_toiec(db: Session = Depends(get_session)):
    """
    Get Default Config Toiec
    """
    query = select(ConfigToiec).where(ConfigToiec.default)
    return db.scalars(query).first()


class PartToiecInput(BaseModel):
    toiec_id: UUID
    part: int
    title: str
    directions: str


# Create config toiec


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
        title=part.title,
        directions=part.directions,
    )
    db.add(part)
    db.commit()
    db.refresh(part)
    return part


class GroupQuestionInput(BaseModel):
    toiec_id: UUID
    part_id: UUID
    title: str
    question: str


@router.post("/{toiec_id}/part/{part_id}/group")
async def create_group_question_toiec(
    toiec_id: str,
    part_id: str,
    group: GroupQuestionInput,
    db: Session = Depends(get_session),
):
    """
    Create Group Question Toiec
    """
    group = GroupQuestion(
        toiec_id=toiec_id,
        part_id=part_id,
        title=group.title,
        question=group.question,
    )
    db.add(group)
    db.commit()
    db.refresh(group)
    return group


class QuestionToiecInput(BaseModel):
    order: int
    question: str
    type_input: str
    type_toiec: str | None = None
    direction: str | None = None
    audio: str | None = None
    list_answer: str
    suggest_answer: str


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
        question=question.question,
        type_input=question.type_input,
        type_toiec=question.type_toiec,
        direction=question.direction,
        audio=question.audio,
        list_answer=question.list_answer,
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


# Load all Toiec by type and Pagaing
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
