"""create_table_charging_session

Revision ID: 6b72aae31e05
Revises: 
Create Date: 2023-12-21 08:20:02.394194

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b72aae31e05'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'charging_session',
        sa.Column('id', sa.Integer()),
        sa.Column('session_id', sa.Integer()),
        sa.Column('energy_delivered_in_kWh', sa.Integer()),
        sa.Column('duration_in_seconds', sa.Integer()),
        sa.Column('session_cost_in_cents', sa.Integer()),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('charging_session')
