"""add user table

Revision ID: 1baee8c2c9b3
Revises: f89c3496fe40
Create Date: 2022-12-27 22:35:52.777379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1baee8c2c9b3'
down_revision = 'f89c3496fe40'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String, nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                            server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
