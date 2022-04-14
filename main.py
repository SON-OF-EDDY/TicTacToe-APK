import kivy
from kivymd.app import MDApp
from kivy.lang import Builder
#from kivy.core.window import Window

#Window.size = (dp(800),1733)

class TicTacToeApp(MDApp):

    player_1_turn = True

    player_1_wins = 0
    player_2_wins = 0

    grid_board = [1,2,3,4,5,6,7,8,9]

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file('design.kv')

    def press_main_button(self,object,id_string):
        if self.player_1_turn == True:
            object.text = 'X'
        else:
            object.text = 'O'
        object.disabled = True
        self.add_to_gridboard(id_string,object.text)
        self.player_1_turn = not(self.player_1_turn)
        self.check_for_draw()
        self.check_for_victory()

    def add_to_gridboard(self,id_text,player_symbol):
        if player_symbol == 'X':
            if id_text == 'top_left':
                self.grid_board[0] = 'X'
            elif id_text == 'top_centre':
                self.grid_board[1] = 'X'
            elif id_text == 'top_right':
                self.grid_board[2] = 'X'
            elif id_text == 'middle_left':
                self.grid_board[3] = 'X'
            elif id_text == 'middle_centre':
                self.grid_board[4] = 'X'
            elif id_text == 'middle_right':
                self.grid_board[5] = 'X'
            elif id_text == 'bottom_left':
                self.grid_board[6] = 'X'
            elif id_text == 'bottom_centre':
                self.grid_board[7] = 'X'
            elif id_text == 'bottom_right':
                self.grid_board[8] = 'X'
        elif player_symbol == 'O':
            if id_text == 'top_left':
                self.grid_board[0] = 'O'
            elif id_text == 'top_centre':
                self.grid_board[1] = 'O'
            elif id_text == 'top_right':
                self.grid_board[2] = 'O'
            elif id_text == 'middle_left':
                self.grid_board[3] = 'O'
            elif id_text == 'middle_centre':
                self.grid_board[4] = 'O'
            elif id_text == 'middle_right':
                self.grid_board[5] = 'O'
            elif id_text == 'bottom_left':
                self.grid_board[6] = 'O'
            elif id_text == 'bottom_centre':
                self.grid_board[7] = 'O'
            elif id_text == 'bottom_right':
                self.grid_board[8] = 'O'

    def check_for_draw(self):
        #if every character in gridboard is not numeric then the board must be full
        draw = True
        for element in self.grid_board:
            if type(element) != str:
                draw = False
        if draw:
            self.root.ids.my_label.text = "IT'S A DRAW!"

    def make_red(self,grid_list):
        #[0,1,2]
        #md_bg_color_disabled: (1, 1, 1, 1)
        for element in grid_list:
            if element == 0:
                self.root.ids.top_left.md_bg_color_disabled = (1,0,0,1)
            elif element == 1:
                self.root.ids.top_centre.md_bg_color_disabled = (1,0,0,1)
            elif element == 2:
                self.root.ids.top_right.md_bg_color_disabled = (1,0,0,1)
            elif element == 3:
                self.root.ids.middle_left.md_bg_color_disabled = (1,0,0,1)
            elif element == 4:
                self.root.ids.middle_centre.md_bg_color_disabled = (1,0,0,1)
            elif element == 5:
                self.root.ids.middle_right.md_bg_color_disabled = (1,0,0,1)
            elif element == 6:
                self.root.ids.bottom_left.md_bg_color_disabled = (1,0,0,1)
            elif element == 7:
                self.root.ids.bottom_centre.md_bg_color_disabled = (1,0,0,1)
            elif element == 8:
                self.root.ids.bottom_right.md_bg_color_disabled = (1,0,0,1)

    def check_for_victory(self):
        #let's change the text color to red on a winning line...
        #eight win conditons

        #Player_1 "X"
        #horizontal win conditions:
        if self.grid_board[0] == 'X' and self.grid_board[1] == "X" \
                and self.grid_board[2] == "X":
            self.root.ids.my_label.text = "'X' WINS!"
            self.player_1_wins += 1
            self.update_score()
            self.disable_everything()
            self.make_red([0, 1, 2])
        elif self.grid_board[3] == 'X' and self.grid_board[4] == "X" \
                and self.grid_board[5] == "X":
            self.root.ids.my_label.text = "'X' WINS!"
            self.player_1_wins += 1
            self.update_score()
            self.disable_everything()
            self.make_red([3, 4, 5])
        elif self.grid_board[6] == 'X' and self.grid_board[7] == "X" \
                and self.grid_board[8] == "X":
            self.root.ids.my_label.text = "'X' WINS!"
            self.player_1_wins += 1
            self.update_score()
            self.disable_everything()
            self.make_red([6, 7, 8])

        #vertical win condtions:
        if self.grid_board[0] == 'X' and self.grid_board[3] == "X" \
                and self.grid_board[6] == "X":
            self.root.ids.my_label.text = "'X' WINS!"
            self.player_1_wins += 1
            self.update_score()
            self.disable_everything()
            self.make_red([0, 3, 6])
        elif self.grid_board[1] == 'X' and self.grid_board[4] == "X" \
                and self.grid_board[7] == "X":
            self.root.ids.my_label.text = "'X' WINS!"
            self.player_1_wins += 1
            self.update_score()
            self.disable_everything()
            self.make_red([1, 4, 7])
        elif self.grid_board[2] == 'X' and self.grid_board[5] == "X" \
                and self.grid_board[8] == "X":
            self.root.ids.my_label.text = "'X' WINS!"
            self.player_1_wins += 1
            self.update_score()
            self.disable_everything()
            self.make_red([2, 5, 8])

        #diagonal win conditons:
        if self.grid_board[0] == 'X' and self.grid_board[4] == "X" \
                and self.grid_board[8] == "X":
            self.root.ids.my_label.text = "'X' WINS!"
            self.player_1_wins += 1
            self.update_score()
            self.disable_everything()
            self.make_red([0, 4, 8])
        elif self.grid_board[2] == 'X' and self.grid_board[4] == "X" \
                and self.grid_board[6] == "X":
            self.root.ids.my_label.text = "'X' WINS!"
            self.player_1_wins += 1
            self.update_score()
            self.disable_everything()
            self.make_red([2, 4, 6])

        #######################################################################
        #Player_2 "O" win conditions:
        # horizontal win conditions:
        if self.grid_board[0] == 'O' and self.grid_board[1] == "O" \
                and self.grid_board[2] == "O":
            self.root.ids.my_label.text = "'O' WINS!"
            self.player_2_wins += 1
            self.update_score()
            self.disable_everything()
            self.make_red([0, 1, 2])
        elif self.grid_board[3] == 'O' and self.grid_board[4] == "O" \
                and self.grid_board[5] == "O":
            self.root.ids.my_label.text = "'O' WINS!"
            self.player_2_wins += 1
            self.update_score()
            self.disable_everything()
            self.make_red([3, 4, 5])
        elif self.grid_board[6] == 'O' and self.grid_board[7] == "O" \
                and self.grid_board[8] == "O":
            self.root.ids.my_label.text = "'O' WINS!"
            self.player_2_wins += 1
            self.update_score()
            self.disable_everything()
            self.make_red([6, 7, 8])

        # vertical win condtions:
        if self.grid_board[0] == 'O' and self.grid_board[3] == "O" \
                and self.grid_board[6] == "O":
            self.root.ids.my_label.text = "'O' WINS!"
            self.player_2_wins += 1
            self.update_score()
            self.disable_everything()
            self.make_red([0, 3, 6])
        elif self.grid_board[1] == 'O' and self.grid_board[4] == "O" \
                and self.grid_board[7] == "O":
            self.root.ids.my_label.text = "'O' WINS!"
            self.player_2_wins += 1
            self.update_score()
            self.disable_everything()
            self.make_red([1, 4, 7])
        elif self.grid_board[2] == 'O' and self.grid_board[5] == "O" \
                and self.grid_board[8] == "O":
            self.root.ids.my_label.text = "'O' WINS!"
            self.player_2_wins += 1
            self.update_score()
            self.disable_everything()
            self.make_red([2, 5, 8])

        # diagonal win conditons:
        if self.grid_board[0] == 'O' and self.grid_board[4] == "O" \
                and self.grid_board[8] == "O":
            self.root.ids.my_label.text = "'O' WINS!"
            self.player_2_wins += 1
            self.update_score()
            self.disable_everything()
            self.make_red([0, 4, 8])
        elif self.grid_board[2] == 'O' and self.grid_board[4] == "O" \
                and self.grid_board[6] == "O":
            self.root.ids.my_label.text = "'O' WINS!"
            self.player_2_wins += 1
            self.update_score()
            self.disable_everything()
            self.make_red([2, 4, 6])

    def update_score(self):
        self.root.ids.score.text = f"'X' WINS: \
{self.player_1_wins}  ||  'O' WINS: {self.player_2_wins}"

    def disable_everything(self):

        self.root.ids.top_left.disabled = True
        self.root.ids.top_centre.disabled = True
        self.root.ids.top_right.disabled = True

        self.root.ids.middle_left.disabled = True
        self.root.ids.middle_centre.disabled = True
        self.root.ids.middle_right.disabled = True

        self.root.ids.bottom_left.disabled = True
        self.root.ids.bottom_centre.disabled = True
        self.root.ids.bottom_right.disabled = True

    def reset_everything(self):

        self.root.ids.top_left.disabled = False
        self.root.ids.top_centre.disabled = False
        self.root.ids.top_right.disabled = False

        self.root.ids.middle_left.disabled = False
        self.root.ids.middle_centre.disabled = False
        self.root.ids.middle_right.disabled = False

        self.root.ids.bottom_left.disabled = False
        self.root.ids.bottom_centre.disabled = False
        self.root.ids.bottom_right.disabled = False

        ###################################################
        self.root.ids.top_left.text = ""
        self.root.ids.top_centre.text = ""
        self.root.ids.top_right.text = ""

        self.root.ids.middle_left.text = ""
        self.root.ids.middle_centre.text = ""
        self.root.ids.middle_right.text = ""

        self.root.ids.bottom_left.text = ""
        self.root.ids.bottom_centre.text = ""
        self.root.ids.bottom_right.text = ""

        #####################################################

        self.root.ids.top_left.md_bg_color_disabled = (1, 1, 1, 1)
        self.root.ids.top_centre.md_bg_color_disabled = (1, 1, 1, 1)
        self.root.ids.top_right.md_bg_color_disabled = (1, 1, 1, 1)

        self.root.ids.middle_left.md_bg_color_disabled = (1, 1, 1, 1)
        self.root.ids.middle_centre.md_bg_color_disabled = (1, 1, 1, 1)
        self.root.ids.middle_right.md_bg_color_disabled = (1, 1, 1, 1)

        self.root.ids.bottom_left.md_bg_color_disabled = (1, 1, 1, 1)
        self.root.ids.bottom_centre.md_bg_color_disabled = (1, 1, 1, 1)
        self.root.ids.bottom_right.md_bg_color_disabled = (1, 1, 1, 1)

        #####################################################

        self.root.ids.my_label.text = "'X' GOES FIRST!"
        self.grid_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.player_1_turn = True

TicTacToeApp().run()
