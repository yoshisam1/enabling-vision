from character import Character, CharacterClass
from narrator import Narrator

def select_character_class():
    print("\nChoose your character class:")
    print("1. Knight - Moderate health, high defense, low attack")
    print("2. Wizard - High health, low defense, moderate attack")
    print("3. Archer - Low health, moderate defense, high attack")
    
    while True:
        choice = input("\nEnter your choice (1-3): ")
        if choice == "1":
            return CharacterClass.KNIGHT
        elif choice == "2":
            return CharacterClass.WIZARD
        elif choice == "3":
            return CharacterClass.ARCHER
        else:
            print("Invalid choice. Please try again.")

def player_turn(player, opponent, narrator):
    print(narrator.announce_turn(player.name))
    print(player)
    
    # Show available moves
    available_moves = player.get_available_moves()
    if not available_moves:
        print(narrator.announce_no_moves())
        return
    
    print(narrator.show_available_moves(available_moves))
    
    # Get move choice
    while True:
        try:
            choice = int(input(narrator.request_move_choice()))
            if 1 <= choice <= len(available_moves):
                move_index = player.moves.index(available_moves[choice-1])
                success, message = player.use_move(move_index, opponent)
                print(message)
                return
            else:
                print(narrator.invalid_choice())
        except ValueError:
            print(narrator.invalid_number())

def battle(player1, player2, narrator):
    print("\nBattle begins!")
    current_player = player1
    opponent = player2
    
    while player1.is_alive and player2.is_alive:
        player_turn(current_player, opponent, narrator)
        
        # Switch turns
        current_player, opponent = opponent, current_player
    
    # Battle ended
    winner = player1 if player1.is_alive else player2
    print(f"\nBattle ended! {winner.name} is victorious!")

def main():
    narrator = Narrator()
    
    # Player 1 setup
    print("\nPlayer 1 setup:")
    name1 = input("Enter your name: ")
    class1 = select_character_class()
    player1 = Character(name1, class1)
    
    # Player 2 setup
    print("\nPlayer 2 setup:")
    name2 = input("Enter your name: ")
    class2 = select_character_class()
    player2 = Character(name2, class2)
    
    # Start battle
    battle(player1, player2, narrator)

if __name__ == "__main__":
    main()
