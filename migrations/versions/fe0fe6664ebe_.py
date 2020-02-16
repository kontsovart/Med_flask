"""empty message

Revision ID: fe0fe6664ebe
Revises: c22f33bb1140
Create Date: 2019-05-24 16:01:14.931795

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fe0fe6664ebe'
down_revision = 'c22f33bb1140'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('prev_state',
    sa.Column('prev_states_id', sa.Integer(), nullable=True),
    sa.Column('state_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['prev_states_id'], ['state.id'], ),
    sa.ForeignKeyConstraint(['state_id'], ['state.id'], )
    )
    op.create_table('trans_state',
    sa.Column('transitions_id', sa.Integer(), nullable=True),
    sa.Column('transition_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['transition_id'], ['transition.id'], ),
    sa.ForeignKeyConstraint(['transitions_id'], ['state.id'], )
    )
    op.drop_table('results')
    op.drop_constraint('state_transitions_fkey', 'state', type_='foreignkey')
    op.drop_constraint('state_prev_states_fkey', 'state', type_='foreignkey')
    op.drop_column('state', 'transitions')
    op.drop_column('state', 'prev_states')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('state', sa.Column('prev_states', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('state', sa.Column('transitions', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('state_prev_states_fkey', 'state', 'state', ['prev_states'], ['id'])
    op.create_foreign_key('state_transitions_fkey', 'state', 'transition', ['transitions'], ['id'])
    op.create_table('results',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('url', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('result_all', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('result_no_stop_words', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='results_pkey')
    )
    op.drop_table('trans_state')
    op.drop_table('prev_state')
    # ### end Alembic commands ###