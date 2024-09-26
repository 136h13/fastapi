"""add last few columns to posts table

Revision ID: 7f445f0153fa
Revises: eb6f830c9dd1
Create Date: 2024-09-25 15:11:30.399670

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7f445f0153fa'
down_revision: Union[str, None] = 'eb6f830c9dd1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
