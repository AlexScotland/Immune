import pytest
from lib.models.host import Host
from lib.models.viruses.influenza import Influenza
import random

def test_host_creation():
    current_host = Host(
                10,
                10,
                color = (255,255,255),
                multiplier = 1, 
                size = 10
            )
    assert isinstance(current_host, Host)
    assert current_host.sick == False

def test_infecting_host():

    current_host = Host(
                10,
                10,
                color = (255,255,255),
                multiplier = 1, 
                size = 10
            )
    assert isinstance(current_host, Host)
    assert current_host.sick == False
    compatible_virus = Influenza(
                10,
                10,
                color = (255,255,255),
                multiplier = 1, 
                size = 10,
                protein = current_host.protein,
                override=True
            )
    current_host.interact_with_virus(compatible_virus)
    assert current_host.sick
    assert compatible_virus in current_host.viruses


def test_infecting_host_replication():

    old_random = random.randint

    def mock_random(*args):
        return 0
    
    random.randint = mock_random

    current_host = Host(
                10,
                10,
                color = (255,255,255),
                multiplier = 1, 
                size = 10
            )
    assert isinstance(current_host, Host)
    assert current_host.sick == False
    compatible_virus = Influenza(
                10,
                10,
                color = (255,255,255),
                multiplier = 1, 
                size = 10,
                protein = current_host.protein
            )
    # reset random
    random.randint = old_random
    current_host.interact_with_virus(compatible_virus)
    assert current_host.sick
    assert compatible_virus in current_host.viruses
    assert len(current_host.viruses) == 1
    current_host._antigenic_drift()
    assert len(current_host.viruses) == 11
