"""empty message

Revision ID: 7019028ca54b
Revises: a6994614eba0
Create Date: 2020-07-14 18:01:22.896665

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7019028ca54b'
down_revision = 'a6994614eba0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('auth', 'add_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('auth', sa.Column('add_time', mysql.DATETIME(), nullable=True))
    # ### end Alembic commands ###