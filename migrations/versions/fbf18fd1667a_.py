"""empty message

Revision ID: fbf18fd1667a
Revises: e0de25225847
Create Date: 2019-05-27 16:42:08.940658

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbf18fd1667a'
down_revision = 'e0de25225847'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('state', 'prev_states_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('state', 'transitions_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('state', 'transitions_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('state', 'prev_states_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###