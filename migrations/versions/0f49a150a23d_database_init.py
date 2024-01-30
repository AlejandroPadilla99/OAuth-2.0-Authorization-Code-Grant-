"""database_init

Revision ID: 0f49a150a23d
Revises: 
Create Date: 2024-01-30 12:41:50.771256

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0f49a150a23d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    statements = [
        """
        CREATE TABLE IF NOT EXISTS users (
            uuid TEXT PRIMARY KEY NOT NULL,
            username VARCHAR NOT NULL,
            password VARCHAR NOT NULL,
            email VARCHAR NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            deleted_at TIMESTAMP DEFAULT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS tokens (
            user_uuid TEXT REFERENCES users(uuid),
            access_token VARCHAR,
            refresh_token VARCHAR,
            code VARCHAR,
            UNIQUE (user_uuid)
        );
        """,
        """
        INSERT INTO users (uuid, username, password, email)
        VALUES ('550e8400-e29b-41d4-a716-446655440000', 'test_user', 'test', 'test@gmail.com');
        """
    ]

    for statement in statements:
        op.execute(statement) 



def downgrade() -> None:
    pass
