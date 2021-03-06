"""add todo model

Revision ID: f2ef9b571677
Revises: 409ccb7f0ad1
Create Date: 2019-03-12 15:24:41.621079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2ef9b571677'
down_revision = '409ccb7f0ad1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(), nullable=True),
    sa.Column('done', sa.Integer(), nullable=True),
    sa.Column('ct', sa.DateTime(), nullable=True),
    sa.Column('finished_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todo')
    # ### end Alembic commands ###
