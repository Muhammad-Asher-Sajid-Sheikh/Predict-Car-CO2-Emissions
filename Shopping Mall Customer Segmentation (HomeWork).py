'''
Project 3: Shopping Mall Customer Segmentation
Question: Can we group customers into "clusters" based on their spending score and income without being told who is who?

The Data
Income: Annual income in thousands.

SpendScore: Score from 1-100 based on behavior.

'''
# 1. Data
income = [15, 16, 17, 20, 80, 85, 90, 120, 125]
score = [39, 81, 6, 77, 40, 50, 45, 90, 85]
data = list(zip(income, score))