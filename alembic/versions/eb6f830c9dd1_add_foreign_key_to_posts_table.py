"""add foreign key to posts table

Revision ID: eb6f830c9dd1
Revises: 9c3d13d7caff
Create Date: 2024-09-25 15:02:42.258210

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eb6f830c9dd1'
down_revision: Union[str, None] = '9c3d13d7caff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
