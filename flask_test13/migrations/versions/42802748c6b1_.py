"""empty message

Revision ID: 42802748c6b1
Revises: 9be245a73b57
Create Date: 2020-03-07 16:14:37.530784

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '42802748c6b1'
down_revision = '9be245a73b57'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cat',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('a_name', sa.String(length=16), nullable=True),
    sa.Column('c_legs', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dog',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('a_name', sa.String(length=16), nullable=True),
    sa.Column('d_color', sa.String(length=8), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('animal')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('animal',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('a_name', mysql.VARCHAR(length=16), nullable=True),
    sa.Column('c_legs', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('d_color', mysql.VARCHAR(length=8), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('dog')
    op.drop_table('cat')
    # ### end Alembic commands ###
