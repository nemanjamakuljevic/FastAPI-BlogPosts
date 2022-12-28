"""add foreign-key to posts table

Revision ID: 4da37f669390
Revises: 1baee8c2c9b3
Create Date: 2022-12-27 22:45:09.053915

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4da37f669390'
down_revision = '1baee8c2c9b3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users",
    local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('posts-users-fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
