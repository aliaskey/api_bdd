"""Message de migration

Revision ID: 958ecf0c6814
Revises: 49bfdef45da8
Create Date: 2024-08-30 14:06:23.971899

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '958ecf0c6814'
down_revision: Union[str, None] = '49bfdef45da8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
