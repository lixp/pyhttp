# coding: utf-8
from sqlalchemy import Column, String, BIGINT
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TiantianBook(Base):
    __tablename__ = 'tiantian_book'

    id = Column(INTEGER(11), primary_key=True)
    status = Column(INTEGER(11), nullable=False)
    manufactureStatus = Column(INTEGER(4), nullable=False)
    manufactureAdminId = Column(INTEGER(4), nullable=False)
    type = Column(INTEGER(11), nullable=False)
    authorizationType = Column(INTEGER(4), nullable=False)
    crType = Column(INTEGER(4), nullable=False)
    bookSeriesId = Column(INTEGER(11), nullable=False)
    cpId = Column(INTEGER(4), nullable=False)
    info = Column(String(512), nullable=False)
    brief = Column(String(512))
    abbreviation = Column(String(512), nullable=False)
    lessons = Column(String(1024), nullable=False)
    suggestLevel = Column(INTEGER(8), nullable=False)
    coverUrl = Column(String(512), nullable=False)
    coverLandscapeUrl = Column(String(512), nullable=False)
    idx = Column(INTEGER(8), nullable=False)
    studyCount = Column(INTEGER(8), nullable=False)
    topicCount = Column(INTEGER(8), nullable=False)
    questionCount = Column(INTEGER(8), nullable=False)
    pageCount = Column(INTEGER(8), nullable=False)
    aheadViewLessonCount = Column(INTEGER(8), nullable=False)
    enableAutoEvaluation = Column(String(32), nullable=False)
    createTime = Column(BIGINT, nullable=False)
    editable = Column(String(8), nullable=False)
    consumeValue = Column(INTEGER(8), nullable=False)
    consumeBookType = Column(INTEGER(8), nullable=False)
    consumeBookTypeName = Column(String(32), nullable=False)
    bookConfig = Column(String(2048))
    addStatus = Column(String(32), nullable=False)
    needClassLock = Column(String(32), nullable=False)
    commonLock = Column(String(32), nullable=False)
    bookSectionMenuBookRelId = Column(INTEGER(8), nullable=False)
    crConfig = Column(String(2048), nullable=False)
    qbQuestionCount = Column(INTEGER(8), nullable=False)
    isVIP = Column(String(8), nullable=False)
    searchTags = Column(String(30))

    def row2dict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = str(getattr(self, column.name))
        return d
