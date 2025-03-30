from .character import Character, CharacterClass
import random
from collections import defaultdict

class MoveTestSuite:
    def __init__(self):
        self.test_target = Character("Target Dummy")
        self.test_target.character_class = CharacterClass.WIZARD
        self.test_target.initialize_character()

    def _print_character_stats(self, character):
        """Print character's current stats"""
        print(f"\n{character.name}'s Stats:")
        print(f"Health: {character.health}/{character.max_health}")
        print(f"Attack: {character.attack}")
        print(f"Defense: {character.defense}")

    def _test_move(self, attacker, move_index):
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
        self._print_character_stats(self.test_target)
        
        # Use the move
        success, message = attacker.use_move(move_index, self.test_target)
        
        # Print the move result
        print("\nMove Result:")
        print(message)
        
        # Print final stats
        print("\nFinal Stats:")
        self._print_character_stats(attacker)
        self._print_character_stats(self.test_target)
        print("="*50)

    def view_all_moves(self):
        """Display all moves for each character class"""
        print("\nAll Available Moves")
        print("="*50)
        
        for class_name in CharacterClass:
            print(f"\n{class_name.name} Moves:")
            print("-"*30)
            character = Character(f"Test {class_name.name}")
            character.character_class = class_name
            character.initialize_character()
            
            for i, move in enumerate(character.moves):
                print(f"{i+1}. {move.name}")
                print(f"   Type: {move.move_type.name}")
                print(f"   Uses: {move.current_uses}/{move.max_uses}")
                print()

    def test_specific_move(self):
        """Test a specific move by class and move number"""
        print("\nTest Specific Move")
        print("="*50)
        
        # Display class options
        print("\nSelect Character Class:")
        for i, class_name in enumerate(CharacterClass):
            print(f"{i+1}. {class_name.name}")
        
        class_choice = input("\nEnter class number (1-3): ")
        try:
            class_index = int(class_choice) - 1
            if not 0 <= class_index < len(CharacterClass):
                print("Invalid class selection!")
                return
        except ValueError:
            print("Invalid input!")
            return
        
        # Create character of selected class
        class_list = list(CharacterClass)
        character = Character(f"Test {class_list[class_index].name}")
        character.character_class = class_list[class_index] 
        character.initialize_character()
        
        # Display available moves
        print(f"\nAvailable moves for {character.character_class.name}:")
        for i, move in enumerate(character.moves):
            print(f"{i+1}. {move.name}")
        
        move_choice = input("\nEnter move number: ")
        try:
            move_index = int(move_choice) - 1
            if not 0 <= move_index < len(character.moves):
                print("Invalid move selection!")
                return
        except ValueError:
            print("Invalid input!")
            return
        
        # Reset test target
        self.test_target = Character("Target Dummy")
        self.test_target.character_class = CharacterClass.WIZARD
        self.test_target.initialize_character()
        
        # Test the selected move
        self._test_move(character, move_index)

    def test_elemental_interactions(self):
        """Test all elemental interactions"""
        print("\nTesting Elemental Interactions")
        print("="*50)
        
        # Create characters
        knight = Character("Test Knight")
        knight.character_class = CharacterClass.KNIGHT
        knight.initialize_character()
        wizard = Character("Test Wizard")
        wizard.character_class = CharacterClass.WIZARD
        wizard.initialize_character()
        archer = Character("Test Archer")
        archer.character_class = CharacterClass.ARCHER
        archer.initialize_character()
        
        # Test Fire -> Water effectiveness (Knight -> Wizard)
        print("\nTesting Fire -> Water effectiveness:")
        print("Knight's Inferno Counter -> Wizard's Tidal Crash")
        knight.use_move(0, wizard)  # Use Fire move
        wizard.use_move(1, knight)  # Use Water move (should be super effective)
        
        # Test Earth -> Fire effectiveness (Archer -> Knight)
        print("\nTesting Earth -> Fire effectiveness:")
        print("Archer's Sharpened Quake -> Knight's Inferno Counter")
        archer.use_move(2, knight)  # Use Earth move
        knight.use_move(0, archer)  # Use Fire move (should be super effective)
        
        # Test Water -> Earth effectiveness (Wizard -> Archer)
        print("\nTesting Water -> Earth effectiveness:")
        print("Wizard's Tidal Crash -> Archer's Sharpened Quake")
        wizard.use_move(1, archer)  # Use Water move
        archer.use_move(2, wizard)  # Use Earth move (should be super effective)

    def run_all_tests(self):
        """Run all move tests"""
        self.test_elemental_interactions()
        print("\nAll move tests completed!")

class GameSimulationTest:
    def __init__(self):
        self.stats = {
            'wins': defaultdict(int),
            'class_wins': defaultdict(int),
            'avg_game_length': [],
            'move_usage': defaultdict(int),
            'damage_dealt': defaultdict(list),
            'healing_done': defaultdict(list),
            'elemental_effectiveness': defaultdict(int),
            'most_used_moves': defaultdict(int),
            'win_rates': defaultdict(float)
        }

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
            self.stats['most_used_moves'][move_name] += 1
            
            # Extract damage from message
            if "Dealt" in message:
                damage_str = message.split("Dealt")[-1].split("damage")[0].strip()
                try:
                    damage = int(damage_str)
                    self.stats['damage_dealt'][attacker.character_class.name].append(damage)
                except ValueError:
                    pass
            
            # Track healing
            if "healed" in message:
                heal_amount = int(message.split("healed")[-1].split("HP")[0].strip())
                self.stats['healing_done'][attacker.character_class.name].append(heal_amount)
            
            # Track elemental effectiveness
            if "super effective" in message:
                self.stats['elemental_effectiveness'][attacker.character_class.name] += 1
        
        return message

    def simulate_game(self, attacker, defender, verbose=False):
        """Simulate a single game between two characters"""
        turn = 1
        max_turns = 50  # Prevent infinite games
        
        if verbose:
            print(f"\nStarting game: {attacker.name} ({attacker.character_class.name}) vs {defender.name} ({defender.character_class.name})")
        
        while attacker.is_alive and defender.is_alive and turn <= max_turns:
            if verbose:
                print(f"\nTurn {turn}")
                print(f"{attacker.name}: {attacker.health}/{attacker.max_health} HP")
                print(f"{defender.name}: {defender.health}/{defender.max_health} HP")
            
            # Attacker's turn
            message = self._simulate_turn(attacker, defender)
            if verbose:
                print(message)
            if not defender.is_alive:
                self.stats['wins'][attacker.name] += 1
                self.stats['class_wins'][attacker.character_class.name] += 1
                self.stats['avg_game_length'].append(turn)
                if verbose:
                    print(f"\n{attacker.name} wins in {turn} turns!")
                return f"{attacker.name} wins!"
            
            # Defender's turn
            message = self._simulate_turn(defender, attacker)
            if verbose:
                print(message)
            if not attacker.is_alive:
                self.stats['wins'][defender.name] += 1
                self.stats['class_wins'][defender.character_class.name] += 1
                self.stats['avg_game_length'].append(turn)
                if verbose:
                    print(f"\n{defender.name} wins in {turn} turns!")
                return f"{defender.name} wins!"
            
            turn += 1
        
        if verbose:
            print("\nGame ended in a draw!")
        return "Draw!"

    def run_simulation(self, num_games=100, verbose=False):
        """Run multiple game simulations"""
        print(f"\nRunning {num_games} game simulations...")
        
        for i in range(num_games):
            # Randomly select character classes
            attacker_class = random.choice(list(CharacterClass))
            defender_class = random.choice(list(CharacterClass))
            
            attacker = Character(f"Player 1 ({attacker_class.name})")
            attacker.character_class = attacker_class
            attacker.initialize_character()
            defender = Character(f"Player 2 ({defender_class.name})")
            defender.character_class = defender_class
            defender.initialize_character()
            
            result = self.simulate_game(attacker, defender, verbose)
            if verbose:
                print(f"\nGame {i+1} Result: {result}")
        
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
                self.stats['win_rates'][class_name] = win_rate
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
                    avg_heal = sum(heals) / len(heals)
                    print(f"{class_name}: {avg_heal:.1f} HP healed per heal")
        else:
            print("\nNo healing data recorded")
        
        # Elemental effectiveness
        if any(self.stats['elemental_effectiveness'].values()):
            print("\nElemental Effectiveness:")
            for class_name, count in self.stats['elemental_effectiveness'].items():
                print(f"{class_name}: {count} super effective hits")
        else:
            print("\nNo elemental effectiveness data recorded")

def run_move_tests():
    """Run the move testing menu"""
    tester = MoveTestSuite()
    
    while True:
        print("\nMove Testing Menu:")
        print("1. View all moves")
        print("2. Test specific move")
        print("3. Test elemental interactions")
        print("4. Return to main menu")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            tester.view_all_moves()
        elif choice == "2":
            tester.test_specific_move()
        elif choice == "3":
            tester.test_elemental_interactions()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def run_game_simulation():
    """Run the game simulation menu"""
    simulator = GameSimulationTest()
    
    while True:
        print("\nGame Simulation Menu:")
        print("1. Run simulation with detailed output")
        print("2. Run simulation with summary only")
        print("3. Return to main menu")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            num_games = int(input("Enter number of games to simulate: "))
            simulator.run_simulation(num_games, verbose=True)
        elif choice == "2":
            num_games = int(input("Enter number of games to simulate: "))
            simulator.run_simulation(num_games, verbose=False)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    """Main menu for the test suite"""
    while True:
        print("\nGame Test Suite")
        print("="*50)
        print("1. Test Moves")
        print("2. Run Game Simulations")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            run_move_tests()
        elif choice == "2":
            run_game_simulation()
        elif choice == "3":
            print("\nExiting test suite.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 