import pygame

class Mole(pygame.sprite.Sprite):
    def __init__(self, (x, y)):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(pygame.image.load('res/mole.png'),
                                            (50, 50))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, d):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)
