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
   """
   La classe principale de l'application

   NOTE: Vous pouvez effacer les méthodes que vous n'avez pas besoin.
   Si vous en avez besoin, remplacer le mot clé "pass" par votre propre code.
   """

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
       self.player_attack_chosen = False
       self.player_won_round = None
       self.draw_round = None
       self.game_state = None

   def setup(self):

       #self.player_list = arcade.SpriteList()
       #self.computer_list = arcade.SpriteList()

       self.player = arcade.Sprite("assets/faceBeard.png", PLAYERS_SCALE)
       self.player.center_x = 100
       self.player.center_y = 300
       self.computer = arcade.Sprite("assets/compy.png")
       self.computer.center_x = 300
       self.computer.center_y = 300



   def validate_victory(self):
       """
       Utilisé pour déterminer qui obtient la victoire (ou s'il y a égalité)
       Rappel: après avoir validé la victoire, il faut changer l'état de jeu
       """


   def draw_possible_attack(self):
       """
       Méthode utilisée pour dessiner toutes les possibilités d'attaque du joueur
       (si aucune attaque n'a été sélectionnée, il faut dessiner les trois possibilités)
       (si une attaque a été sélectionnée, il faut dessiner cette attaque)
       """
       pass

   def draw_computer_attack(self):
       """
       Méthode utilisée pour dessiner les possibilités d'attaque de l'ordinateur
       """
       pass


   def draw_scores(self):
       """
       Montrer les scores du joueur et de l'ordinateur
       """
       pass

   def draw_instructions(self):
       """
       Dépendemment de l'état de jeu, afficher les instructions d'utilisation au joueur (appuyer sur espace, ou sur une image)
       """
       pass

   def on_draw(self):

       arcade.start_render()

       # Display title
       arcade.draw_text(SCREEN_TITLE,
                        0,
                        SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 2,
                        arcade.color.BLACK_BEAN,
                        60,
                        width=SCREEN_WIDTH,
                        align="center")

       self.player.draw()
       self.computer.draw()
       #self.draw_instructions()
       #self.draw_possible_attack()
       #self.draw_scores()
       #self.rock.draw()
       #self.paper.draw()
       #self.scissors.draw()
       #afficher l'attaque de l'ordinateur selon l'état de jeu
       #afficher le résultat de la partie si l'ordinateur a joué (ROUND_DONE)
       pass

   def on_update(self, delta_time):

       self.rock.update()
       self.paper.update()
       self.scissors.update()
       #vérifier si le jeu est actif (ROUND_ACTIVE) et continuer l'animation des attaques
       #si le joueur a choisi une attaque, générer une attaque de l'ordinateur et valider la victoire
       #changer l'état de jeu si nécessaire (GAME_OVER)
       pass

   def on_key_press(self, key, key_modifiers):
       GameState.NOT_STARTED = True
       if key == arcade.key.SPACE:
           if GameState.NOT_STARTED == True:
               GameState.ROUND_ACTIVE = True
               GameState.NOT_STARTED = False
           elif GameState.ROUND_DONE == True:
               GameState.ROUND_ACTIVE = True
               GameState.ROUND_DONE = False
           elif GameState.GAME_OVER == True:
               GameState.GAME_OVER = False
               GameState.ROUND_ACTIVE = True
               GameState.ROUND_DONE = False
               GameState.NOT_STARTED = False



   def reset_round(self):
       """
       Réinitialiser les variables qui ont été modifiées
       """
       #self.computer_attack_type = -1
       #self.player_attack_chosen = False
       #self.player_attack_type = {AttackType.ROCK: False, AttackType.PAPER: False, AttackType.SCISSORS: False}
       #self.player_won_round = False
       #self.draw_round = False

       pass

   def on_mouse_press(self, x, y, button, key_modifiers):


       # Rappel que si le joueur choisi une attaque, self.player_attack_chosen = True
       if self.player.collides_with_point((x, y)):
           print("L'usager a cliqué sur le sprite.")
       if self.rock.collides_with_point((x, y)):
           self.player_attack_type = AttackType.ROCK
           self.player_attack_chosen = True
       if self.paper.collides_with_point((x, y)):
           self.player_attack_type = AttackType.PAPER
           self.player_attack_chosen = True
       if self.scissors.collides_with_point((x, y)):
           self.player_attack_type = AttackType.SCISSORS
           self.player_attack_chosen = True


def main():
   game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
   game.setup()
   arcade.run()


if __name__ == "__main__":
   main()

