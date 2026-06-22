from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from ... import RegionConnection, Transition, LocationData
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanBounce, CanJumpTiles, CanClimb, CanCarry

boss_locations: dict[str, LocationData] = {
}
collectable_locations: dict[str, LocationData] = {
    "LL Blighted Docks Tall Room Chest": LocationData(29, "Loner's Landing Blighted Docks Fences Bottom"),
    # needs burrow,
    "LL Blighted Docks Side Cave Chest": LocationData(28, "Loner's Landing Blighted Docks Side Cave"),
    "LL Blighted Docks Bridge Chest": LocationData(31, "Loner's Landing Blighted Docks Bridge"),  # needs bounce, climb,
    "LL Blighted Docks Residence Chest": LocationData(26, "Loner's Landing Blighted Docks Residence"),  # needs burrow,
    "LL Blighted Docks Burrow Residence Bubble": LocationData(23, "Loner's Landing Blighted Docks Burrow"),
    # needs burrow,
    "LL Boardwalk Fire Bounce Chest": LocationData(27, "Loner's Landing Boardwalk Fire Bounce"),  # needs bounce,
    "LL Boardwalk Sandfalls Ledge Chest": LocationData(324, "Loner's Landing Boardwalk Sandfalls Ledge"),
    # needs bounce,
    "LL Shipwreck Beach Trigger Antennae": LocationData(32, "Loner's Landing Boat Side"),  # needs fishing rod, burrow,
    "LL Belowdecks Unchosen Weapon #1": LocationData(17, "Loner's Landing Belowdecks"),  # needs kear x4, burrow,
    "LL Belowdecks Unchosen Weapon #2": LocationData(18, "Loner's Landing Belowdecks"),  # needs kear x4, burrow,
    "LL Belowdecks Chest": LocationData(30, "Loner's Landing Belowdecks"),  # needs canjumptiles(distance=2),
    "LL Captain's Gift" : LocationData(24, "Loner's Landing Shipwreck"),
}


