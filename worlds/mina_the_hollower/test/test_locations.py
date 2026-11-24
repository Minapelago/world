from BaseClasses import ItemClassification
from collections import Counter

from .. import options, MinaTheHollowerWorld
from .bases import MinaTestBase
from ..data.locations import all_collectables
from ..data.locations.areas import loners_landing


def check_all_locations(base):
    world_location_names = {location.name for location in base.world.get_locations()}

    for location in all_collectables:
        base.assertIn(location.value, world_location_names)
    # Optional locations are never created, whichever start the player gets.
    for location in loners_landing.OptionalLocations:
        base.assertNotIn(location.value, world_location_names)

class TestCollectablesNoOssexStart(MinaTestBase):
    options = {
        "ability_rando": [],
        "goal": "radiantManorGenerator"
    }

    def test_all_locations_loaded(self):
        check_all_locations(self)


class TestCollectablesOssexStart(MinaTestBase):
    options = {
        "ability_rando": ["Swim"],
        "goal": "radiantManorGenerator",
    }

    def test_all_locations_loaded(self):
        check_all_locations(self)
