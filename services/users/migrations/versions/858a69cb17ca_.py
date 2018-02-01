"""empty message

Revision ID: 858a69cb17ca
Revises: 
Create Date: 2018-02-01 10:41:25.514275

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '858a69cb17ca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'users', ['username'])
    op.create_unique_constraint(None, 'users', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'users', type_='unique')
    # ### end Alembic commands ###
