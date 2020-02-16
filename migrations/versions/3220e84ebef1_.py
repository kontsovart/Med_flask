"""empty message

Revision ID: 3220e84ebef1
Revises: cc699ba2ac1c
Create Date: 2019-05-28 11:17:03.663165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3220e84ebef1'
down_revision = 'cc699ba2ac1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('prev_state_table',
    sa.Column('prev_states_id', sa.Integer(), nullable=False),
    sa.Column('prev_state_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['prev_state_id'], ['state.id'], ),
    sa.ForeignKeyConstraint(['prev_states_id'], ['state.id'], ),
    sa.PrimaryKeyConstraint('prev_states_id', 'prev_state_id')
    )
    op.drop_table('prev_state')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('prev_state',
    sa.Column('prev_states_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('prev_state_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['prev_state_id'], ['state.id'], name='prev_state_prev_state_id_fkey'),
    sa.ForeignKeyConstraint(['prev_states_id'], ['state.id'], name='prev_state_prev_states_id_fkey'),
    sa.PrimaryKeyConstraint('prev_states_id', 'prev_state_id', name='prev_state_pkey')
    )
    op.drop_table('prev_state_table')
    # ### end Alembic commands ###
