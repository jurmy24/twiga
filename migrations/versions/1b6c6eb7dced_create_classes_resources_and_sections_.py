"""create classes_resources and sections table

Revision ID: 1b6c6eb7dced
Revises: fc271252a164
Create Date: 2024-10-30 20:55:13.216954

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '1b6c6eb7dced'
down_revision: Union[str, None] = 'fc271252a164'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('classes_resources',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('class_id', sa.Integer(), nullable=False),
    sa.Column('resource_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['class_id'], ['classes.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['resource_id'], ['resources.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_classes_resources_class_id'), 'classes_resources', ['class_id'], unique=False)
    op.create_index(op.f('ix_classes_resources_resource_id'), 'classes_resources', ['resource_id'], unique=False)
    op.create_table('sections',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('resource_id', sa.Integer(), nullable=False),
    sa.Column('parent_section_id', sa.Integer(), nullable=True),
    sa.Column('section_index', sqlmodel.sql.sqltypes.AutoString(length=20), nullable=True),
    sa.Column('section_title', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=True),
    sa.Column('section_type', sqlmodel.sql.sqltypes.AutoString(length=15), nullable=True),
    sa.Column('section_order', sa.Integer(), nullable=False),
    sa.Column('page_range', sa.ARRAY(sa.Integer()), nullable=True),
    sa.Column('summary', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['parent_section_id'], ['sections.id'], ),
    sa.ForeignKeyConstraint(['resource_id'], ['resources.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sections_resource_id'), 'sections', ['resource_id'], unique=False)
    op.add_column('resources', sa.Column('subjects', sa.ARRAY(sa.String(length=50)), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('resources', 'subjects')
    op.drop_index(op.f('ix_sections_resource_id'), table_name='sections')
    op.drop_table('sections')
    op.drop_index(op.f('ix_classes_resources_resource_id'), table_name='classes_resources')
    op.drop_index(op.f('ix_classes_resources_class_id'), table_name='classes_resources')
    op.drop_table('classes_resources')
    # ### end Alembic commands ###
