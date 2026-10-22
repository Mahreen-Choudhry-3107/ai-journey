# plt.scatter(x, y, color='color_nmae', marker='marker-style', label='label name')
import matplotlib.pyplot as plt

hours_studies = [1,2,3,4,5,6,7,8]
exam_scores = [50, 55, 60, 65, 70, 75, 80, 85]

# scatter plot
plt.scatter(hours_studies, exam_scores, color='green', marker='o', label='Student Data')

plt.xlabel('Hours studied')
plt.ylabel('Exam Score')
plt.title('Relationship Between Study time and Exam Score')
plt.legend()
plt.grid(True)



# Two classes
# plt.scatter(x, y, color='color_nmae', marker='marker-style', label='label name')

# scatter plot
plt.scatter([1,2,3], [50, 55, 60], color='blue', label='Class A') #g1
plt.scatter([1,2,3], [45, 50, 52], color='orange', label='Class B') #g1

plt.xlabel('Hours studied')
plt.ylabel('Exam Score')
plt.title('Comparison of Two Classes')
plt.legend()
plt.grid(True)