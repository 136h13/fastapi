"""create posts table

Revision ID: 68303ad57993
Revises: 
Create Date: 2024-09-25 13:31:57.694689

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '68303ad57993'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


#handles table changes
def upgrade() -> None: 
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable= False, primary_key= True), sa.Column('title', sa.String(), nullable= False))
    pass

#handles rollback
def downgrade() -> None:
    op.drop_table('posts')
    pass
