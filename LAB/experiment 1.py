# Experiment 1: Student Average Score Analysis
# Description: Load student test scores from CSV using NumPy, calculate the mean score for each subject,
#              and identify the subject with the highest average score.

import numpy as np

# Load student scores from CSV (columns 1 to 4 correspond to Math, Science, English, History)
student_scores = np.loadtxt("Students_data.csv", delimiter=",", skiprows=1, usecols=(1, 2, 3, 4))
subjects = ["Math", "Science", "English", "History"]

# Calculate average score for each subject
average_scores = np.mean(student_scores, axis=0)

# Find subject with the highest average score
highest_subject = subjects[np.argmax(average_scores)]

# Output results
print("Average scores:", np.round(average_scores, 2))
print("Subject with highest average score:", highest_subject)
