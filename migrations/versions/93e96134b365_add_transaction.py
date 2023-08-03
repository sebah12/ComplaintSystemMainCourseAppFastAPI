"""add transaction

Revision ID: 93e96134b365
Revises: ae4134588efe
Create Date: 2023-08-03 17:25:08.743064

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93e96134b365'
down_revision = 'ae4134588efe'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quote_id', sa.String(length=120), nullable=False),
    sa.Column('transfer_id', sa.Integer(), nullable=False),
    sa.Column('target_account_id', sa.String(length=100), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('complaint_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['complaint_id'], ['complaints.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    # ### end Alembic commands ###
