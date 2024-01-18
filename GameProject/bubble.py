import pygame
import random
import image
from settings import *
from balloon import Balloon

class Bubble(Balloon):
    def __init__(self):
        #size
        random_size_value = random.uniform(BUBBLE_SIZE_RANDOMIZE[0], BUBBLE_SIZE_RANDOMIZE[1])
        size = (int(BUBBLE_SIZES[0] * random_size_value), int(BUBBLE_SIZES[1] * random_size_value))
        # moving
        moving_direction, start_pos = self.define_pop_pos(size)
        # sprite
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0]//1.4, size[1]//1.4)
        self.images = [image.load(f"material/bubble/bubble.png", size=size, flip=moving_direction=="right") for nb in range(1, 7)] # load the images
        self.current_frame = 0
        self.animation_timer = 0
        

    def pop(self, balloon): # remove the balloon from the list
        balloon.remove(self)
        return -BUBBLE_PENALITY
