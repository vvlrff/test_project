from sqlalchemy import BIGINT, TIMESTAMP, MetaData, Table, Column, Integer, String, JSON, Text

metadata = MetaData()

NEWS_DATA = Table(
    'news_data',
    metadata,
    Column('tg_data_id', Integer, primary_key=True),
    Column('message_id', Integer),
    Column('sender', Text),
    Column('chat_title', Text),
    Column('date', TIMESTAMP),
    Column('message', Text),
    Column('photo_id', BIGINT),
)

CHANNELS_TG = Table(
    'channels_tg',
    metadata,
    Column()
)