from enum import Enum
import arcade


class AttackType(Enum):
    ROCK = 0,
    PAPER = 1,
    SCISSORS = 2

player_attack_type = {
    0: "roche",
    1: "papier",
    2: "ciseauX"
}


class AttackAnimation(arcade.Sprite):
    ATTACK_SCALE = 0.5
    ANIMATION_SPEED = 5.0