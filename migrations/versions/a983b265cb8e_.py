"""empty message

Revision ID: a983b265cb8e
Revises: 5c7e912cea7a
Create Date: 2019-01-23 21:54:09.549548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a983b265cb8e'
down_revision = '5c7e912cea7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('article', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'article')
    # ### end Alembic commands ###
