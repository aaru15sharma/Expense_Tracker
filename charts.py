import matplotlib.pyplot as plt
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    port=3308,
    user="root",
    passwd="",
    database="expenses_users"
)

my_cursor = db.cursor()

y = "SELECT DATE_OF_EXPENSE, SUM(AMOUNT) AS TOTAL_AMOUNT FROM expenses WHERE USERNAME = %s GROUP BY DATE_OF_EXPENSE DESC"
u = "aarushisharma"
my_cursor.execute(y, [u])
result = my_cursor.fetchall()

Dates = []
amounts = []

for i in result:
    Dates.append(i[0])
    amounts.append(i[1])

print("Dates: ", Dates)
print("Amounts: ", amounts)

plt.plot(Dates, amounts)
plt.title('My Expenses')
plt.ylabel('Amount')
plt.xlabel('Date')
plt.grid(True, color='#f1f1f1')
plt.show()