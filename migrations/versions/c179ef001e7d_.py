"""empty message

Revision ID: c179ef001e7d
Revises: 3220e84ebef1
Create Date: 2019-05-28 11:27:05.357645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c179ef001e7d'
down_revision = '3220e84ebef1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trans_state_table',
    sa.Column('transitions_id', sa.Integer(), nullable=False),
    sa.Column('transition_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['transition_id'], ['transition.id'], ),
    sa.ForeignKeyConstraint(['transitions_id'], ['state.id'], ),
    sa.PrimaryKeyConstraint('transitions_id', 'transition_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trans_state_table')
    # ### end Alembic commands ###
