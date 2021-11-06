import pygame

class Basketball:
    def __init__(self):
        self.init_pygame()

    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()
        
    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Basketball")

    def _handle_input(self):
        pass

    def _process_game_logic(self):
        pass

    def _draw(self):
        pass

    def _get_game_objects(self):
        pass