import csv
import random

def generate_random_salary(job_title):
    """Generate a random salary range based on job title."""
    salary_ranges = {
        "Data Analyst": (88, 138),
        "Data Engineer": (110000, 163000),
        "Senior Data Engineer": (162000, 238000),
        "Business Analyst": (99000, 170000),
        "Data Scientist": (90000, 180000),
        "Machine Learning Engineer": (90000, 175000),
        "Senior Data Analyst": (135000, 195000),
        "Cloud Engineer": (121000, 192000),
        "Senior Data Scientist": (196000, 302000),
        "Software Engineer": (128000, 207000),
    }

    min_salary, max_salary = salary_ranges.get(job_title, (40000, 100000))
    return random.uniform((min_salary, max_salary) , 2)

def process_csv():
    """Process the CSV file to add salary information."""
    input_file = "data_jobs.csv"  # Input file name
    output_file = "out.csv"  # Output file name

    with open(input_file, mode='r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        fieldnames = reader.fieldnames + ["salary_year_avg"]

        rows = []
        for row in reader:
            job_title = row.get("job_title_short", "")  # Adjusted field name
            row["salary_year_avg"] = generate_random_salary(job_title)
            rows.append(row)

    with open(output_file, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        writer.writerows(rows)

    print(f"Processed data saved to {output_file}")

def main():
    process_csv()

if __name__ == "__main__":
    main()
