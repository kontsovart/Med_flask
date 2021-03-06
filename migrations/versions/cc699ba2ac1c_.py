"""empty message

Revision ID: cc699ba2ac1c
Revises: cdabec659614
Create Date: 2019-05-28 11:13:09.187765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc699ba2ac1c'
down_revision = 'cdabec659614'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('prev_state',
    sa.Column('prev_states_id', sa.Integer(), nullable=False),
    sa.Column('prev_state_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['prev_state_id'], ['state.id'], ),
    sa.ForeignKeyConstraint(['prev_states_id'], ['state.id'], ),
    sa.PrimaryKeyConstraint('prev_states_id', 'prev_state_id')
    )
    op.drop_table('trans_state')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trans_state',
    sa.Column('transitions_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('transition_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['transition_id'], ['transition.id'], name='trans_state_transition_id_fkey'),
    sa.ForeignKeyConstraint(['transitions_id'], ['state.id'], name='trans_state_transitions_id_fkey'),
    sa.PrimaryKeyConstraint('transitions_id', 'transition_id', name='trans_state_pkey')
    )
    op.drop_table('prev_state')
    # ### end Alembic commands ###
