#Ulysse Doyon

import random
import arcade
#import arcade.gui

from attack_animation import AttackType, AttackAnimation
from game_state import GameState

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Roche, papier, ciseaux"
DEFAULT_LINE_HEIGHT = 45
PLAYERS_SCALE = 0.25


class MyGame(arcade.Window):

    PLAYER_IMAGE_X = (SCREEN_WIDTH / 2) - (SCREEN_WIDTH / 4)
    PLAYER_IMAGE_Y = SCREEN_HEIGHT / 2.5
    COMPUTER_IMAGE_X = (SCREEN_WIDTH / 2) * 1.5
    COMPUTER_IMAGE_Y = SCREEN_HEIGHT / 2.5
    ATTACK_FRAME_WIDTH = 154 / 2
    ATTACK_FRAME_HEIGHT = 154 / 2

    def __init__(self, width, height, title):
       super().__init__(width, height, title)

       arcade.set_background_color(arcade.color.BLACK_OLIVE)

       self.player = None
       self.computer = None
       self.rock = AttackAnimation(AttackType.ROCK)
       self.paper = AttackAnimation(AttackType.PAPER)
       self.scissors = AttackAnimation(AttackType.SCISSORS)
       self.player_score = 0
       self.computer_score = 0
       self.player_attack_type = {}
       self.computer_attack_type = None
       self.player_attack_chosen = 0
       self.player_won_round = None
       self.draw_round = None
       self.game_state = None
       self.game_state = GameState.NOT_STARTED
        

    def setup(self):

       #self.player_list = arcade.SpriteList()
       #self.computer_list = arcade.SpriteList()

       self.player = arcade.Sprite("assets/faceBeard.png", PLAYERS_SCALE)
       self.player.center_x = 300
       self.player.center_y = 300

       self.computer = arcade.Sprite("assets/compy.png")
       self.computer.center_x = 1000
       self.computer.center_y = 300

       #self.rock = arcade.Sprite("assets/srock.png")
       self.rock.center_x = 150
       self.rock.center_y = 170

       #self.paper = arcade.Sprite("assets/spaper.png")
       self.paper.center_x = 304
       self.paper.center_y = 170

       #self.scissors = arcade.Sprite("assets/scissors.png")
       self.scissors.center_x = 458
       self.scissors.center_y = 170

    def validate_victory(self):

       if self.game_state == GameState.ROUND_DONE:
           if self.player_attack_type == self.computer_attack_type:
               print("draw")
           elif self.player_attack_type == AttackType.ROCK and self.computer_attack_type == AttackType.SCISSORS:
               print("player win")
               self.player_score += 1
           elif self.player_attack_type == AttackType.ROCK and self.computer_attack_type == AttackType.PAPER:
               print("compi win")
               self.computer_score += 1
           elif self.player_attack_type == AttackType.PAPER and self.computer_attack_type == AttackType.ROCK:
               print("player win")
               self.player_score += 1
           elif self.player_attack_type == AttackType.PAPER and self.computer_attack_type == AttackType.SCISSORS:
               print("compi win")
               self.computer_score += 1
           elif self.player_attack_type == AttackType.SCISSORS and self.computer_attack_type == AttackType.PAPER:
               print("player win")
               self.player_score += 1
           elif self.player_attack_type ==AttackType.SCISSORS and self.computer_attack_type == AttackType.ROCK:
               print("compi win")
               self.computer_score += 1

    def draw_possible_attack(self):

       if self.player_attack_chosen == 1:
           if self.player_attack_type == AttackType.ROCK:

               self.rock.center_x = 304
               self.rock.center_y = 170
               self.rock.draw()

           if self.player_attack_type == AttackType.PAPER:

               self.paper.center_x = 304
               self.paper.center_y = 170
               self.paper.draw()

           if self.player_attack_type == AttackType.SCISSORS:

               self.scissors.center_x = 304
               self.scissors.center_y = 170
               self.scissors.draw()
       else:
           self.rock.center_x = 150
           self.rock.draw()

           arcade.draw_rectangle_outline(150, 170, 154, 154, arcade.color.DARK_RED, 3, 0)
           self.paper.center_x = 304
           self.paper.draw()
           self.scissors.center_x = 458
           self.scissors.draw()

           arcade.draw_rectangle_outline(458, 170, 154, 154, arcade.color.DARK_RED, 3, 0)

    def draw_computer_attack(self):

        if self.computer_attack_type == AttackType.ROCK:
           #print("rock")
           self.rock.draw()
           self.rock.center_x = 1000
        elif self.computer_attack_type == AttackType.PAPER:
            #print("paper")
            self.paper.draw()
            self.paper.center_x = 1000
        elif self.computer_attack_type == AttackType.SCISSORS:
            #print("scissors")
            self.scissors.draw()
            self.scissors.center_x = 1000

    def draw_scores(self):
       score = "player: "+str(self.player_score)+" computer: "+str(self.computer_score)
       arcade.draw_text(score,
                        0,
                        SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 4,
                        arcade.color.PALE_RED_VIOLET,
                        50,
                        width=SCREEN_WIDTH,
                        align="center"
                        )

    def draw_instructions(self):

        arcade.draw_text("Appuyer sur une image pour faire une attaque!",
                         0,
                         SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 4,
                         arcade.color.PALE_AQUA,
                         50,
                         width=SCREEN_WIDTH,
                         align="center")

    def on_draw(self):

       arcade.start_render()

       arcade.draw_text(SCREEN_TITLE,
                        0,
                        SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 2,
                        arcade.color.BLACK_BEAN,
                        60,
                        width=SCREEN_WIDTH,
                        align="center")

       self.player.draw()
       self.draw_computer_attack()
       arcade.draw_rectangle_outline(1000, 170, 154, 154, arcade.color.DARK_RED, 3, 0)
       if self.game_state == GameState.NOT_STARTED:
           self.draw_instructions()

       self.draw_possible_attack()

       if self.game_state != GameState.NOT_STARTED:
           self.draw_scores()
       #self.rock.draw()
       #arcade.draw_rectangle_outline(150, 170, 154, 154, arcade.color.DARK_RED, 3, 0)
       #self.paper.draw()
       arcade.draw_rectangle_outline(304, 170, 154, 154, arcade.color.DARK_RED, 3, 0)
       #self.scissors.draw()
       #arcade.draw_rectangle_outline(458, 170, 154, 154, arcade.color.DARK_RED, 3, 0)
       #afficher l'attaque de l'ordinateur selon l'état de jeu
       #afficher le résultat de la partie si l'ordinateur a joué (ROUND_DONE)
       #arcade.finish_render()

    def on_update(self, delta_time):

       self.rock.on_update(delta_time)
       self.paper.on_update(delta_time)
       self.scissors.on_update(delta_time)


       if self.player_attack_chosen == 1 and self.game_state == GameState.ROUND_ACTIVE:
           pc_attack = random.randint(0, 2)
           if pc_attack == 0:
               self.computer_attack_type = AttackType.ROCK
           elif pc_attack == 1:
               self.computer_attack_type = AttackType.PAPER
           else:
               self.computer_attack_type = AttackType.SCISSORS
           self.game_state = GameState.ROUND_DONE
           print(self.player_attack_type)
           print(self.computer_attack_type)

       if self.game_state == GameState.ROUND_DONE:
           self.validate_victory()
           self.game_state = GameState.GAME_OVER
           print(self.game_state)
       #vérifier si le jeu est actif (ROUND_ACTIVE) et continuer l'animation des attaques
       #si le joueur a choisi une attaque, générer une attaque de l'ordinateur et valider la victoire
       #changer l'état de jeu si nécessaire (GAME_OVER)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            if self.game_state == GameState.NOT_STARTED:
               self.game_state = GameState.ROUND_ACTIVE
               print(self.game_state)
            elif self.game_state == GameState.ROUND_ACTIVE:
                self.game_state = GameState.ROUND_DONE
                print(self.game_state)
            elif self.game_state == GameState.GAME_OVER:
                self.reset_round()
                self.game_state = GameState.ROUND_ACTIVE
                print("Hello")


    def reset_round(self):
        self.computer_attack_type = 0
        self.player_attack_chosen = 0
        self.player_attack_type = 0

        #self.on_draw()
        #self.draw_possible_attack()
        #self.game_state = GameState.NOT_STARTED


    def on_mouse_press(self, x, y, button, key_modifiers):


       # Rappel que si le joueur choisi une attaque, self.player_attack_chosen = True
       if self.player.collides_with_point((x, y)):
           print("L'usager a cliqué sur le sprite.")
           #if self.game_state == GameState.GAME_OVER:
               #self.reset_round()
       if self.rock.collides_with_point((x, y)):
           self.player_attack_type = AttackType.ROCK
           self.player_attack_chosen = 1
       if self.paper.collides_with_point((x, y)):
           self.player_attack_type = AttackType.PAPER
           self.player_attack_chosen = 1
       if self.scissors.collides_with_point((x, y)):
           self.player_attack_type = AttackType.SCISSORS
           self.player_attack_chosen = 1


def main():
   game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
   game.setup()
   arcade.run()


if __name__ == "__main__":
   main()
