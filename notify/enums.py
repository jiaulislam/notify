from enum import Enum


class APIStatusEnum(str, Enum):
    ALIVE = "alive"
    DEAD = "dead"
    UPGRDATION_ONGOING = "upgradation ongoing"
