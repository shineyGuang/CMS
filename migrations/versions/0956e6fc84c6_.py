"""empty message

Revision ID: 0956e6fc84c6
Revises: b76ee8509390
Create Date: 2020-07-21 00:02:33.596641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0956e6fc84c6'
down_revision = 'b76ee8509390'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'create_time')
    # ### end Alembic commands ###