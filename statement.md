## Problem Statement
The objective of this project is to design and develop a simple, console-based Indian Voting System using Python.
The system must allow users to:
Enter the number of candidates.
Enter the names of all candidates.
Allow multiple voters to cast their votes.
Ensure each voter can vote only once.
Display the final election results with vote counts and the winning candidate.
The system should be easy to use, secure from duplicate voting, and efficient for small-scale election simulations such as class-level or club-level elections.

## Scope of the Project
The scope of this project includes:
Basic voting functionality for a small group.
Prevention of duplicate votes using voter IDs.
Result generation with winner declaration.
Console-based interaction for simplicity.
No external admin panel or database; all operations occur at runtime.
The project does not include:
Biometric or OTP-based verification.
Large-scale or real-time election management.
Graphical interfaces or web connectivity.

## Target Users
This project is intended for:
Students learning Python programming.
Educators who want a simple election demo tool for class activities.
Small groups, clubs, or teams needing a basic voting simulation.
Beginners practicing Python input/output, loops, and dictionaries.

## High-Level Features
Dynamic Candidate Entry – Users specify the number of candidates and their names at the start.
Secure Voting – Each voter uses a unique Voter ID; repeated IDs are blocked.
Real-Time Vote Counting – Votes are instantly added to candidate totals.
Winner Declaration – The system automatically calculates and displays the winner.
User-Friendly Console Interface – Clear instructions for smooth usage.
Support for Multiple Voters – Keeps accepting votes until users choose to stop.
