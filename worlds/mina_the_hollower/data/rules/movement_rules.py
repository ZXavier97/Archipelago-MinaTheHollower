import dataclasses
from itertools import combinations
from typing import override

from BaseClasses import CollectionState
from NetUtils import JSONMessagePart
from rule_builder.rules import Rule
from ...constants import MINA_THE_HOLLOWER
from ...world_base import MinaTheHollowerBase
from ...data import ItemTypeEnum
from ..items import Trinkets, Sidearms, PlayerUpgrades, Weapons, \
    Abilities, all_movement_items



def base_movement_calc(movement_loadout, has_walls: bool):
    distance = 1
    if Abilities.BURROW in movement_loadout:
        distance+=1
    if Trinkets.BRISK_BREW in movement_loadout:
        distance += 1
    if Trinkets.WALLOWERS_GAUNTLETS in movement_loadout and has_walls:
        distance += 5
    if Trinkets.BELLOWS_BUSTLE in movement_loadout:
        distance += 2
    if Trinkets.KERI_THE_WISP in movement_loadout or (Sidearms.DEFLECTOR_PARASOL in movement_loadout and not Trinkets.BELLOWS_BUSTLE in movement_loadout):
        distance += 2
    if Sidearms.MIST_JAR in movement_loadout:
        distance += 1
    if Trinkets.PIT_PRESERVER in movement_loadout:
        distance += 1
    if Sidearms.DRIVER_DRILL in movement_loadout:
        distance+=4
    return distance

def shield_calc(movement_loadout, has_walls: bool):
    distance = 4
    if Trinkets.BRISK_BREW in movement_loadout:
        distance += 1
    if Trinkets.WALLOWERS_GAUNTLETS in movement_loadout and has_walls:
        distance += 5
    if Trinkets.BELLOWS_BUSTLE in movement_loadout:
        distance += 2
    if Trinkets.KERI_THE_WISP in movement_loadout or (Sidearms.DEFLECTOR_PARASOL in movement_loadout and not Trinkets.BELLOWS_BUSTLE in movement_loadout):
        distance += 2
    if Sidearms.MIST_JAR in movement_loadout:
        distance += 1
    if Trinkets.PIT_PRESERVER in movement_loadout:
        distance += 1
    if Sidearms.DRIVER_DRILL in movement_loadout:
        distance += 4
    return distance

def bridge_weaver_calc(movement_loadout, has_walls: bool):
    distance = 3
    if Abilities.BURROW in movement_loadout:
        distance += 1
    if Trinkets.WALLOWERS_GAUNTLETS in movement_loadout and has_walls:
        distance += 5
    if Trinkets.BELLOWS_BUSTLE in movement_loadout:
        distance += 2
    if Trinkets.KERI_THE_WISP in movement_loadout or (Sidearms.DEFLECTOR_PARASOL in movement_loadout and not Trinkets.BELLOWS_BUSTLE in movement_loadout):
        distance += 2
    if Sidearms.MIST_JAR in movement_loadout:
        distance += 1
    if Trinkets.PIT_PRESERVER in movement_loadout:
        distance += 1
    if Sidearms.DRIVER_DRILL in movement_loadout:
        distance += 4
    if Trinkets.BRISK_BREW in movement_loadout and distance > 3:
        distance += 1
    return distance

def iron_steed_calc(movement_loadout, has_walls: bool):
    distance = 5
    if Trinkets.KERI_THE_WISP in movement_loadout:
        return 11
    if Trinkets.BELLOWS_BUSTLE in movement_loadout:
        distance += 1
    if Trinkets.PIT_PRESERVER in movement_loadout:
        distance += 1
    return distance


def spring_heel_calc(movement_loadout, has_walls: bool):
    distance = 3

    if Trinkets.WALLOWERS_GAUNTLETS in movement_loadout and has_walls:
        distance+=5

    if Trinkets.BRISK_BREW in movement_loadout:
        distance += 1

    if Trinkets.KERI_THE_WISP in movement_loadout or (Sidearms.DEFLECTOR_PARASOL in movement_loadout and not Trinkets.BELLOWS_BUSTLE in movement_loadout):
        distance += 2

    if Sidearms.DRIVER_DRILL in movement_loadout:
        distance+=4
        if Trinkets.KERI_THE_WISP in movement_loadout:
            distance+=1
    if Sidearms.MIST_JAR in movement_loadout:
        distance += 1
    if Trinkets.PIT_PRESERVER in movement_loadout:
        distance += 1
    if Trinkets.BELLOWS_BUSTLE in movement_loadout:
        distance += 2
    return distance


exclusive_movements = [
    (Trinkets.SPRING_HEELS, spring_heel_calc),
    (Sidearms.IRON_STEED, iron_steed_calc),
    (Trinkets.BRIDGE_WEAVER, bridge_weaver_calc),
    (Weapons.GUARDIAN_CASKET, shield_calc),
]


def is_valid_loadout(loadout):
    return not len(loadout & exclusive_movements) > 1


def valid_loadouts(state: CollectionState, player: int):
    available_trinkets: list[ItemTypeEnum] = [
        t for t in Trinkets
        if state.has(t.value, player)
    ]
    if state.has(Weapons.GUARDIAN_CASKET.value, player, 2):
        available_trinkets.append(Weapons.GUARDIAN_CASKET)

    has_joules = state.has(PlayerUpgrades.JOULE_BOX.value, player)
    available_sidearms = [
        s for s in Sidearms
        if has_joules and state.has(s.value, player)
    ]

    has_burrow = state.has(Abilities.BURROW.value, player)

    trinket_slots = state.count(PlayerUpgrades.TRINKET_BAG.value, player)


    def emit(loadout: set):
        frozen = frozenset(loadout)
        if is_valid_loadout(frozen):
            yield frozen

    for num_trinkets in range(min(trinket_slots, len(available_trinkets)), -1, -1):
        for trinkets in combinations(available_trinkets, num_trinkets):

            base_loadout = set(trinkets)

            if has_burrow:
                base_loadout.add(Abilities.BURROW)

            yield from emit(base_loadout)

            for sidearm in available_sidearms:
                yield from emit(base_loadout | {sidearm})






@dataclasses.dataclass(kw_only=True)
class CanJumpTiles(Rule[MinaTheHollowerBase], game=MINA_THE_HOLLOWER):
    distance: int
    has_wall: bool = False
    @override
    def _instantiate(self, world: MinaTheHollowerBase) -> Rule.Resolved:
        # caching_enabled only needs to be passed in when your world inherits from CachedRuleBuilderWorld
        return self.Resolved(distance=self.distance, has_wall=self.has_wall, player=world.player, caching_enabled=False)

    class Resolved(Rule.Resolved):
        distance: int
        has_wall: bool

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            for loadout in valid_loadouts(state, self.player):
                candidates = [
                    calc(loadout, self.has_wall)
                    for item, calc in exclusive_movements
                    if item in loadout
                ]
                if not candidates:
                    candidates = [base_movement_calc(loadout, self.has_wall)]
                if max(candidates) >= self.distance:
                    return True
            return False

        @override
        def item_dependencies(self) -> dict[str, set[int]]:
            return  {item.value : {item.item_id} for item in all_movement_items}

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            # this method can be overridden to display custom explanations
            return [
                {"type": "color", "color": "green" if state and self(state) else "salmon", "text": str(self)},
            ]
        @override
        def __str__(self) -> str:
            return "Jump x tiles"