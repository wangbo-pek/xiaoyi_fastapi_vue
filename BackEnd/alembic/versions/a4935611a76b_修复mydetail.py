"""修复mydetail

Revision ID: a4935611a76b
Revises: 890a4c345956
Create Date: 2025-04-13 23:55:42.525434

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'a4935611a76b'
down_revision: Union[str, None] = '890a4c345956'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('my_detail', sa.Column('name', sa.String(length=32), nullable=False, comment='名字'))
    op.add_column('my_detail', sa.Column('nickname', sa.String(length=32), nullable=False, comment='昵称'))
    op.alter_column('my_detail', 'full_intro',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100),
               type_=sa.String(length=300),
               existing_comment='我的完整介绍',
               existing_nullable=False)
    op.alter_column('my_detail', 'wisdom',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100),
               type_=sa.String(length=500),
               existing_comment='我的智慧语句',
               existing_nullable=False)
    op.drop_column('my_detail', 'career')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('my_detail', sa.Column('career', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100), nullable=False, comment='我的职业'))
    op.alter_column('my_detail', 'wisdom',
               existing_type=sa.String(length=500),
               type_=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100),
               existing_comment='我的智慧语句',
               existing_nullable=False)
    op.alter_column('my_detail', 'full_intro',
               existing_type=sa.String(length=300),
               type_=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100),
               existing_comment='我的完整介绍',
               existing_nullable=False)
    op.drop_column('my_detail', 'nickname')
    op.drop_column('my_detail', 'name')
    # ### end Alembic commands ###
