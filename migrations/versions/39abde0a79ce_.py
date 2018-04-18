"""empty message

Revision ID: 39abde0a79ce
Revises: e3b8ac109a67
Create Date: 2018-04-16 20:49:22.048686

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39abde0a79ce'
down_revision = 'e3b8ac109a67'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('description', sa.String(length=100), server_default='', nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('roles', 'description')
    # ### end Alembic commands ###