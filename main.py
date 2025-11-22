# --------------------------------------------------------
# MAIN VOTING SYSTEM
# Uses modules with single functions
# --------------------------------------------------------

import random
from voter_operations import handle_voter_registration, voters, candidates
from vote_operations import display_election_results, votes

def setup_candidates():
    """Setup candidates at the beginning"""
    print("\n=== INDIAN VOTING SYSTEM ===")
    
    try:
        num = int(input("Enter number of candidates: "))
    except ValueError:
        print("Please enter a valid number!")
        return
    
    if num <= 0:
        print(" Number of candidates must be greater than 0!")
        return

    for i in range(1, num + 1):
        print(f"\nEnter details for Candidate {i}:")
        name = input("Candidate Name: ").strip()
        party = input("Party Name: ").strip()
        
        if not name or not party:
            print(" Candidate name and party cannot be empty!")
            continue
            
        cid = f"C{i}"
        candidates[cid] = {"name": name, "party": party}

    print("\n--- Candidates Registered Successfully ---\n")
    for cid, info in candidates.items():
        print(f"{cid} → {info['name']} ({info['party']})")

def cast_vote():
    """Handle voting process"""
    if not candidates:
        print("No candidates registered yet!")
        return
        
    voter_id = input("\nEnter your Voter ID: ").strip()

    if voter_id not in voters:
        print("Invalid Voter ID! Please register first.")
        return

    if voters[voter_id]["has_voted"]:
        print("You have already voted!")
        return

    print("\n--- CANDIDATES ---")
    for cid, info in candidates.items():
        print(f"{cid} → {info['name']} ({info['party']})")

    choice = input("\nEnter Candidate ID to vote: ").strip()

    if choice not in candidates:
        print("Invalid Candidate ID!")
        return

    votes[voter_id] = choice
    voters[voter_id]["has_voted"] = True

    print("🗳 Vote cast successfully!")

def main_menu():
    """Main program loop"""
    setup_candidates()
    
    # Check if candidates were setup successfully
    if not candidates:
        print(" Candidate setup failed. Exiting program.")
        return
    
    while True:
        print("\n" + "="*25 + " MAIN MENU " + "="*25)
        print("1. Register as Voter")
        print("2. Cast Vote")
        print("3. Show Results")
        print("0. Exit")
        print("="*61)

        choice = input("Enter your choice (0-3): ").strip()

        if choice == "1":
            handle_voter_registration()
        elif choice == "2":
            cast_vote()
        elif choice == "3":
            display_election_results()
        elif choice == "0":
            print("\nThank you for using the Indian Voting System! Goodbye!")
            break
        else:
            print(" Invalid Choice! Please enter 0, 1, 2, or 3.")

# Start the program


main_menu()
