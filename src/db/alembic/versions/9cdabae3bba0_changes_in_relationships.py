"""changes in relationships

Revision ID: 9cdabae3bba0
Revises: f1b2b03eb424
Create Date: 2023-12-05 12:09:37.040431

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9cdabae3bba0"
down_revision: Union[str, None] = "f1b2b03eb424"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###