"""init table

Revision ID: 1891bee64e51
Revises: 
Create Date: 2024-08-17 20:45:46.605656

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '1891bee64e51'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('toiec',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('level', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('type_toiec', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('author', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('parttoiec',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('toiec_id', sa.Uuid(), nullable=False),
    sa.Column('part', sa.Integer(), nullable=False),
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('directions', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['toiec_id'], ['toiec.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('questiontoiec',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('toiec_id', sa.Uuid(), nullable=False),
    sa.Column('order', sa.Integer(), nullable=False),
    sa.Column('question', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('type_input', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('type_toiec', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('direction', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('audio', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('list_answer', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('suggest_answer', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['toiec_id'], ['parttoiec.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('questiontoiec')
    op.drop_table('parttoiec')
    op.drop_table('toiec')
    # ### end Alembic commands ###
