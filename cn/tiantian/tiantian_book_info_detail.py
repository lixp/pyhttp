# coding: utf-8
from sqlalchemy import Column, Float, String
from sqlalchemy.dialects.mysql import INTEGER, MEDIUMTEXT, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TiantianBookInfoDetail(Base):
    __tablename__ = 'tiantian_book_info_detail'

    id = Column(INTEGER(255))
    idx = Column(INTEGER(255))
    info = Column(String(512))
    status = Column(INTEGER(255))
    type = Column(INTEGER(255))
    mode = Column(INTEGER(255))
    bookId = Column(INTEGER(255))
    coverUrl = Column(String(512))
    hwDesc = Column(String(512))
    topics = Column(MEDIUMTEXT)
    canBeAnswered = Column(TINYINT(1))
    enableAutoEvaluation = Column(TINYINT(1))
    iflyExcellentThreshold = Column(Float)
    iflyGoodThreshold = Column(Float)
    iflyScoreMapX1 = Column(Float)
    iflyScoreMapY1 = Column(Float)
    iflyScoreMapX2 = Column(Float)
    iflyScoreMapY2 = Column(Float)
    suggestScoreCalcType = Column(INTEGER(11))
    studentScoreShowType = Column(INTEGER(11))
    studentScoreCommentThresholds = Column(MEDIUMTEXT)
    crType = Column(INTEGER(11))
    hwConfig = Column(MEDIUMTEXT)
    crConfig = Column(MEDIUMTEXT)
    topicId = Column(INTEGER(255), primary_key=True)
    lessonId = Column(INTEGER(255))
