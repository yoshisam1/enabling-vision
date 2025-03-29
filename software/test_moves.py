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
        """Get all moves for each character class"""
        moves_dict = {}
        for char_class in CharacterClass:
            moves_dict[char_class.name] = char_class.value["moves"]
        return moves_dict

    def test_specific_move(self, attacker, defender, move_name):
        """Test a specific move by name"""
        move_index = None
        for i, move in enumerate(attacker.moves):
            if move.name == move_name:
                move_index = i
                break
        
        if move_index is not None:
            self._test_move(attacker, defender, move_index)
        else:
            print(f"Move '{move_name}' not found!")

    def test_knight_moves(self, defender):
        """Test all Knight moves"""
        attacker = Character("Knight", CharacterClass.KNIGHT)
        print("\nTesting Knight Moves:")
        for i, move in enumerate(attacker.moves):
            self._test_move(attacker, defender, i)

    def test_wizard_moves(self, defender):
        """Test all Wizard moves"""
        attacker = Character("Wizard", CharacterClass.WIZARD)
        print("\nTesting Wizard Moves:")
        for i, move in enumerate(attacker.moves):
            self._test_move(attacker, defender, i)

    def test_archer_moves(self, defender):
        """Test all Archer moves"""
        attacker = Character("Archer", CharacterClass.ARCHER)
        print("\nTesting Archer Moves:")
        for i, move in enumerate(attacker.moves):
            self._test_move(attacker, defender, i)

    def test_special_scenarios(self):
        """Test special scenarios like super effectiveness"""
        print("\nTesting Special Scenarios:")
        
        # Test elemental effectiveness
        print("\nTesting Elemental Effectiveness:")
        knight = Character("Knight", CharacterClass.KNIGHT)
        wizard = Character("Wizard", CharacterClass.WIZARD)
        
        # Use a Fire move first
        knight.use_move(0, wizard)  # Use a Fire move
        # Then use a Water move (should be super effective)
        wizard.use_move(1, knight)  # Use a Water move
        
        # Test low HP scenarios
        print("\nTesting Low HP Scenarios:")
        knight.health = knight.max_health // 4
        wizard.use_move(4, knight)  # Use Volcanic Surge (should roll twice)
        
        # Test high defense scenarios
        print("\nTesting High Defense Scenarios:")
        knight.defense = 15
        wizard.use_move(2, knight)  # Use Rock Breaker (should get bonus power)

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
        
        return message

    def simulate_game(self, attacker, defender, verbose=False):
        """Simulate a single game between two characters"""
        turn = 1
        max_turns = 50  # Prevent infinite games
        
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
                return f"{attacker.name} wins!"
            
            # Defender's turn
            message = self._simulate_turn(defender, attacker)
            if verbose:
                print(message)
            if not attacker.is_alive:
                self.stats['wins'][defender.name] += 1
                self.stats['class_wins'][defender.character_class.name] += 1
                self.stats['avg_game_length'].append(turn)
                return f"{defender.name} wins!"
            
            turn += 1
        
        return "Draw!"

    def run_simulation(self, num_games=100, verbose=False):
        """Run multiple game simulations"""
        print(f"\nRunning {num_games} game simulations...")
        
        for i in range(num_games):
            # Randomly select character classes
            attacker_class = random.choice(list(CharacterClass))
            defender_class = random.choice(list(CharacterClass))
            
            attacker = Character(f"Player 1 ({attacker_class.name})", attacker_class)
            defender = Character(f"Player 2 ({defender_class.name})", defender_class)
            
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

def main():
    tester = GameTestSuite()
    
    while True:
        print("\nGame Test Menu:")
        print("1. Test specific move")
        print("2. Test all Knight moves")
        print("3. Test all Wizard moves")
        print("4. Test all Archer moves")
        print("5. Test special scenarios")
        print("6. Run game simulations")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == "1":
            # Create test characters
            attacker = Character("Attacker", CharacterClass.KNIGHT)
            defender = Character("Defender", CharacterClass.WIZARD)
            
            # Show available moves
            print("\nAvailable moves:")
            for i, move in enumerate(attacker.moves):
                print(f"{i+1}. {move.name}")
            
            move_name = input("\nEnter move name to test: ")
            tester.test_specific_move(attacker, defender, move_name)
            
        elif choice == "2":
            defender = Character("Defender", CharacterClass.WIZARD)
            tester.test_knight_moves(defender)
            
        elif choice == "3":
            defender = Character("Defender", CharacterClass.KNIGHT)
            tester.test_wizard_moves(defender)
            
        elif choice == "4":
            defender = Character("Defender", CharacterClass.WIZARD)
            tester.test_archer_moves(defender)
            
        elif choice == "5":
            tester.test_special_scenarios()
            
        elif choice == "6":
            num_games = int(input("Enter number of games to simulate: "))
            verbose = input("Show detailed output? (y/n): ").lower() == 'y'
            tester.run_simulation(num_games, verbose)
            
        elif choice == "7":
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 