"""empty message

Revision ID: ca732ea1bff2
Revises: 2bf54ea1af90
Create Date: 2019-03-07 18:24:22.984002

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ca732ea1bff2'
down_revision = '2bf54ea1af90'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('active', sa.Boolean(), nullable=True))
    op.drop_column('user', 'status')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('status', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.drop_column('user', 'active')
    # ### end Alembic commands ###