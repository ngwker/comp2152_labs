"""
Author: Ahmed Abdo
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton"
preferred_weight_kg = 20.5
highest_reps = 25

# Step c: Create a dictionary named workout_stats
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (25, 50, 40),
    "Taylor": (20, 30, 25)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
for friend, minutes in workout_stats.copy().items():
    total = sum(minutes)
    workout_stats[f"{friend}_Total"] = total

# Step e: Create a 2D nested list called workout_list
workout_list = [list(workout_stats[friend]) for friend in ["Alex", "Jamie", "Taylor"]]

# Step f: Slice the workout_list
yoga_running = [row[:2] for row in workout_list]
print("Yoga and Running minutes for all friends:")
print(yoga_running)


weightlifting_last2 = [row[2] for row in workout_list[-2:]]
print("\nWeightlifting minutes for last two friends:")
print(weightlifting_last2)

# Step g: Check if any friend's total >= 120
print("\nFriends with total workout >= 120 minutes:")
for friend in ["Alex", "Jamie", "Taylor"]:
    if workout_stats[f"{friend}_Total"] >= 120:
        print(f"Great job staying active, {friend}!")

# Step h: User input to look up a friend
friend_name = input("\nEnter a friend's name to check stats: ")
if friend_name in ["Alex", "Jamie", "Taylor"]:
    minutes = workout_stats[friend_name]
    total = workout_stats[f"{friend_name}_Total"]
    print(f"{friend_name}'s workout minutes (Yoga, Running, Weightlifting): {minutes}")
    print(f"Total workout minutes: {total}")
else:
    print(f"Friend {friend_name} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
totals = {friend: workout_stats[f"{friend}_Total"] for friend in ["Alex", "Jamie", "Taylor"]}
max_friend = max(totals, key=totals.get)
min_friend = min(totals, key=totals.get)

print(f"\nFriend with highest total workout minutes: {max_friend} ({totals[max_friend]} minutes)")
print(f"Friend with lowest total workout minutes: {min_friend} ({totals[min_friend]} minutes)")
