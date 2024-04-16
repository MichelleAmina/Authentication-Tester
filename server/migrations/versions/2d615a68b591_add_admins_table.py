"""add admins table

Revision ID: 2d615a68b591
Revises: 
Create Date: 2024-04-16 07:30:34.395273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d615a68b591'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('company_name', sa.String(), nullable=True),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('confirm_password', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('admins')
    # ### end Alembic commands ###
