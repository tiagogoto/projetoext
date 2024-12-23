"""empty message

Revision ID: 7246a9e8cc2c
Revises: a473a29b51f3
Create Date: 2024-11-23 12:33:50.535077

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7246a9e8cc2c'
down_revision = 'a473a29b51f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('organization',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('acronym', sa.Text(), nullable=True),
    sa.Column('logo', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('institution', schema=None) as batch_op:
        batch_op.add_column(sa.Column('logo', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('institution', schema=None) as batch_op:
        batch_op.drop_column('logo')

    op.drop_table('organization')
    # ### end Alembic commands ###
