"""modified visitor_log model

Revision ID: 649be773c4f2
Revises: e85c77442533
Create Date: 2025-04-15 23:32:14.868874

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '649be773c4f2'
down_revision: Union[str, None] = 'e85c77442533'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'note_list', 'category', ['category_id'], ['id'])
    op.add_column('visitor_log', sa.Column('visitor_id', sa.String(length=64), nullable=False, comment='访客唯一 ID（如 localStorage 中的 UUID）'))
    op.alter_column('visitor_log', 'path',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=300),
               type_=sa.String(length=255),
               existing_comment='访问路径',
               existing_nullable=False)
    op.alter_column('visitor_log', 'referer',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=300),
               type_=sa.String(length=255),
               existing_comment='来源页面',
               existing_nullable=True)
    op.alter_column('visitor_log', 'user_agent',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=512),
               type_=sa.String(length=255),
               existing_comment='User-Agent',
               existing_nullable=True)
    op.create_index(op.f('ix_visitor_log_visitor_id'), 'visitor_log', ['visitor_id'], unique=False)
    op.drop_column('visitor_log', 'os')
    op.drop_column('visitor_log', 'method')
    op.drop_column('visitor_log', 'query')
    op.drop_column('visitor_log', 'country')
    op.drop_column('visitor_log', 'city')
    op.drop_column('visitor_log', 'browser')
    op.drop_column('visitor_log', 'device')
    op.drop_column('visitor_log', 'province')
    op.drop_column('visitor_log', 'status_code')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('visitor_log', sa.Column('status_code', mysql.INTEGER(), autoincrement=False, nullable=False, comment='响应状态码'))
    op.add_column('visitor_log', sa.Column('province', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=64), nullable=True, comment='省份'))
    op.add_column('visitor_log', sa.Column('device', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=64), nullable=True, comment='设备类型'))
    op.add_column('visitor_log', sa.Column('browser', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=64), nullable=True, comment='浏览器'))
    op.add_column('visitor_log', sa.Column('city', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=64), nullable=True, comment='城市'))
    op.add_column('visitor_log', sa.Column('country', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=64), nullable=True, comment='国家'))
    op.add_column('visitor_log', sa.Column('query', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=300), nullable=True, comment='URL 查询参数'))
    op.add_column('visitor_log', sa.Column('method', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=10), nullable=False, comment='请求方法'))
    op.add_column('visitor_log', sa.Column('os', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=64), nullable=True, comment='操作系统'))
    op.drop_index(op.f('ix_visitor_log_visitor_id'), table_name='visitor_log')
    op.alter_column('visitor_log', 'user_agent',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=512),
               existing_comment='User-Agent',
               existing_nullable=True)
    op.alter_column('visitor_log', 'referer',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=300),
               existing_comment='来源页面',
               existing_nullable=True)
    op.alter_column('visitor_log', 'path',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=300),
               existing_comment='访问路径',
               existing_nullable=False)
    op.drop_column('visitor_log', 'visitor_id')
    op.drop_constraint(None, 'note_list', type_='foreignkey')
    # ### end Alembic commands ###
