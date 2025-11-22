# Voting-System
## Project Title: Indian Voting System
## Overview:
This project is a simplified console-based voting system written in Python.
It simulates how a basic voting process works in India, without requiring any admin login.

At the start of the program:

User enters number of candidates

User enters candidate names & party names

Voters can register and cast their vote

One voter = One vote

System displays the final election results and winner

This project is ideal for school/college assignments, B.Tech 1st year labs, or Python beginners.

## Features
✔️ Candidate Setup

System asks for number of candidates

User enters candidate & party details

Auto-assigns Candidate IDs (C1, C2, …)

✔️ Voter Registration

Voters can register with:

Name

Age

Age validation (must be 18 or above)

Auto-generated Voter ID (e.g., IND12345)

✔️ Voting System

Voter enters Voter ID to vote

One vote per voter (secure)

Vote stored in memory (dictionary)

✔️ Results

Shows total vote count for each candidate

Declares the winner

## Technologies / Tools Used
Python 3.x, 
Dictionaries & List, 
Random module, 
Console I/O

No external libraries are required.

## Steps to Install & Run the Project
1️⃣ Install Python

If not installed, download Python from:
https://www.python.org/downloads/

2️⃣ Create a project folder
IndianVotingSystem/

3️⃣ Create a Python file

Create file:

voting_system.py


Paste the full program code into it.

4️⃣ Run the program

Open terminal / command prompt:

python voting_system.py


The program will start and ask for number of candidates.

🧪 Instructions for Testing

Follow these steps to test the voting system:

✔️ Step 1: Enter number of candidates

Example:

Enter number of candidates: 3

✔️ Step 2: Enter candidate details
Candidate 1 Name: Rahul
Party: AAP
Candidate 2 Name: Sneha
Party: BJP
Candidate 3 Name: Arjun
Party: INC

✔️ Step 3: Register voters

From main menu → select option 1

Example:

Full Name: Ramesh
Age: 22
Your Voter ID is: IND54321

✔️ Step 4: Cast Votes

Choose option 2
Enter valid voter ID → choose candidate ID

✔️ Step 5: Show Results

Choose option 3
See votes per candidate & winner
