"""empty message

Revision ID: 30d285e0cad0
Revises: 57b29d2f4c43
Create Date: 2018-03-27 14:49:25.829732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30d285e0cad0'
down_revision = '57b29d2f4c43'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('crawllogs',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('crawl_time', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.Column('source', sa.String(length=50), server_default='', nullable=True),
    sa.Column('job_type', sa.String(length=50), server_default='', nullable=True),
    sa.Column('spend_time', sa.String(length=50), server_default='', nullable=True),
    sa.Column('job_count', sa.String(length=50), server_default='', nullable=True),
    sa.Column('workYear', sa.String(length=50), server_default='', nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_crawllogs_crawl_time'), 'crawllogs', ['crawl_time'], unique=False)
    op.create_table('messages',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('crawl_time', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.Column('message', sa.Text(), server_default='', nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_messages_crawl_time'), 'messages', ['crawl_time'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_messages_crawl_time'), table_name='messages')
    op.drop_table('messages')
    op.drop_index(op.f('ix_crawllogs_crawl_time'), table_name='crawllogs')
    op.drop_table('crawllogs')
    # ### end Alembic commands ###