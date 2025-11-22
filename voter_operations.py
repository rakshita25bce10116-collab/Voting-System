# --------------------------------------------------------
# VOTER OPERATIONS MODULE
# Handles all voter-related functions
# --------------------------------------------------------

import random

# Global data storage
voters = {}
candidates = {}
votes = {}

def handle_voter_registration():
    """Register a new voter and return voter ID"""
    print("\n--- VOTER REGISTRATION ---")
    name = input("Enter Full Name: ")
    
    try:
        age = int(input("Enter Age: "))
    except ValueError:
        print("❌ Please enter a valid age!")
        return None

    if age < 18:
        print("❌ You must be 18+ to register.")
        return None

    # Generate unique voter ID
    while True:
        voter_id = f"IND{random.randint(10000, 99999)}"
        if voter_id not in voters:
            break
    
    voters[voter_id] = {
        "name": name,
        "age": age,
        "has_voted": False
    }

    print(f"\n✅ Registration Successful! Your Voter ID is: {voter_id}")
    return voter_id