### Exercices ###

'''
 1 - Python has the module called statistics and we can use this module to
do all the statistical calculations. However, to learn how to make function
and reuse function let us try to develop a program, which calculates
the measure of central tendency of a sample (mean, median, mode) and
measure of variability (range, variance, standard deviation). 
In addition to those measures, find the min, max, count, percentile, and
frequency distribution of the sample. You can create a class called 
Statistics and create all the functions that do statistical calculations as
methods for the Statistics class. Check the output below.
'''
class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return max(self.data) - min(self.data)

    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
        else:
            return sorted_data[n//2]

    def mode(self):
        frequency = {}
        for item in self.data:
            frequency[item] = frequency.get(item, 0) + 1
        max_frequency = max(frequency.values())
        modes = [key for key, value in frequency.items() if value == max_frequency]
        return {'mode': modes[0], 'count': max_frequency}

    def variance(self):
        mean = self.mean()
        return sum((x - mean) ** 2 for x in self.data) / len(self.data)

    def std(self):
        return self.variance() ** 0.5

    def freq_dist(self):
        frequency = {}
        for item in self.data:
            frequency[item] = frequency.get(item, 0) + 1
        return sorted(frequency.items(), key=lambda x: x[1], reverse=True)


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print("Count:", data.count())
print("Sum:", data.sum())
print("Min:", data.min())
print("Max:", data.max())
print("Range:", data.range())
print("Mean:", data.mean())
print("Median:", data.median())
print("Mode:", data.mode())
print("Variance:", data.variance())
print("Standard Deviation:", data.std())
print("Frequency Distribution:", data.freq_dist())

#=============================================================================
#Level 2
#=============================================================================

'''
 1 - Create a class called PersonAccount. It has firstname, lastname,
incomes, expenses properties and it has total_income, total_expense,
account_info, add_income, add_expense and account_balance methods.
Incomes is a set of incomes and its description. The same goes for expenses.
'''

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def total_income(self):
        return sum(income[0] for income in self.incomes)

    def total_expense(self):
        return sum(expense[0] for expense in self.expenses)

    def account_info(self):
        return f"Account Information for {self.firstname} {self.lastname}:\n" \
               f"Total Income: {self.total_income()}\n" \
               f"Total Expense: {self.total_expense()}\n" \
               f"Account Balance: {self.account_balance()}"

    def add_income(self, amount, description):
        self.incomes.append((amount, description))

    def add_expense(self, amount, description):
        self.expenses.append((amount, description))

    def account_balance(self):
        return self.total_income() - self.total_expense()


# Example usage:
person1 = PersonAccount("John", "Doe")
person1.add_income(5000, "Salary")
person1.add_income(1000, "Bonus")
person1.add_expense(1500, "Rent")
person1.add_expense(800, "Groceries")

print(person1.account_info())