"""description of changes

Revision ID: 14ba81d6e303
Revises: ed0aff52a4a5
Create Date: 2025-02-09 01:58:30.094083

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '14ba81d6e303'
down_revision: Union[str, None] = 'ed0aff52a4a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reports', sa.Column('title', sa.String(), nullable=True))
    op.add_column('reports', sa.Column('description', sa.String(), nullable=True))
    op.add_column('reports', sa.Column('self_report', sa.Boolean(), nullable=True))
    op.drop_column('reports', 'schedule_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reports', sa.Column('schedule_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('reports', 'self_report')
    op.drop_column('reports', 'description')
    op.drop_column('reports', 'title')
    # ### end Alembic commands ###
