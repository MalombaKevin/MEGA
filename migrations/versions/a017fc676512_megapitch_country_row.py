"""Megapitch Country row

Revision ID: a017fc676512
Revises: 2107ec4cc810
Create Date: 2022-05-13 13:48:26.117168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a017fc676512'
down_revision = '2107ec4cc810'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roles')
    op.add_column('megapitch', sa.Column('country', sa.String(length=255), nullable=True))
    op.drop_constraint('users_role_id_fkey', 'users', type_='foreignkey')
    op.drop_column('users', 'role_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('users_role_id_fkey', 'users', 'roles', ['role_id'], ['id'])
    op.drop_column('megapitch', 'country')
    op.create_table('roles',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='roles_pkey')
    )
    # ### end Alembic commands ###
