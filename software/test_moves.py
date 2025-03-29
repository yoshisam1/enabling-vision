from character import Character, CharacterClass
import random
from collections import defaultdict
import time

class GameTestSuite:
    def __init__(self):
        self.moves_dict = self._get_all_moves()
        self.stats = {
            'wins': defaultdict(int),
            'class_wins': defaultdict(int),
            'avg_game_length': [],
            'move_usage': defaultdict(int),
            'damage_dealt': defaultdict(list),
            'healing_done': defaultdict(list)
        }

    def _print_character_stats(self, character):
        """Print character's current stats"""
        print(f"\n{character.name}'s Stats:")
        print(f"Health: {character.health}/{character.max_health}")
        print(f"Attack: {character.attack}")
        print(f"Defense: {character.defense}")

    def _test_move(self, attacker, defender, move_index):
        """Test a specific move and print the results"""
        print("\n" + "="*50)
        print(f"Testing {attacker.name}'s {attacker.moves[move_index].name}")
        print("-"*50)
        
        # Reset move uses before testing
        for move in attacker.moves:
            move.current_uses = move.max_uses
        
        # Print initial stats
        print("Initial Stats:")
        self._print_character_stats(attacker)
        self._print_character_stats(defender)
        
        # Use the move
        success, message = attacker.use_move(move_index, defender)
        
        # Print the move result
        print("\nMove Result:")
        print(message)
        
        # Print final stats
        print("\nFinal Stats:")
        self._print_character_stats(attacker)
        self._print_character_stats(defender)
        print("="*50)

    def _get_all_moves(self):
        """Get a dictionary of all moves and their character classes"""
        moves = {}
        for char_class in CharacterClass:
            char = Character("Test", char_class)
            for i, move in enumerate(char.moves):
                moves[move.name] = (char_class, i)
        return moves

    def test_specific_move(self, move_name):
        """Test a specific move by name"""
        if move_name not in self.moves_dict:
            print(f"Move '{move_name}' not found!")
            return
        
        char_class, move_index = self.moves_dict[move_name]
        
        # Create characters based on the move's class
        if char_class == CharacterClass.KNIGHT:
            attacker = Character("Test Knight", CharacterClass.KNIGHT)
            defender = Character("Target Dummy", CharacterClass.WIZARD)
        elif char_class == CharacterClass.WIZARD:
            attacker = Character("Test Wizard", CharacterClass.WIZARD)
            defender = Character("Target Dummy", CharacterClass.KNIGHT)
            if move_name == "Volcanic Surge":
                attacker.health = attacker.max_health // 3
            elif move_name == "Tidal Crash":
                attacker.health = attacker.max_health // 2
        else:  # ARCHER
            attacker = Character("Test Archer", CharacterClass.ARCHER)
            defender = Character("Target Dummy", CharacterClass.KNIGHT)
            if move_name == "Sharpened Quake":
                defender.health = defender.max_health // 3
        
        # Special setup for Inferno Counter
        if move_name == "Inferno Counter":
            attacker.take_damage(20)
            print(f"Attacker took 20 damage before using {move_name}")
        
        self._test_move(attacker, defender, move_index)

    def test_knight_moves(self):
        """Test all Knight moves"""
        print("\nTesting Knight Moves")
        print("="*50)
        
        knight = Character("Test Knight", CharacterClass.KNIGHT)
        target = Character("Target Dummy", CharacterClass.WIZARD)
        
        # Test each move
        for i in range(len(knight.moves)):
            # Reset characters for each test
            knight = Character("Test Knight", CharacterClass.KNIGHT)
            target = Character("Target Dummy", CharacterClass.WIZARD)
            self._test_move(knight, target, i)

    def test_wizard_moves(self):
        """Test all Wizard moves"""
        print("\nTesting Wizard Moves")
        print("="*50)
        
        wizard = Character("Test Wizard", CharacterClass.WIZARD)
        target = Character("Target Dummy", CharacterClass.KNIGHT)
        
        # Test each move
        for i in range(len(wizard.moves)):
            # Reset characters for each test
            wizard = Character("Test Wizard", CharacterClass.WIZARD)
            target = Character("Target Dummy", CharacterClass.KNIGHT)
            
            # Special setup for moves that need specific conditions
            if wizard.moves[i].name == "Volcanic Surge":
                # Test with low HP
                wizard.health = wizard.max_health // 3
            elif wizard.moves[i].name == "Tidal Crash":
                # Test with missing HP
                wizard.health = wizard.max_health // 2
                
            self._test_move(wizard, target, i)

    def test_archer_moves(self):
        """Test all Archer moves"""
        print("\nTesting Archer Moves")
        print("="*50)
        
        archer = Character("Test Archer", CharacterClass.ARCHER)
        target = Character("Target Dummy", CharacterClass.KNIGHT)
        
        # Test each move
        for i in range(len(archer.moves)):
            # Reset characters for each test
            archer = Character("Test Archer", CharacterClass.ARCHER)
            target = Character("Target Dummy", CharacterClass.KNIGHT)
            
            # Special setup for moves that need specific conditions
            if archer.moves[i].name == "Sharpened Quake":
                # Test with target at low HP
                target.health = target.max_health // 3
                
            self._test_move(archer, target, i)

    def test_special_scenarios(self):
        """Test special move interactions"""
        print("\nTesting Special Scenarios")
        print("="*50)
        
        # Test Inferno Counter after taking damage
        knight = Character("Test Knight", CharacterClass.KNIGHT)
        attacker = Character("Attacker", CharacterClass.ARCHER)
        target = Character("Target", CharacterClass.WIZARD)
        
        print("\nTesting Inferno Counter after taking damage:")
        # First, have the knight take some damage
        knight.take_damage(20)
        print(f"Knight took 20 damage, health now: {knight.health}/{knight.max_health}")
        # Then test Inferno Counter
        counter_index = next(i for i, move in enumerate(knight.moves) if move.name == "Inferno Counter")
        self._test_move(knight, target, counter_index)
        
        # Test Flame Arrow stacking
        print("\nTesting Flame Arrow attack stacking:")
        archer = Character("Test Archer", CharacterClass.ARCHER)
        target = Character("Target", CharacterClass.WIZARD)
        flame_arrow_index = next(i for i, move in enumerate(archer.moves) if move.name == "Flame Arrow")
        
        # Use Flame Arrow multiple times to test stacking
        for _ in range(4):  # Test beyond the stack limit
            self._test_move(archer, target, flame_arrow_index)

    def print_available_moves(self):
        """Print all available moves grouped by character class"""
        print("\nAvailable Moves:")
        print("="*50)
        
        for char_class in CharacterClass:
            print(f"\n{char_class.name}:")
            char = Character("Test", char_class)
            for move in char.moves:
                print(f"- {move.name}")

    def _simulate_turn(self, attacker, defender):
        """Simulate a single turn"""
        # Reset move uses if all moves are depleted
        if not any(move.current_uses > 0 for move in attacker.moves):
            for move in attacker.moves:
                move.current_uses = move.max_uses
        
        # Get available moves
        available_moves = [i for i, move in enumerate(attacker.moves) if move.current_uses > 0]
        
        if not available_moves:
            return "No moves available!"
        
        # Choose a move randomly
        move_index = random.choice(available_moves)
        success, message = attacker.use_move(move_index, defender)
        
        # Track statistics
        if success:
            move_name = attacker.moves[move_index].name
            self.stats['move_usage'][move_name] += 1
            
            # Extract damage from message using the formula result
            if "Damage calculation:" in message:
                damage_str = message.split("=")[-1].split("!")[0].strip()
                try:
                    damage = int(damage_str)
                    self.stats['damage_dealt'][attacker.character_class.name].append(damage)
                except ValueError:
                    pass
            
            # Track healing
            if "Healed" in message:
                heal_amount = int(message.split("Healed")[-1].split("!")[0].strip())
                self.stats['healing_done'][attacker.character_class.name].append(heal_amount)
        
        return message

    def simulate_game(self, player1_class, player2_class, verbose=False):
        """Simulate a complete game between two characters"""
        # Create characters
        player1 = Character("Player 1", player1_class)
        player2 = Character("Player 2", player2_class)
        
        current_player = player1
        opponent = player2
        turns = 0
        start_time = time.time()
        
        while player1.is_alive and player2.is_alive:
            if verbose:
                print(f"\n{current_player.name}'s turn ({current_player.character_class.name})")
                print(f"Health: {current_player.health}/{current_player.max_health}")
                print(f"Opponent Health: {opponent.health}/{opponent.max_health}")
            
            message = self._simulate_turn(current_player, opponent)
            
            if verbose:
                print(message)
            
            # Switch turns
            current_player, opponent = opponent, current_player
            turns += 1
            
            # Prevent infinite games
            if turns > 100:
                if verbose:
                    print("Game ended in a draw (too many turns)")
                return None, turns
        
        # Record game statistics
        game_time = time.time() - start_time
        winner = player1 if player1.is_alive else player2
        loser = player2 if player1.is_alive else player1
        
        self.stats['wins'][winner.name] += 1
        self.stats['class_wins'][winner.character_class.name] += 1
        self.stats['avg_game_length'].append(turns)
        
        if verbose:
            print(f"\nGame Over! {winner.name} ({winner.character_class.name}) wins!")
            print(f"Final Health - Winner: {winner.health}, Loser: {loser.health}")
            print(f"Turns taken: {turns}")
        
        return winner, turns

    def run_simulation(self, num_games=100, verbose=False):
        """Run multiple game simulations"""
        print(f"\nRunning {num_games} game simulations...")
        
        # Reset statistics
        self.stats = {
            'wins': defaultdict(int),
            'class_wins': defaultdict(int),
            'avg_game_length': [],
            'move_usage': defaultdict(int),
            'damage_dealt': defaultdict(list),
            'healing_done': defaultdict(list)
        }
        
        # Run simulations
        for i in range(num_games):
            if verbose:
                print(f"\nGame {i+1}/{num_games}")
            
            # Randomly select character classes
            player1_class = random.choice(list(CharacterClass))
            player2_class = random.choice(list(CharacterClass))
            
            self.simulate_game(player1_class, player2_class, verbose)
        
        self.print_statistics()

    def print_statistics(self):
        """Print detailed statistics from the simulations"""
        print("\nGame Statistics")
        print("="*50)
        
        # Win rates by class
        total_games = sum(self.stats['class_wins'].values())
        if total_games > 0:
            print("\nWin Rates by Class:")
            for class_name, wins in self.stats['class_wins'].items():
                win_rate = (wins / total_games) * 100
                print(f"{class_name}: {win_rate:.1f}% ({wins}/{total_games} games)")
        else:
            print("\nNo completed games recorded (all games ended in draws)")
        
        # Average game length
        if self.stats['avg_game_length']:
            avg_turns = sum(self.stats['avg_game_length']) / len(self.stats['avg_game_length'])
            print(f"\nAverage Game Length: {avg_turns:.1f} turns")
        else:
            print("\nNo valid game length data recorded")
        
        # Most used moves
        if self.stats['move_usage']:
            print("\nMost Used Moves:")
            sorted_moves = sorted(self.stats['move_usage'].items(), key=lambda x: x[1], reverse=True)
            for move, uses in sorted_moves[:5]:
                print(f"{move}: {uses} uses")
        else:
            print("\nNo move usage data recorded")
        
        # Average damage per class
        if any(self.stats['damage_dealt'].values()):
            print("\nAverage Damage per Class:")
            for class_name, damages in self.stats['damage_dealt'].items():
                if damages:
                    avg_damage = sum(damages) / len(damages)
                    print(f"{class_name}: {avg_damage:.1f} damage per hit")
        else:
            print("\nNo damage data recorded")
        
        # Average healing per class
        if any(self.stats['healing_done'].values()):
            print("\nAverage Healing per Class:")
            for class_name, heals in self.stats['healing_done'].items():
                if heals:
                    avg_healing = sum(heals) / len(heals)
                    print(f"{class_name}: {avg_healing:.1f} healing per use")
        else:
            print("\nNo healing data recorded")

    def run_move_tests(self):
        """Run the move testing menu"""
        while True:
            print("\nMove Testing Menu")
            print("="*50)
            print("1. Test specific move")
            print("2. Test all Knight moves")
            print("3. Test all Wizard moves")
            print("4. Test all Archer moves")
            print("5. Test special scenarios")
            print("6. Show available moves")
            print("7. Return to main menu")
            
            choice = input("\nEnter your choice (1-7): ")
            
            if choice == "1":
                self.print_available_moves()
                move_name = input("\nEnter the move name to test: ")
                self.test_specific_move(move_name)
            elif choice == "2":
                self.test_knight_moves()
            elif choice == "3":
                self.test_wizard_moves()
            elif choice == "4":
                self.test_archer_moves()
            elif choice == "5":
                self.test_special_scenarios()
            elif choice == "6":
                self.print_available_moves()
            elif choice == "7":
                break
            else:
                print("\nInvalid choice. Please try again.")

    def run(self):
        """Main menu interface"""
        test_suite = GameTestSuite()
        while True:
            print("\nGame Test Suite")
            print("="*50)
            print("1. Test Moves")
            print("2. Run Game Simulations")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1-3): ")
            
            if choice == "1":
                self.run_move_tests()
            elif choice == "2":
                num_games = int(input("Enter number of games to simulate: "))
                verbose = input("Show detailed output? (y/n): ").lower() == 'y'
                self.run_simulation(num_games, verbose)
            elif choice == "3":
                print("\nExiting test suite.")
                break
            else:
                print("\nInvalid choice. Please try again.")

def main():
    """Create and run the test suite"""
    test_suite = GameTestSuite()
    test_suite.run()

if __name__ == "__main__":
    main() 