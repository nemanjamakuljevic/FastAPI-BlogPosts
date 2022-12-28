"""add content column to post table

Revision ID: f89c3496fe40
Revises: 6436cd41503e
Create Date: 2022-12-27 21:52:03.017387

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f89c3496fe40'
down_revision = '6436cd41503e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
