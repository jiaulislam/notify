from enum import Enum


class APIStatusEnum(str, Enum):
    ALIVE = "alive"
    DEAD = "dead"
    UPGRDATION_ONGOING = "upgradation ongoing"


class MsgTypeEnum(str, Enum):
    LAPSED = "lapsed"
    NO_DUE = "no_due"
    PREMIUM_PAID = "premium_paid"
