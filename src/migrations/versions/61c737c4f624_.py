"""empty message

Revision ID: 61c737c4f624
Revises: 7246a9e8cc2c
Create Date: 2024-11-23 14:25:36.267530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61c737c4f624'
down_revision = '7246a9e8cc2c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('meetings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('meetings', schema=None) as batch_op:
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###
