# coding: utf-8
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, MEDIUMTEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TiantianBookInfo(Base):
    __tablename__ = 'tiantian_book_info'

    id = Column(INTEGER(11), primary_key=True)
    status = Column(INTEGER(11))
    manufactureStatus = Column(INTEGER(4))
    manufactureAdminId = Column(INTEGER(4))
    type = Column(INTEGER(11))
    authorizationType = Column(INTEGER(4))
    crType = Column(INTEGER(4))
    bookSeriesId = Column(INTEGER(11))
    cpId = Column(INTEGER(4))
    info = Column(String(512))
    brief = Column(String(512))
    abbreviation = Column(String(512))
    suggestLevel = Column(INTEGER(8))
    coverUrl = Column(String(512))
    coverLandscapeUrl = Column(String(512))
    idx = Column(INTEGER(8))
    studyCount = Column(INTEGER(8))
    topicCount = Column(INTEGER(8))
    questionCount = Column(INTEGER(8))
    pageCount = Column(INTEGER(8))
    aheadViewLessonCount = Column(INTEGER(8))
    enableAutoEvaluation = Column(String(32))
    createTime = Column(BIGINT(255))
    editable = Column(String(8))
    consumeValue = Column(INTEGER(255))
    consumeBookType = Column(INTEGER(8))
    consumeBookTypeName = Column(String(32))
    addStatus = Column(String(32))
    needClassLock = Column(String(32))
    commonLock = Column(String(32))
    bookSectionMenuBookRelId = Column(INTEGER(8))
    qbQuestionCount = Column(INTEGER(8))
    isVIP = Column(String(8))
    searchTags = Column(String(30))
    lessons = Column(MEDIUMTEXT)
    crConfig = Column(MEDIUMTEXT)
    tags = Column(MEDIUMTEXT)
    bookConfig = Column(MEDIUMTEXT)
    lessonGroups = Column(MEDIUMTEXT)
