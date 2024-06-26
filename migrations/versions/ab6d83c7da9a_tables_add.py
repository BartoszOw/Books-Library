"""Tables add

Revision ID: ab6d83c7da9a
Revises: 
Create Date: 2024-04-06 17:26:35.146880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab6d83c7da9a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=200), nullable=True),
    sa.Column('sec_name', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('author', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_author_first_name'), ['first_name'], unique=False)
        batch_op.create_index(batch_op.f('ix_author_sec_name'), ['sec_name'], unique=False)

    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('genre', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_book_name'), ['name'], unique=True)

    op.create_table('author_book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('loan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_author_id', sa.Integer(), nullable=True),
    sa.Column('borrower_name', sa.String(length=100), nullable=True),
    sa.Column('borrower_date', sa.Text(), nullable=True),
    sa.Column('return_date', sa.Text(), nullable=True),
    sa.Column('returned', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['book_author_id'], ['author_book.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('return',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('loan_id', sa.Integer(), nullable=True),
    sa.Column('returned_date', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['loan_id'], ['loan.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('return')
    op.drop_table('loan')
    op.drop_table('author_book')
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_book_name'))

    op.drop_table('book')
    with op.batch_alter_table('author', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_author_sec_name'))
        batch_op.drop_index(batch_op.f('ix_author_first_name'))

    op.drop_table('author')
    # ### end Alembic commands ###
