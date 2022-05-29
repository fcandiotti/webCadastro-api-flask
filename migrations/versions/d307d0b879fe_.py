"""empty message

Revision ID: d307d0b879fe
Revises: 34c533c95ad5
Create Date: 2022-05-29 00:19:13.056684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd307d0b879fe'
down_revision = '34c533c95ad5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario', sa.Column('is_admin', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuario', 'is_admin')
    # ### end Alembic commands ###
