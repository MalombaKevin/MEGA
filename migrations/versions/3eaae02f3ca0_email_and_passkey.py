"""email and passkey

Revision ID: 3eaae02f3ca0
Revises: 5216178a0091
Create Date: 2022-05-11 00:49:33.224218

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3eaae02f3ca0'
down_revision = '5216178a0091'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    op.drop_column('users', 'pass_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_hash', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###
