"""empty message

Revision ID: 32b882f6095d
Revises: d43377062b47
Create Date: 2024-10-28 14:29:27.329820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32b882f6095d'
down_revision = 'd43377062b47'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('country',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('acronym', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('institution',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('acronym', sa.Text(), nullable=False),
    sa.Column('country', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['country'], ['country.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('department',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('acronym', sa.Text(), nullable=False),
    sa.Column('inst_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['inst_id'], ['institution.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('course',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('depart_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['depart_id'], ['department.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('permissions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.Text(), nullable=False))
        batch_op.drop_column('descricao')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('permissions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('descricao', sa.TEXT(), nullable=False))
        batch_op.drop_column('description')

    op.drop_table('course')
    op.drop_table('department')
    op.drop_table('institution')
    op.drop_table('country')
    # ### end Alembic commands ###