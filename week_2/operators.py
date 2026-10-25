lives = int (input("Enter the number of lives: "))
print(lives)

energy = int (input("Enter the amount of energy: "))
print(energy)

shield = int (input("Enter the amount of shield: "))
print(shield)   

print("Health has been set")

#lives, energy level and shield as emojis
lives = "❤️" * lives    
energy = "⚡" * energy
shield = "🛡️" * shield

print("Lives: "+ lives)
print("Energy: "+ energy)
print("Shield: "+ shield)