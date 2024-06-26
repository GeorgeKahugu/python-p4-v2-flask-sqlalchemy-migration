"""rename address

Revision ID: b416231dae2a
Revises: 4c71e9ac60d5
Create Date: 2024-06-26 19:17:24.649187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b416231dae2a'
down_revision = '4c71e9ac60d5'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('departments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('location', sa.String(), nullable=True))
        batch_op.drop_column('address')
    op.alter_column('departments', 'address',  new_column_name='location')

def downgrade():
    with op.batch_alter_table('departments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('location')
    op.alter_column('departments', 'location',  new_column_name='address')