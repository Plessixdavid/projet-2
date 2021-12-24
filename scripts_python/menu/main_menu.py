from menu.game_menu import Game_Menu

def start():
    g = Game_Menu()


    while g.running:
        g.curr_menu.display_menu()
        g.score_menu.display_menu_score()
        g.game_loop()

if __name__ == "__main__":
    
    start()
                   