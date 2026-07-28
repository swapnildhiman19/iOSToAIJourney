"""create_tasks_table
Revision ID: 0001
Revises: 
Create Date: 2026-07-28
"""

from typing import Sequence, Union
import alembic.op as op 
import sqlalchemy as sa

revision: str = '0001'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        'tasks',
        sa.Column('task_id', sa.UUID(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.UniqueConstraint('title', name='uq_tasks_title')
    )
def downgrade() -> None:
    op.drop_table('tasks')