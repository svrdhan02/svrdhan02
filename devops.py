
def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    
    current_year = 2024  # You can change this to the current year
    
    years_to_100 = 100 - age
    year_turn_100 = current_year + years_to_100
    
    print(f"Hello, {name}!")
    print(f"You will turn 100 years old in the year {year_turn_100}.")
if __name__ == "__main__":
   