from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

# Статусы проверки правила (FED-05): только "allowed" попадает в выдачу (ROD-04).
RULE_STATUS_ALLOWED = "allowed"
RULE_STATUS_PENDING = "pending_review"
RULE_STATUS_REJECTED = "rejected"


class Parameter(Base):
    """Параметр сетапа. Каноническое имя — единый словарь VAR-02."""

    __tablename__ = "parameters"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    unit = Column(String, nullable=False)
    influence_description = Column(String, nullable=False)
    limitations = Column(String, nullable=True)

    rules = relationship("Rule", back_populates="parameter")


class Rule(Base):
    """Экспертное правило: симптом/условие → изменение параметра → эффект/ограничение.

    Схема соответствует шаблону VAR-03 и ER-диаграмме docs/diagrams/data-model.puml.
    """

    __tablename__ = "rules"

    id = Column(Integer, primary_key=True)
    symptom_condition = Column(String, nullable=False)
    parameter_id = Column(Integer, ForeignKey("parameters.id"), nullable=False)
    direction = Column(String, nullable=False)  # "increase" | "decrease"
    effect = Column(String, nullable=False)
    limitations = Column(String, nullable=True)
    applicability = Column(String, nullable=True)
    status = Column(String, nullable=False, default=RULE_STATUS_PENDING)
    basis = Column(String, nullable=True)

    parameter = relationship("Parameter", back_populates="rules")
