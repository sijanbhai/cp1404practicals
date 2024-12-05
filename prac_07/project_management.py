import os
from project import Project
from datetime import datetime


def load_projects(filename):
    """Load projects from a file."""
    projects = []
    try:
        with open(filename, "r") as file:
            next(file)  # Skip header
            for line in file:
                project = Project.from_string(line.strip())
                projects.append(project)
        print(f"Loaded {len(projects)} projects from {filename}")
    except FileNotFoundError:
        print(f"{filename} not found.")
    return projects


def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(project.to_string() + "\n")
    print(f"Saved {len(projects)} projects to {filename}")


def display_projects(projects):
    """Display incomplete and completed projects, sorted by priority."""
    incomplete = [p for p in projects if not p.is_completed()]
    completed = [p for p in projects if p.is_completed()]

    print("\nIncomplete projects:")
    for project in sorted(incomplete):
        print(project)

    print("\nCompleted projects:")
    for project in sorted(completed):
        print(project)


def filter_projects_by_date(projects):
    """Filter and display projects that start after a given date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%y").date()

    filtered_projects = [p for p in projects if p.start_date > filter_date]
    print(f"\nProjects after {filter_date.strftime('%d/%m/%Y')}:")
    for project in sorted(filtered_projects, key=lambda p: p.start_date):
        print(project)


def add_new_project(projects):
    """Prompt the user to add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion_percent = input("Percent complete: ")

    new_project = Project(name, start_date, priority, cost_estimate, completion_percent)
    projects.append(new_project)
    print(f"New project added: {new_project}")


def update_project(projects):
    """Allow the user to update a project."""
    for idx, project in enumerate(projects):
        print(f"{idx} {project}")

    project_choice = int(input("Project choice: "))
    project = projects[project_choice]

    new_percentage = input(f"New Percentage ({project.completion_percent}): ")
    if new_percentage:
        project.completion_percent = int(new_percentage)

    new_priority = input(f"New Priority ({project.priority}): ")
    if new_priority:
        project.priority = int(new_priority)

    print(f"Updated project: {project}")


def main():
    projects = load_projects("projects.txt")

    while True:
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_choice = input("Would you like to save to projects.txt? (y/n): ")
            if save_choice.lower() == 'y':
                save_projects("projects.txt", projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
