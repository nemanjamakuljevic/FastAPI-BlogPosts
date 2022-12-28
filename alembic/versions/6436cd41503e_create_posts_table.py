"""create posts table

Revision ID: 6436cd41503e
Revises: 
Create Date: 2022-12-27 21:37:27.538460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6436cd41503e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
