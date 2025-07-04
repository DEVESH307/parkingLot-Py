from parkingLot.src.models.models import SlotAssignmentStrategyEum
from parkingLot.src.strategy.randomSlotFindingStrategy import RandomSlotFindingStrategy


class SlotFactory:
    @staticmethod
    def get_slot_strategy_object(slot_assignment_strategy_enum):
        if slot_assignment_strategy_enum == SlotAssignmentStrategyEum.RANDOM:
            return RandomSlotFindingStrategy()
        return None
