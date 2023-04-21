import pytest
from lib.models.viruses.influenza import Influenza
from lib.models.host import Host
import random

def test_creation_of_virus():
    virus = Influenza(
                10,
                10,
                color = (255,255,255),
                multiplier = 1, 
                size = 10
            )
    assert isinstance(virus, Influenza)

def test_replication_of_virus():
    virus = Influenza(
                10,
                10,
                color = (255,255,255),
                multiplier = 1, 
                size = 10
            )
    assert isinstance(virus, Influenza)
    new_viruses = virus.replicate()
    assert len(new_viruses) == virus.replication_rate
