from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import  JSON, Boolean, Column, ForeignKey, Integer, MetaData, Sequence, String,DateTime, Table

from ..datebase import Base


metadata = MetaData()

role = Table(
    'role',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('permissions', JSON),

)

user = Table(
    'user',
    metadata,
    Column("id", Integer, primary_key=True),
    Column('name', String),
    Column('email', String),
    Column('hashed_pass', String),
    Column('register_at', DateTime, default=datetime.utcnow),
    Column('role_id', Integer, ForeignKey("role.id")),
    Column('is_active',Boolean, default=True, nullable=False),
    Column('is_superuser',Boolean, default=False, nullable=False),
    Column('is_verified',Boolean, default=False, nullable=False)

)

class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    name : str = Column('name', String)
    email : str = Column('email', String)
    hashed_password : str = Column('hashed_pass', String(length=1024), nullable=False)
    is_active : bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
    register_at: DateTime = Column('register_at', DateTime, default=datetime.utcnow)
    role_id: int = Column('role_id', Integer, ForeignKey(role.c.id))
