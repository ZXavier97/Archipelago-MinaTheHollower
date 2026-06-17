from BaseClasses import LocationProgressType
from rule_builder.rules import Has, CanReachLocation
from ... import RegionConnection, Transition, LocationData
from ...rules.ability_rules import CanBurrow, CanJumpOneTile, CanBounce, CanJumpTiles, CanClimb, CanCarry, CanSwim



collectable_locations: dict[str, LocationData] = {
    "BB Sandwater Junction Goremaw Fang": LocationData(88, "Sandfalls Sandwater Junction"),
    # needs burrow, carry, climb, fishing rod, 5 tiles of air movement,
    "BB Bone Rush Trail Furgus Tunnel Chest": LocationData(354, "Bone Beach Bone Rush Mine"),
    "BB Gold Grasp Bonestone": LocationData(71, "Bone Beach Bone Rush Drop"),
    "BB Large Conveyor Bonestone": LocationData(70, "Bone Beach Bone Rush Conveyor Top", CanBounce()),  # needs canbounce(),
    "BB Split Room Chest": LocationData(78, "Bone Beach Worms Back Split"),  # needs 2 tiles of air movement,
    "BB Aquatic Conveyor Chest": LocationData(73, "Bone Beach Aquatic Conveyor"),  # needs burrow,
    "BB Brac's Tent Polyp Lamp": LocationData(80, "Bone Beach Brac's Tent"),
    "BB Brac's Tent Kear": LocationData(81, "Bone Beach Brac's Tent"),
    "BB Secret Shoals Joule Syringe": LocationData(74, "Bone Beach Secret Shoals"),  # needs canswim(),
    "BB Calcified Caverns Kear": LocationData(79, "Bone Beach Calcified Caves"),
    "BB Calcified Cage Bonestone": LocationData(76, "Bone Beach Calcified Cage"),
    "BB Submerged Handles Chest": LocationData(77, "Bone Beach Submerged Handles"),  # needs swim,
    "BB Pulsing Tract Bonestone": LocationData(86, "Bone Beach Pulsing Tract Moving Top"),  # needs burrow, float,
    "BB Worm's Back Battery Buster": LocationData(75, "Bone Beach Worms Back Chest"),  # needs canbounce(),
    "BB Worm's Spine Bonestone": LocationData(72, "Bone Beach Worms Back Right"),  # needs burrow,
    "BB Stomach Mine Kear": LocationData(84, "Bone Beach Stomach Mine Lower"),  # needs burrow, float,
    "BB Moving Stairs Bonestone": LocationData(85, "Bone Beach Gut Depths Hidden"),  # needs burrow, float,
    "BB Gut Passage Chest": LocationData(87, "Bone Beach Gut Depths Dark"),  # needs burrow,
    "BB Brain Alcove Health Rose": LocationData(83, "Bone Beach Brain Alcove"),  # needs burrow,

}


boss_locations: dict[str, LocationData] = {
    "BB Brain Alcove Mined Mind": LocationData(None, "Bone Beach Brain Alcove"),  # needs burrow,
}