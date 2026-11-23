from BaseClasses import CollectionState

from ..data.rules.movement_rules import CanJumpTiles
from .bases import MinaTestBase

class TestJumpRules(MinaTestBase):
    options = {"ability_rando": ["swim"]}

    def can_jump(self, distance: int, *items: str) -> bool:
        # fresh state per check so the rule cache can't hide the result
        state = CollectionState(self.multiworld)
        for name in items:
            state.collect(self.world.create_item(name), prevent_sweep=True)
        return CanJumpTiles(distance=distance).resolve(self.world)(state)

    def test_swim_does_not_shrink_jump(self):
        self.assertTrue(self.can_jump(3, "Trinket Bag", "Spring Heels"))
        self.assertTrue(self.can_jump(3, "Trinket Bag", "Spring Heels", "Swim"))
    