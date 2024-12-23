"""empty message

Revision ID: bc6bcb27dc82
Revises: ccbf80a38eb9
Create Date: 2024-11-07 21:20:30.221803

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc6bcb27dc82'
down_revision = 'ccbf80a38eb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('attendees', schema=None) as batch_op:
        batch_op.add_column(sa.Column('course_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_course', 'course', ['course_id'], ['id'])

    with op.batch_alter_table('meeting_agenda', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.Boolean(), nullable=True))

    with op.batch_alter_table('meeting_attendees', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('meeting_attendees', schema=None) as batch_op:
        batch_op.drop_column('status')

    with op.batch_alter_table('meeting_agenda', schema=None) as batch_op:
        batch_op.drop_column('status')

    with op.batch_alter_table('attendees', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('course_id')

    # ### end Alembic commands ###
