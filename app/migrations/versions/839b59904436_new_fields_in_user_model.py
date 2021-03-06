"""new fields in user model

Revision ID: 839b59904436
Revises: dedbfeadf734
Create Date: 2018-10-05 02:43:18.047575

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '839b59904436'
down_revision = 'dedbfeadf734'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
