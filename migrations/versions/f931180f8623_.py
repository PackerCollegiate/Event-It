"""empty message

Revision ID: f931180f8623
Revises: c1181938b826
Create Date: 2023-05-23 12:23:40.157708

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f931180f8623'
down_revision = 'c1181938b826'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscribers',
    sa.Column('subscriber_id', sa.Integer(), nullable=True),
    sa.Column('subscribed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['subscribed_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['subscriber_id'], ['user.id'], )
    )
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('image')

    op.drop_table('subscribers')
    # ### end Alembic commands ###
