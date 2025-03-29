from character import Character, CharacterClass

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

def player_turn(player, opponent):
    print(f"\n{player.name}'s turn!")
    print(player)
    
    # Show available moves
    available_moves = player.get_available_moves()
    if not available_moves:
        print("No moves available!")
        return
    
    print("\nAvailable moves:")
    for i, move in enumerate(available_moves):
        print(f"{i+1}. {move.name} - {move.effect_description}")
    
    # Get move choice
    while True:
        try:
            choice = int(input("\nChoose a move (enter the number): "))
            if 1 <= choice <= len(available_moves):
                move_index = player.moves.index(available_moves[choice-1])
                success, message = player.use_move(move_index, opponent)
                print(message)
                return
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a number.")

def battle(player1, player2):
    print("\nBattle begins!")
    current_player = player1
    opponent = player2
    
    while player1.is_alive and player2.is_alive:
        player_turn(current_player, opponent)
        
        # Switch turns
        current_player, opponent = opponent, current_player
    
    # Battle ended
    winner = player1 if player1.is_alive else player2
    print(f"\nBattle ended! {winner.name} is victorious!")

def main():
    print("Welcome to the Battle Game!")
    
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
    battle(player1, player2)

if __name__ == "__main__":
    main()
