from lib.base_classes.protein_cell import ProteinCell
import random

class Influenza(ProteinCell):

    def __init__(self, x, y, color, multiplier = 1, size = None, protein = None, override = False):
        super().__init__(x, y, color, multiplier, size, protein)
        self.replication_rate = 10
        self.mutated = self._determine_mutation(override)

    def _determine_mutation(self, override):
        self.mutated = False
        if not override:
            if random.randint(1,2) % 2 == 0:
                # Gives 50% chance of mutation
                self.mutated = True
                self.protein = self._determine_protein()
    
    def replicate(self):
        all_new_replicants = []
        for replication in range(0, self.replication_rate):
            all_new_replicants.append(
                Influenza(
                    self.x, 
                    self.y, 
                    self.color
                )
            )
        return all_new_replicants

        
