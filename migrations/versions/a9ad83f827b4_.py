"""empty message

Revision ID: a9ad83f827b4
Revises: 0b3820577be9
Create Date: 2019-05-28 12:06:50.329253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9ad83f827b4'
down_revision = '0b3820577be9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trans_state_table')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trans_state_table',
    sa.Column('transitions_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('transition_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['transition_id'], ['transition.id'], name='trans_state_table_transition_id_fkey'),
    sa.ForeignKeyConstraint(['transitions_id'], ['transition.id'], name='trans_state_table_transitions_id_fkey'),
    sa.PrimaryKeyConstraint('transitions_id', 'transition_id', name='trans_state_table_pkey')
    )
    # ### end Alembic commands ###