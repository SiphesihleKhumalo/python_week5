class Superhero:
    def __init__(self, name, secret_identity, powers, weakness, origin_story):
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers  # This will be a list
        self.weakness = weakness
        self.origin_story = origin_story
        self.energy_level = 100
        
    def use_power(self, power_index):
        if power_index < len(self.powers):
            power = self.powers[power_index]
            if self.energy_level >= 10:
                print(f"{self.name} uses {power}! ⚡")
                self.energy_level -= 10
            else:
                print(f"{self.name} is too tired to use {power}! 😴")
        else:
            print("Power not found!")
    
    def rest(self):
        print(f"{self.name} takes a well-deserved rest. 🛌")
        self.energy_level = min(100, self.energy_level + 30)
    
    def describe(self):
        print(f"⚡ Hero Name: {self.name}")
        print(f"🕵️ Secret Identity: {self.secret_identity}")
        print("💪 Powers:")
        for power in self.powers:
            print(f"- {power}")
        print(f"⚠️ Weakness: {self.weakness}")
        print(f"📖 Origin: {self.origin_story}")
        print(f"🔋 Energy Level: {self.energy_level}%")

# Inheritance example - Enhanced human
class EnhancedHuman(Superhero):
    def __init__(self, name, secret_identity, powers, weakness, origin_story, enhancement_source):
        super().__init__(name, secret_identity, powers, weakness, origin_story)
        self.enhancement_source = enhancement_source
    
    # Override the use_power method
    def use_power(self, power_index):
        if power_index < len(self.powers):
            power = self.powers[power_index]
            if self.energy_level >= 8:  # Enhanced humans use slightly less energy
                print(f"{self.name} uses {power} with {self.enhancement_source} enhancement! ✨")
                self.energy_level -= 8
            else:
                print(f"{self.name} is too tired to use {power}! 💤")
        else:
            print("Power not found!")
    
    def describe(self):
        super().describe()
        print(f"🔬 Enhancement Source: {self.enhancement_source}")

# Create our female superheroes
print("=== FEMALE SUPERHERO SHOWCASE ===")
wonder_woman = Superhero(
    name="Wonder Woman",
    secret_identity="Diana Prince",
    powers=["Lasso of Truth", "Super strength", "Flight", "Combat skills"],
    weakness="Losing her bracelets",
    origin_story="Amazonian princess from Themyscira"
)

catwoman = EnhancedHuman(
    name="Catwoman",
    secret_identity="Selina Kyle",
    powers=["Peak human agility", "Master thief", "Whip mastery", "Nine lives"],
    weakness="Her moral ambiguity",
    origin_story="Gotham City burglar with a complex moral code",
    enhancement_source="Feline mutation"
)

storm = Superhero(
    name="Storm",
    secret_identity="Ororo Munroe",
    powers=["Weather manipulation", "Flight", "Lightning generation", "Precognition"],
    weakness="Claustrophobia",
    origin_story="Daughter of an African princess with mutant powers"
)

# Demonstrate the classes
wonder_woman.describe()
print("\n")
wonder_woman.use_power(0)  # Lasso of Truth
wonder_woman.use_power(2)  # Flight
print("\n")

catwoman.describe()
print("\n")
catwoman.use_power(1)  # Master thief
catwoman.use_power(3)  # Nine lives
print("\n")

storm.describe()
print("\n")
storm.use_power(0)  # Weather manipulation
storm.use_power(2)  # Lightning generation


QUESTION 2

class Heroine:
    def __init__(self, name):
        self.name = name
    
    def special_move(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def introduce(self):
        print(f"I am {self.name}, the {self.__class__.__name__}!")

class AmazonWarrior(Heroine):
    def special_move(self):
        print(f"{self.name} executes a powerful Amazonian charge! 🛡️💥")
    
    def battle_cry(self):
        print(f"{self.name} shouts: 'For Themyscira!' 🗣️")

class Thief(Heroine):
    def special_move(self):
        print(f"{self.name} silently disappears into the shadows! 🐾🌑")
    
    def steal(self):
        print(f"{self.name} pockets something valuable without anyone noticing! 💎")

class Mutant(Heroine):
    def special_move(self):
        print(f"{self.name} unleashes her mutant powers! 🌪️⚡")
    
    def transform(self):
        print(f"{self.name}'s eyes glow with cosmic energy! 👁️✨")

# Demonstrate polymorphism
print("\n=== FEMALE HERO POLYMORPHISM ===")
heroines = [
    AmazonWarrior("Wonder Woman"),
    Thief("Catwoman"),
    Mutant("Storm")
]

for heroine in heroines:
    heroine.introduce()
    heroine.special_move()
    
    # Demonstrate unique methods
    if isinstance(heroine, AmazonWarrior):
        heroine.battle_cry()
    elif isinstance(heroine, Thief):
        heroine.steal()
    elif isinstance(heroine, Mutant):
        heroine.transform()
    
    print()  # Add space between heroines