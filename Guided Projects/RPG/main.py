import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):

        #Gen setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("My First RPG")
        self.clock = pygame.time.Clock()

        self.level = Level()

        #Sound
        main_sound = pygame.mixer.Sound('Guided Projects/RPG/audio/main.wav')
        main_sound.set_volume(.5)
        main_sound.play(loops=-1)

    def run(self):
        while True: 
            for event in pygame.event.get():
                #Checks if game will be closed
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()