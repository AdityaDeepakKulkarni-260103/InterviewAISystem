from alembic import op
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

revision = '001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('modules',
        Column('id', Integer, primary_key=True),
        Column('name', String(50), unique=True, nullable=False),
        Column('description', String(200), nullable=True)
    )

    op.create_table('module_info',
        Column('id', Integer, primary_key=True),
        Column('module_id', Integer, ForeignKey('modules.id'), nullable=False),
        Column('version', String(20), nullable=False),
        Column('release_date', DateTime, nullable=False)
    )

    op.create_table('users',
        Column('id', Integer, primary_key=True),
        Column('username', String(50), unique=True, nullable=False),
        Column('email', String(120), unique=True, nullable=False),
        Column('password', String(128), nullable=False)
    )

def downgrade():
    op.drop_table('users')
    op.drop_table('module_info')
    op.drop_table('modules')