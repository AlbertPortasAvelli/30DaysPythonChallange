# Simple JobFinder App

class User:
    def __init__(self, username, skills):
        self.username = username
        self.skills = skills
        self.profile_completed = False

    def complete_profile(self):
        print("Complete your profile:")
        self.name = input("Name: ")
        self.education = input("Education: ")
        self.experience = input("Work Experience: ")
        self.bio = input("Bio: ")
        self.profile_completed = True

    def display_profile(self):
        print(f"\nUser Profile - {self.username}")
        print(f"Name: {self.name}")
        print(f"Education: {self.education}")
        print(f"Work Experience: {self.experience}")
        print(f"Bio: {self.bio}")
        print("Skills:", ', '.join(self.skills) if self.skills else "No skills listed")

def job_search(user, location, industry):
    if user.profile_completed:
        print("\nJob Search Results:")
        print(f"Showing jobs in {location} related to {', '.join(user.skills)} skills.")
        # Default jobs for demonstration
        jobs = [
            {"title": "Software Developer", "company": "Tech Co", "location": "CityA"},
            {"title": "Data Analyst", "company": "Data Corp", "location": "CityB"},
            {"title": "UX Designer", "company": "Design Solutions", "location": "CityC"},
            {"title": "Marketing Specialist", "company": "Marketing Pro", "location": "CityD"},
        ]
        for job in jobs:
            print(f"\n{job['title']} at {job['company']} in {job['location']}")
    else:
        print("Please complete your profile before searching for jobs.")

def main():
    print("Welcome to JobFinder!")

    # User Registration
    username = input("Enter your username: ")
    skills = input("Enter your skills (comma-separated): ").split(',')

    # Create User
    user = User(username, skills)

    # Complete Profile
    user.complete_profile()

    # Display Profile
    user.display_profile()

    # Job Search
    location = input("Enter desired location for job search: ")
    industry = input("Enter desired industry for job search: ")

    # Perform Job Search
    job_search(user, location, industry)

if __name__ == "__main__":
    main()