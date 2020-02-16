"""empty message

Revision ID: 0b3820577be9
Revises: 707d5ca1b4bd
Create Date: 2019-05-28 11:39:51.793500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b3820577be9'
down_revision = '707d5ca1b4bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('state', sa.Column('transitions_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'state', 'transition', ['transitions_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'state', type_='foreignkey')
    op.drop_column('state', 'transitions_id')
    # ### end Alembic commands ###