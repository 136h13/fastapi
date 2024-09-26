"""add content column to posts table

Revision ID: b3b90ca7906c
Revises: 68303ad57993
Create Date: 2024-09-25 14:31:18.027787

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b3b90ca7906c'
down_revision: Union[str, None] = '68303ad57993'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
