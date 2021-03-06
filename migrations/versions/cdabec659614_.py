"""empty message

Revision ID: cdabec659614
Revises: ddd8ab94e4a9
Create Date: 2019-05-28 11:10:45.888658

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cdabec659614'
down_revision = 'ddd8ab94e4a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trans_state',
    sa.Column('transitions_id', sa.Integer(), nullable=False),
    sa.Column('transition_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['transition_id'], ['transition.id'], ),
    sa.ForeignKeyConstraint(['transitions_id'], ['state.id'], ),
    sa.PrimaryKeyConstraint('transitions_id', 'transition_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trans_state')
    # ### end Alembic commands ###
