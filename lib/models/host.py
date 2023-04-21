from lib.base_classes.protein_cell import ProteinCell
from lib.strategies.interaction import InteractionStrategy
from lib.models.viruses.influenza import Influenza
import arcade

class Host(ProteinCell):
    
    def __init__(self, x, y, color, multiplier = 1, size = None, protein = None):
        super().__init__(x, y, color, multiplier, size, protein)
        self.strategy = self.set_interaction_strategy()
        self.viruses = []
        self.original_color = self.color
        self.sick = False
        self.length_of_sickness = 100 # allows our host's "immune system" to get rid of all viruses
        self.sick_timer = 0
    
    def set_interaction_strategy(self, strategy= InteractionStrategy):
        return strategy()
    
    def interact_with_virus(self, virus: Influenza):
        self.sick = self._determine_if_infected(virus)
        if self.sick:
            self._infect(virus)
            
    
    def _infect(self, virus: Influenza):
        self.sick_timer = self.length_of_sickness
        self.sick = True
        self.color = (0,0,0)
        self.viruses.append(virus)
    
    def _cured(self):
        self.viruses = []
        self.sick = False
        self.color = self.original_color
        self.sick_timer = 0
    
    def spawn(self):
        super().spawn()
        if self.sick:
            arcade.draw_circle_outline(self.x, self.y, self.size+2, arcade.color.RED)
            self._antigenic_drift()
            # self.sick_timer -= 1
            # if self.sick_timer <= 0:
            #     self._cured()

    def _antigenic_drift(self):
        # for virus in self.viruses:
        #     new_virus += virus.replicate()
        
        self.viruses = self.viruses[0].replicate()

    def _determine_if_infected(self, virus: Influenza):
        return self.strategy.check_compatibility(self, virus)