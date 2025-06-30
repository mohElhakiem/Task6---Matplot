import matplotlib.pyplot as plt


days = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]

temp = [35,37,33,42,36,39,40]


plt.figure(figsize=(10, 8))
plt.plot(days, temp, marker='o', linestyle='-', color='brown')

plt.title("Reports of this week's temperatures")
plt.xlabel("Days of the week")
plt.ylabel("Temperatures of the week")
plt.xticks(rotation=45)
plt.show()