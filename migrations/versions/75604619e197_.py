"""empty message

Revision ID: 75604619e197
Revises: 5b763af0a4c7
Create Date: 2021-08-25 20:03:32.017118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75604619e197'
down_revision = '5b763af0a4c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todolists', 'completed')
    op.add_column('todos', sa.Column('complete', sa.Boolean(), nullable=False))
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.drop_column('todos', 'complete')
    op.add_column('todolists', sa.Column('completed', sa.BOOLEAN(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
