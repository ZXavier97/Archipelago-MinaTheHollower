from ... import LocationData
from ...items import SingleKears
from ...rules.ability_rules import CanBurrow, CanBounce, CanClimb, CanCarry, HasFishingRod, CanSwim
from ...rules.state_rules import HasKear, HasRepairedOneGenerator, HasLadder
from ...rules.movement_rules import CanJumpTiles

boss_locations: dict[str, LocationData] = {
}
collectable_locations: dict[str, LocationData] = {
    "LL Blighted Docks Tall Room Chest": LocationData(29, "Loner's Landing Blighted Docks Fences Bottom"),
    # needs burrow,
    "LL Blighted Docks Side Cave Chest": LocationData(28, "Loner's Landing Blighted Docks Side Cave"),
    "LL Blighted Docks Bridge Chest": LocationData(31, "Loner's Landing Blighted Docks Bridge", CanBounce() & CanClimb()),
    "LL Blighted Docks Residence Chest": LocationData(26, "Loner's Landing Blighted Docks Residence", CanBurrow()),
    "LL Blighted Docks Burrow Residence Bubble": LocationData(23, "Loner's Landing Blighted Docks Burrow", CanJumpTiles(distance=2)),
    # needs burrow,
    "LL Boardwalk Fire Bounce Chest": LocationData(27, "Loner's Landing Boardwalk Fire Bounce", CanBounce()),
    "LL Boardwalk Sandfalls Ledge Chest": LocationData(324, "Loner's Landing Boardwalk Sandfalls Ledge"),
    # needs bounce,
    "LL Fish Trigger Antennae": LocationData(32, "Loner's Landing Boat Side", HasFishingRod() & CanBurrow()),
    "LL Belowdecks Unchosen Weapon #1": LocationData(17, "Loner's Landing Belowdecks", HasKear(kear=SingleKears.LONERS_LANDING_BELOWDECKS_LEFT_WEAPON_KEAR.value)),
    "LL Belowdecks Unchosen Weapon #2": LocationData(18, "Loner's Landing Belowdecks", HasKear(kear=SingleKears.LONERS_LANDING_BELOWDECKS_RIGHT_WEAPON_KEAR.value)),
    "LL Belowdecks Chest": LocationData(30, "Loner's Landing Belowdecks", CanJumpTiles(distance=2)),
    "LL Captain's Gift" : LocationData(24, "Loner's Landing Shipwreck"),
}


