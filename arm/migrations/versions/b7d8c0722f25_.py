"""empty message

Revision ID: b7d8c0722f25
Revises: 
Create Date: 2019-01-23 22:26:24.846696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7d8c0722f25'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('job',
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('arm_version', sa.String(length=20), nullable=True),
    sa.Column('crc_id', sa.String(length=63), nullable=True),
    sa.Column('logfile', sa.String(length=256), nullable=True),
    sa.Column('disc', sa.String(length=63), nullable=True),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('stop_time', sa.DateTime(), nullable=True),
    sa.Column('job_length', sa.String(length=12), nullable=True),
    sa.Column('status', sa.String(length=32), nullable=True),
    sa.Column('no_of_titles', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=256), nullable=True),
    sa.Column('title_auto', sa.String(length=256), nullable=True),
    sa.Column('title_manual', sa.String(length=256), nullable=True),
    sa.Column('year', sa.String(length=4), nullable=True),
    sa.Column('year_auto', sa.String(length=4), nullable=True),
    sa.Column('year_manual', sa.String(length=4), nullable=True),
    sa.Column('video_type', sa.String(length=20), nullable=True),
    sa.Column('video_type_auto', sa.String(length=20), nullable=True),
    sa.Column('video_type_manual', sa.String(length=20), nullable=True),
    sa.Column('imdb_id', sa.String(length=15), nullable=True),
    sa.Column('imdb_id_auto', sa.String(length=15), nullable=True),
    sa.Column('imdb_id_manual', sa.String(length=15), nullable=True),
    sa.Column('poster_url', sa.String(length=256), nullable=True),
    sa.Column('poster_url_auto', sa.String(length=256), nullable=True),
    sa.Column('poster_url_manual', sa.String(length=256), nullable=True),
    sa.Column('devpath', sa.String(length=15), nullable=True),
    sa.Column('mountpoint', sa.String(length=20), nullable=True),
    sa.Column('hasnicetitle', sa.Boolean(), nullable=True),
    sa.Column('errors', sa.Text(), nullable=True),
    sa.Column('disctype', sa.String(length=20), nullable=True),
    sa.Column('label', sa.String(length=256), nullable=True),
    sa.Column('ejected', sa.Boolean(), nullable=True),
    sa.Column('updated', sa.Boolean(), nullable=True),
    sa.Column('pid', sa.Integer(), nullable=True),
    sa.Column('pid_hash', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('job_id')
    )
    op.create_table('track',
    sa.Column('track_id', sa.Integer(), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.Column('track_number', sa.String(length=4), nullable=True),
    sa.Column('length', sa.Integer(), nullable=True),
    sa.Column('aspect_ratio', sa.String(length=20), nullable=True),
    sa.Column('blocks', sa.Integer(), nullable=True),
    sa.Column('fps', sa.Float(), nullable=True),
    sa.Column('playlist', sa.String(length=5), nullable=True),
    sa.Column('main_feature', sa.Boolean(), nullable=True),
    sa.Column('basename', sa.String(length=256), nullable=True),
    sa.Column('filename', sa.String(length=256), nullable=True),
    sa.Column('orig_filename', sa.String(length=256), nullable=True),
    sa.Column('new_filename', sa.String(length=256), nullable=True),
    sa.Column('ripped', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['job.job_id'], ),
    sa.PrimaryKeyConstraint('track_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('track')
    op.drop_table('job')
    # ### end Alembic commands ###
