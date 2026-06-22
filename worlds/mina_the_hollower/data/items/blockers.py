from BaseClasses import ItemClassification
from .. import ItemTypeEnum
from ...constants import ITEMS_OFFSET_BLOCKERS

class AstralPlatforms(ItemTypeEnum):
    GREEN_ASTRAL_PLATFORMS = ("Green Astral Platforms",ITEMS_OFFSET_BLOCKERS, ItemClassification.progression)
    RED_ASTRAL_PLATFORMS = ("Red Astral Platforms",ITEMS_OFFSET_BLOCKERS+1, ItemClassification.progression)
    BLUE_ASTRAL_PLATFORMS = ("Blue Astral Platforms",ITEMS_OFFSET_BLOCKERS+2, ItemClassification.progression)
    YELLOW_ASTRAL_PLATFORMS = ("Yellow Astral Platforms",ITEMS_OFFSET_BLOCKERS+3, ItemClassification.progression)
    PURPLE_ASTRAL_PLATFORMS = ("Purple Astral Platforms",ITEMS_OFFSET_BLOCKERS+4, ItemClassification.progression)