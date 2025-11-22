# --------------------------------------------------------
# VOTE OPERATIONS MODULE
# Handles voting and results
# --------------------------------------------------------

from voter_operations import voters, candidates, votes

def display_election_results():
    """Calculate and display election results"""
    print("\n===== ELECTION RESULTS =====")
    
    if not votes:
        print("No votes cast yet!")
        return

    # Count votes for each candidate
    vote_count = {}
    for cid in candidates:
        vote_count[cid] = 0
    
    for candidate_id in votes.values():
        if candidate_id in vote_count:
            vote_count[candidate_id] += 1

    # Display results
    for cid, count in vote_count.items():
        candidate_info = candidates[cid]
        print(f"{candidate_info['name']} ({candidate_info['party']}): {count} votes")

    # Find winner
    winner_id = max(vote_count, key=vote_count.get)
    winner_info = candidates[winner_id]
    
    print(f"\n WINNER: {winner_info['name']} ({winner_info['party']})")
    
    # Show statistics
    total_voters = len(voters)
    total_votes = len(votes)
    print(f"\nTotal Registered Voters: {total_voters}")

    print(f"Total Votes Cast: {total_votes}")
