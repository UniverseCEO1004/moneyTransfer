"""Optimizing the new AuditorSettings for faster setup, queries, pagination, and filtering.

Revision ID: 595e27f36454
Revises: 57f648d4b597
Create Date: 2015-02-14 00:16:25.590209

"""

# revision identifiers, used by Alembic.
revision = '595e27f36454'
down_revision = '57f648d4b597'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('auditorsettings', sa.Column('issue_text', sa.String(length=512), nullable=True))
    op.drop_column('auditorsettings', 'notes')
    op.drop_column('auditorsettings', 'issue')
    op.add_column('itemaudit', sa.Column('auditor_setting_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'itemaudit', 'auditorsettings', ['auditor_setting_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'itemaudit', type_='foreignkey')
    op.drop_column('itemaudit', 'auditor_setting_id')
    op.add_column('auditorsettings', sa.Column('issue', sa.VARCHAR(length=512), autoincrement=False, nullable=False))
    op.add_column('auditorsettings', sa.Column('notes', sa.VARCHAR(length=512), autoincrement=False, nullable=True))
    op.drop_column('auditorsettings', 'issue_text')
    ### end Alembic commands ###
