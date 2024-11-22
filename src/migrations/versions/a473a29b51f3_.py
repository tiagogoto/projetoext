"""empty message

Revision ID: a473a29b51f3
Revises: 17d7455d545f
Create Date: 2024-11-21 17:56:08.123420

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a473a29b51f3'
down_revision = '17d7455d545f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('meeting_minute', schema=None) as batch_op:
        batch_op.add_column(sa.Column('endtime', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('quorum', sa.Integer(), nullable=False))
        batch_op.alter_column('aproved_date',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('recorded_by',
               existing_type=sa.TEXT(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('meeting_minute', schema=None) as batch_op:
        batch_op.alter_column('recorded_by',
               existing_type=sa.TEXT(),
               nullable=False)
        batch_op.alter_column('aproved_date',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.drop_column('quorum')
        batch_op.drop_column('endtime')

    # ### end Alembic commands ###
