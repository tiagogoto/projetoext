"""empty message

Revision ID: 06ec0502ae13
Revises: c765fb0d3ab8
Create Date: 2024-10-29 20:03:51.764357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06ec0502ae13'
down_revision = 'c765fb0d3ab8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('institution', schema=None) as batch_op:
        batch_op.add_column(sa.Column('country_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'country', ['country_id'], ['id'])
        batch_op.drop_column('country')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('institution', schema=None) as batch_op:
        batch_op.add_column(sa.Column('country', sa.INTEGER(), nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'country', ['country'], ['id'])
        batch_op.drop_column('country_id')

    # ### end Alembic commands ###
