# Simple In-Memory Database for Job Postings
job_postings_db = {}

# Simple In-Memory Database for Users
users_db = {
    'managers': {'company_manager': {'password': 'manager_password', 'role': 'manager'}},
    'users': {'job_seeker': {'password': 'seeker_password', 'role': 'user', 'applied_jobs': []}}
}

# Function to view job details
def view_job_details(job_id):
    job = job_postings_db.get(job_id)
    if job:
        print("Job ID:", job_id)
        print("Job Title:", job['job_title'])
        print("Company:", job['company'])
        print("Location:", job['location'])
        print("Requirements:", ', '.join(job['requirements']))
        print("Responsibilities:", '\n'.join(job['responsibilities']))
        print("Application Status:", job['application_status'])
        print("Number of Applicants:", len(job['applicants']))
        print()
    else:
        print("Job not found.")

# Function for user authentication
def authenticate_user(username, password, role):
    user_data = users_db.get(role, {}).get(username)
    if user_data and user_data['password'] == password:
        return user_data
    else:
        print(f"Authentication failed. Invalid username, password, or insufficient permissions.")
        return None

# Function for managers to create job posts
def create_job_post(manager_username):
    manager_data = authenticate_user(manager_username, input("Enter your password: "), 'managers')
    if manager_data:
        job_id = input("Enter a unique Job ID: ")
        if job_id not in job_postings_db:
            job_postings_db[job_id] = {
                'job_title': input("Enter Job Title: "),
                'company': manager_username,
                'location': input("Enter Job Location: "),
                'requirements': input("Enter Job Requirements (comma-separated): ").split(','),
                'responsibilities': input("Enter Job Responsibilities (one per line, end with an empty line): ").split('\n'),
                'application_status': 'Open',
                'applicants': []
            }
            print(f"Job ID {job_id} created successfully!")
        else:
            print("Job ID already exists. Please choose a unique Job ID.")
    else:
        print("Authentication failed. You do not have permission to create job posts or user not found.")

# Function for job seekers to view available jobs
def view_available_jobs():
    print("Available Jobs:")
    for job_id, job in job_postings_db.items():
        if job['application_status'] == 'Open':
            print(f"Job ID: {job_id}, Title: {job['job_title']}, Company: {job['company']}, Location: {job['location']}")

# Function for job seekers to apply for a job
def apply_for_job(job_id, username):
    job = job_postings_db.get(job_id)
    user_data = users_db.get('users', {}).get(username)
    
    if job and user_data:
        if job['application_status'] == 'Open':
            job['applicants'].append(username)
            user_data['applied_jobs'].append(job_id)
            print(f"Application submitted successfully for {username} to Job ID {job_id}!")
        else:
            print("Sorry, applications for this job are currently closed.")
    else:
        print("Job or user not found.")

# Function for job seekers to check the status of their applications
def check_application_status(username):
    user_data = users_db.get('users', {}).get(username)
    if user_data:
        print(f"Applications for {username}:")
        for job_id in user_data['applied_jobs']:
            job = job_postings_db.get(job_id)
            if job:
                print(f"Job ID: {job_id}, Title: {job['job_title']}, Company: {job['company']}, Status: {job['application_status']}")
            else:
                print(f"Job ID {job_id} not found.")
    else:
        print("User not found.")

# Main Program
while True:
    print("Welcome to the Job Platform!")
    print("1. Log in as a Manager")
    print("2. Log in as a Job Seeker")
    print("3. View Available Jobs")
    print("4. Check Application Status")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        manager_username = input("Enter your username: ")
        create_job_post(manager_username)

    elif choice == '2':
        job_seeker_username = input("Enter your username: ")
        job_seeker_password = input("Enter your password: ")
        job_seeker = authenticate_user(job_seeker_username, job_seeker_password, 'users')
        if job_seeker:
            print("Logged in as Job Seeker.")
            view_available_jobs()
            job_action = input("Do you want to apply for a job? (yes/no): ").lower()
            if job_action == 'yes':
                job_id_to_apply = input("Enter the Job ID to apply: ")
                apply_for_job(job_id_to_apply, job_seeker_username)

    elif choice == '3':
        view_available_jobs()

    elif choice == '4':
        job_seeker_username = input("Enter your username: ")
        check_application_status(job_seeker_username)

    elif choice == '5':
        print("Exiting the Job Platform. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
