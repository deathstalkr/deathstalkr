from datetime import datetime

start_date = datetime(2021, 2, 3)  # Replace with your start date
placeholder = "{{EXPERIENCE}}"

# Calculate the experience
now = datetime.now()
years = now.year - start_date.year
months = now.month - start_date.month
if months < 0:
    years -= 1
    months += 12

# Format the experience string
experience = f"{years} years and {months} months"

# Read the README file
with open("README.md", "r") as file:
    readme = file.read()

# Replace the placeholder or old experience string
if placeholder in readme:
    updated_readme = readme.replace(placeholder, experience)
else:
    updated_readme = readme.replace(experience, experience)

# Write the updated README back to the file
with open("README.md", "w") as file:
    file.write(updated_readme)
