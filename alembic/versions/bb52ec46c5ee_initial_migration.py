"""Initial migration

Revision ID: bb52ec46c5ee
Revises: 
Create Date: 2024-08-30 10:40:30.632560

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bb52ec46c5ee'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('author', sa.String(), nullable=True),
    sa.Column('isbn', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_books_author'), 'books', ['author'], unique=False)
    op.create_index(op.f('ix_books_id'), 'books', ['id'], unique=False)
    op.create_index(op.f('ix_books_isbn'), 'books', ['isbn'], unique=True)
    op.create_index(op.f('ix_books_title'), 'books', ['title'], unique=False)
    op.create_table('readers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_readers_email'), 'readers', ['email'], unique=True)
    op.create_index(op.f('ix_readers_first_name'), 'readers', ['first_name'], unique=False)
    op.create_index(op.f('ix_readers_id'), 'readers', ['id'], unique=False)
    op.create_index(op.f('ix_readers_last_name'), 'readers', ['last_name'], unique=False)
    op.create_table('borrows',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reader_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('borrow_date', sa.DateTime(), nullable=True),
    sa.Column('return_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], ),
    sa.ForeignKeyConstraint(['reader_id'], ['readers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_borrows_id'), 'borrows', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_borrows_id'), table_name='borrows')
    op.drop_table('borrows')
    op.drop_index(op.f('ix_readers_last_name'), table_name='readers')
    op.drop_index(op.f('ix_readers_id'), table_name='readers')
    op.drop_index(op.f('ix_readers_first_name'), table_name='readers')
    op.drop_index(op.f('ix_readers_email'), table_name='readers')
    op.drop_table('readers')
    op.drop_index(op.f('ix_books_title'), table_name='books')
    op.drop_index(op.f('ix_books_isbn'), table_name='books')
    op.drop_index(op.f('ix_books_id'), table_name='books')
    op.drop_index(op.f('ix_books_author'), table_name='books')
    op.drop_table('books')
    # ### end Alembic commands ###
