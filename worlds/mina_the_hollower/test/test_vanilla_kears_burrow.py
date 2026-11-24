from BaseClasses import CollectionState
from Fill import distribute_items_restrictive

from .bases import MinaTestBase


class TestVanillaKearsBurrowEarly(MinaTestBase):
    # Vanilla Kear locks need every Kear, and without Burrow too few locations are open to hold them,
    # so Burrow behind a Kear lock can fail the fill.
    options = {"ability_rando": ["Burrow"], "kear_rando": "vanilla"}

    def test_burrow_reachable_from_start(self):
        for seed in range(1, 6):
            with self.subTest(seed=seed):
                self.world_setup(seed)
                distribute_items_restrictive(self.multiworld)
                burrow = next(item for item in self.multiworld.get_items() if item.name == "Burrow")
                state = CollectionState(self.multiworld)
                state.sweep_for_advancements([loc for loc in self.multiworld.get_locations() if loc.address is None])
                self.assertTrue(burrow.location.can_reach(state), f"Burrow at {burrow.location}")
