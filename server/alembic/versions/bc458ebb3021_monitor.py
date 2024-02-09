"""monitor

Revision ID: bc458ebb3021
Revises: c34dcd11b329
Create Date: 2024-02-05 19:55:04.977070

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc458ebb3021'
down_revision: Union[str, None] = 'c34dcd11b329'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('videoinfo', sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('videoinfo', 'updated_at')
    # ### end Alembic commands ###
