"""add user table

Revision ID: 9c3d13d7caff
Revises: b3b90ca7906c
Create Date: 2024-09-25 14:43:31.767384

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9c3d13d7caff'
down_revision: Union[str, None] = 'b3b90ca7906c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
