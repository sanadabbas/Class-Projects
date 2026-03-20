"""
Dog Purchase System - Improved Version

This module manages a dog purchasing system with validation for breed, color, age, and price.
"""

# List to store purchased dogs
purchased_dogs = []

# List of available dogs and their price ranges
dog_breeds = {
    "Labrador": [500, 800, 1200, 1500],
    "Bulldog": [600, 1200, 1500, 2000],
    "Beagle": [300, 500, 800, 1200],
    "Poodle": [800, 1000, 2000, 2500],
    "Golden Retriever": [700, 1800],
}

# Allowed colors and age range for purchasing
dog_colors = ["Black", "White", "Brown", "Golden", "Gray"]
age_limit = (0, 15)  # Age range in years

# List of online stores and their price ranges per breed
dog_stores = [
    {"name": "Pet Store A", "prices": {"Labrador": 1200, "Bulldog": 1800, "Beagle": 800, "Poodle": 2000, "Golden Retriever": 1600}},
    {"name": "Dog Haven", "prices": {"Labrador": 1000, "Bulldog": 1500, "Beagle": 600, "Poodle": 2200, "Golden Retriever": 1400}},
    {"name": "Canine World", "prices": {"Labrador": 1300, "Bulldog": 1700, "Beagle": 700, "Poodle": 2400, "Golden Retriever": 1500}},
]


def get_integer_input(prompt, min_val, max_val):
    """
    Get validated integer input from user within a specified range.
    
    Args:
        prompt (str): The input prompt to display
        min_val (int): Minimum acceptable value
        max_val (int): Maximum acceptable value
    
    Returns:
        int: Valid integer within range, or None if invalid
    """
    try:
        value = int(input(prompt))
        if min_val <= value <= max_val:
            return value
        else:
            print(f"Error: Value must be between {min_val} and {max_val}.")
            return None
    except ValueError:
        print(f"Error: Please enter a valid number between {min_val} and {max_val}.")
        return None


def get_string_input(prompt, valid_options=None):
    """
    Get validated string input from user.
    
    Args:
        prompt (str): The input prompt to display
        valid_options (list): List of valid options (None means any non-empty string)
    
    Returns:
        str: Valid string input, or None if invalid
    """
    value = input(prompt).strip()
    
    if not value:
        print("Error: Input cannot be empty.")
        return None
    
    if valid_options and value not in valid_options:
        print(f"Error: Invalid option. Choose from: {', '.join(valid_options)}")
        return None
    
    return value


def display_available_dogs():
    """Display all available dog breeds and their price ranges."""
    print("\nAvailable Dog Breeds and Price Ranges:")
    for breed, price_range in dog_breeds.items():
        min_price = min(price_range)
        max_price = max(price_range)
        print(f"{breed}: ${min_price} - ${max_price}")


def display_store_prices(breed):
    """Display prices for a specific breed at all online stores.
    
    Args:
        breed (str): The dog breed to search for
    """
    print(f"\nPrices for {breed} at various stores:")
    for store in dog_stores:
        if breed in store["prices"]:
            print(f"{store['name']}: ${store['prices'][breed]}")


def purchase_dog(name, age, color, breed, price):
    """Add a purchased dog with validation.
    
    Args:
        name (str): Dog's name
        age (int): Dog's age in years
        color (str): Dog's color
        breed (str): Dog's breed
        price (float): Purchase price
    
    Returns:
        bool: True if purchase successful, False otherwise
    """
    # Validate breed
    if breed not in dog_breeds:
        print(f"Error: {breed} is not an available breed.")
        return False
    
    # Validate color
    if color not in dog_colors:
        print(f"Error: {color} is not available. Choose from {', '.join(dog_colors)}.")
        return False
    
    # Validate age
    if not (age_limit[0] <= age <= age_limit[1]):
        print(f"Error: Age must be between {age_limit[0]} and {age_limit[1]} years.")
        return False
    
    # Validate price using dynamic min/max
    price_range = dog_breeds[breed]
    min_price = min(price_range)
    max_price = max(price_range)
    
    if not (min_price <= price <= max_price):
        print(f"Error: Price must be between ${min_price} and ${max_price}.")
        display_store_prices(breed)
        return False
    
    # Add dog to purchased list
    purchased_dogs.append({
        "Name": name,
        "Age": age,
        "Color": color,
        "Breed": breed,
        "Price": price
    })
    print(f"Success: {name} the {breed} has been added to your purchases at ${price}!"
    return True


def display_dogs():
    """Display all purchased dogs."""
    if purchased_dogs:
        print("\nYou have purchased the following dogs:")
        for i, dog in enumerate(purchased_dogs, 1):
            print(f"{i}. Name: {dog['Name']}, Age: {dog['Age']} years, Color: {dog['Color']}, Breed: {dog['Breed']}, Price: ${dog['Price']}")
    else:
        print("\nYou haven't purchased any dogs yet.")


def menu_purchase_dog():
    """Handle the dog purchase menu flow."""
    name = input("Enter dog's name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return
    
    print("\nAvailable colors:", ", ".join(dog_colors))
    color = input("Enter dog's color: ").strip().title()
    if color not in dog_colors:
        print(f"Error: {color} is not available. Choose from {', '.join(dog_colors)}.")
        return
    
    print("\nAvailable breeds:", ", ".join(dog_breeds.keys()))
    breed = input("Enter dog breed: ").strip()
    if breed not in dog_breeds:
        print(f"Error: {breed} is not an available breed.")
        return
    
    age = get_integer_input("Enter dog's age (0-15): ", age_limit[0], age_limit[1])
    if age is None:
        return
    
    price_range = dog_breeds[breed]
    min_price = min(price_range)
    max_price = max(price_range)
    price = get_integer_input(f"Enter the price for the {breed} (${min_price}-${max_price}): ", min_price, max_price)
    if price is None:
        return
    
    purchase_dog(name, age, color, breed, price)


def menu_search_stores():
    """Handle the store price search menu flow."""
    print("\nAvailable breeds to search prices for:", ", ".join(dog_breeds.keys()))
    breed = input("Enter breed to search prices: ").strip()
    if breed in dog_breeds:
        display_store_prices(breed)
    else:
        print(f"Error: {breed} is not an available breed.")


def main_menu():
    """Display and handle the main menu."""
    while True:
        print("\n=== Dog Purchase System ===")
        print("1. View Available Dogs")
        print("2. Purchase a Dog")
        print("3. View Purchased Dogs")
        print("4. Search Online Stores")
        print("5. Exit")
        
        # Input validation for menu choice
        choice = get_integer_input("Enter your choice (1-5): ", 1, 5)
        
        if choice is None:
            continue
        
        if choice == 1:
            display_available_dogs()
        elif choice == 2:
            menu_purchase_dog()
        elif choice == 3:
            display_dogs()
        elif choice == 4:
            menu_search_stores()
        elif choice == 5:
            print("Thank you for using the Dog Purchase System!")
            break


def main():
    """Main entry point for the program."""
    userchoice = input("Would you like to buy dogs? (y/n): ").lower()
    if userchoice in ['y', 'yes']:
        main_menu()
    else:
        print("You have successfully exited the program.")


# Initial program entry point
if __name__ == "__main__":
    main()