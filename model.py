import os

from sqlalchemy import (JSON, Column, DateTime, ForeignKey, Integer, String,
                        Unicode, create_engine, DATETIME)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.sql.sqltypes import BigInteger, Boolean

SQL_URI = 'sqlite:///db.sqlite'
engine = create_engine(SQL_URI)
Base = declarative_base()
session = scoped_session(sessionmaker(
    autocommit=False, autoflush=True, bind=None))
session.configure(bind=engine)


class Profile(Base):
    __tablename__ = 'profile'
    id = Column(Unicode, primary_key=True)
    created = Column(DATETIME)
    updated = Column(DATETIME)
    city = Column(Unicode)
    first_name = Column(Unicode)
    last_name = Column(Unicode)
    headline = Column(Unicode)
    state = Column(Unicode)
    summary = Column(Unicode)


class Course(Base):
    __tablename__ = 'course'
    name = Column(Unicode)
    number = Column(Unicode)
    profile_id = Column(Unicode, ForeignKey(Profile.id))
    id = Column(String, primary_key=True)


class Education(Base):
    __tablename__ = 'education'
    id = Column(String, primary_key=True)
    created = Column(DATETIME)
    updated = Column(DATETIME)
    starts_at = Column(DATETIME)
    ends_at = Column(DATETIME)
    field_of_study = Column(Unicode)
    degree_name = Column(Unicode)
    school = Column(Unicode)
    school_profile_url = Column(Unicode)
    profile_id = Column(Unicode, ForeignKey(Profile.id))


class Experience(Base):
    __tablename__ = 'experience'
    id = Column(String, primary_key=True)
    created = Column(DATETIME)
    updated = Column(DATETIME)
    starts_at = Column(DATETIME)
    ends_at = Column(DATETIME)
    company = Column(Unicode)
    company_profile_url = Column(Unicode)
    title = Column(Unicode)
    location = Column(Unicode)
    profile_id = Column(Unicode, ForeignKey(Profile.id))
    description = Column(Unicode)


class HonourAward(Base):
    __tablename__ = 'honour_award'
    id = Column(String, primary_key=True)
    created = Column(DATETIME)
    updated = Column(DATETIME)
    title = Column(Unicode)
    issuer = Column(Unicode)
    issued_on = Column(DATETIME)
    description = Column(Unicode)
    profile_id = Column(Unicode, ForeignKey(Profile.id))


class Language(Base):
    __tablename__ = 'language'
    id = Column(String, primary_key=True)
    created = Column(DATETIME)
    updated = Column(DATETIME)
    profile_id = Column(Unicode, ForeignKey(Profile.id))
    name = Column(Unicode)


class Organization(Base):
    __tablename__ = 'organization'
    id = Column(String, primary_key=True)
    created = Column(DATETIME)
    updated = Column(DATETIME)
    profile_id = Column(Unicode, ForeignKey(Profile.id))
    starts_at = Column(DATETIME)
    ends_at = Column(DATETIME)
    name = Column(Unicode)
    title = Column(Unicode)
    description = Column(Unicode)


class Patent(Base):
    __tablename__ = 'patent'
    id = Column(String, primary_key=True)
    created = Column(DATETIME)
    updated = Column(DATETIME)
    profile_id = Column(Unicode, ForeignKey(Profile.id))
    title = Column(Unicode)
    description = Column(Unicode)
    url = Column(Unicode)
    issued_on = Column(DATETIME)
    issuer = Column(Unicode)
    patent_number = Column(Unicode)


class Project(Base):
    __tablename__ = 'project'
    id = Column(String, primary_key=True)
    created = Column(DATETIME)
    updated = Column(DATETIME)
    profile_id = Column(Unicode, ForeignKey(Profile.id))
    title = Column(Unicode)
    description = Column(Unicode)
    url = Column(Unicode)


class Publication(Base):
    __tablename__ = 'publication'
    id = Column(String, primary_key=True)
    created = Column(DATETIME)
    updated = Column(DATETIME)
    profile_id = Column(Unicode, ForeignKey(Profile.id))
    name = Column(Unicode)
    publisher = Column(Unicode)
    published_on = Column(DATETIME)
    description = Column(Unicode)
    url = Column(Unicode)


class TestScore(Base):
    __tablename__ = 'test_score'
    id = Column(String, primary_key=True)
    created = Column(DATETIME)
    updated = Column(DATETIME)
    profile_id = Column(Unicode, ForeignKey(Profile.id))
    name = Column(Unicode)
    score = Column(Unicode)
    date_on = Column(DATETIME)
    description = Column(Unicode)


class VolunteeringExperience(Base):
    __tablename__ = 'volunteering_experience'
    id = Column(String, primary_key=True)
    created = Column(DATETIME)
    updated = Column(DATETIME)
    profile_id = Column(Unicode, ForeignKey(Profile.id))
    starts_at = Column(DATETIME)
    ends_at = Column(DATETIME)
    cause = Column(Unicode)
    company = Column(Unicode)
    company_profile_url = Column(Unicode)
    title = Column(Unicode)
    location = Column(Unicode)
