"""description

Revision ID: e85c77442533
Revises: c45ecf5bcc1e
Create Date: 2025-04-14 16:11:13.812462

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e85c77442533'
down_revision: Union[str, None] = 'c45ecf5bcc1e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('category_id', table_name='note_list')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('category_id', 'note_list', ['category_id'], unique=True)
    # ### end Alembic commands ###
