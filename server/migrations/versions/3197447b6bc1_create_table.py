"""create table

Revision ID: 3197447b6bc1
Revises: 08eea8813053
Create Date: 2023-07-11 20:01:14.254513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3197447b6bc1'
down_revision = '08eea8813053'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('showroom_customer', schema=None) as batch_op:
        batch_op.drop_constraint('showroom_customer_showroom_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'showroom', ['showroom_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('showroom_customer', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('showroom_customer_showroom_id_fkey', 'showroom', ['showroom_id'], ['id'])

    # ### end Alembic commands ###