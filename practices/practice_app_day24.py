import numpy as np

# Sample data for startup costs, additional capital, and revenue (in euros)
sample_data = {
    'SL': {
        'average_startup_costs': 10000,
        'average_additional_capital': 5000,
        'average_revenue_per_year': 20000
    },
    'SA': {
        'average_startup_costs': 15000,
        'average_additional_capital': 7000,
        'average_revenue_per_year': 30000
    }
}

def estimate_initial_capital(startup_costs, additional_capital):
    total_capital = startup_costs + additional_capital
    return total_capital

def calculate_years_to_profit(revenue_per_year, initial_capital):
    # Assuming profit is calculated after deducting startup costs and additional capital
    years_to_profit = initial_capital / revenue_per_year
    return years_to_profit

def main():
    # User input for company type and industry
    company_type = input("Enter company type (SL or SA): ")
    industry = input("Enter industry type: ")

    # User input for startup costs and additional capital
    try:
        startup_costs = float(input("Enter startup costs (in euros): "))
        additional_capital = float(input("Enter additional capital required (in euros): "))
    except ValueError:
        print("Invalid input. Please enter numerical values for startup costs and additional capital.")
        return

    # Estimate initial capital
    initial_capital = estimate_initial_capital(startup_costs, additional_capital)
    print("Estimated initial capital needed:", initial_capital, "euros")

    # Calculate average startup costs, additional capital, and revenue based on company type
    average_startup_costs = sample_data[company_type]['average_startup_costs']
    average_additional_capital = sample_data[company_type]['average_additional_capital']
    average_revenue_per_year = sample_data[company_type]['average_revenue_per_year']

    # Compare with averages
    startup_costs_difference = startup_costs - average_startup_costs
    additional_capital_difference = additional_capital - average_additional_capital

    print("Difference from average startup costs:", startup_costs_difference, "euros")
    print("Difference from average additional capital:", additional_capital_difference, "euros")

    # Calculate revenue needed for profitability and years to achieve profitability
    revenue_needed_for_profitability = initial_capital + (startup_costs_difference + additional_capital_difference)
    years_to_profit = calculate_years_to_profit(average_revenue_per_year, revenue_needed_for_profitability)

    print("Revenue needed for profitability:", revenue_needed_for_profitability, "euros")
    print("Years to achieve profitability based on average revenue:", years_to_profit, "years")

if __name__ == "__main__":
    main()
