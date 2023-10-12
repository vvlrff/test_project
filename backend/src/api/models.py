# from sqlalchemy import BIGINT, TIMESTAMP, MetaData, Table, Column, Integer, Text

# metadata = MetaData()


# News_data = Table(
#     'news_data',
#     metadata,
#     Column('tg_data_id', Integer, primary_key=True),
#     Column('message_id', Integer),
#     Column('sender', Text),
#     Column('chat_title', Text),
#     Column('date', TIMESTAMP),
#     Column('message', Text),
#     Column('photo_id', BIGINT),
# )