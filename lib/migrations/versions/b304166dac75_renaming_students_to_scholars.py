"""Renaming students to scholars

Revision ID: b304166dac75
Revises: 791279dd0760
Create Date: 2025-03-22 00:07:14.240545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b304166dac75'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
