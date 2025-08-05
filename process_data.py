import csv
import os

DATA_DIRECTORY = "./data"
OUTPUT_FILE_PATH = "./formatted_data.csv"

# Open the output file for writing
with open(OUTPUT_FILE_PATH, "w", newline="") as output_file:
    writer = csv.writer(output_file)
    # Write the header
    writer.writerow(["sales", "date", "region"])

    # Iterate over all files in the data folder
    for file_name in os.listdir(DATA_DIRECTORY):
        # Process only CSV files
        if not file_name.endswith(".csv"):
            continue

        with open(f"{DATA_DIRECTORY}/{file_name}", "r", newline="") as input_file:
            reader = csv.reader(input_file)
            for row_index, input_row in enumerate(reader):
                # Skip the header row
                if row_index == 0:
                    continue

                product, raw_price, quantity, transaction_date, region = input_row

                if product == "pink morsel":
                    # Remove '$' from the price and convert to float
                    price = float(raw_price.replace("$", ""))
                    sale = price * int(quantity)
                    # Write the processed row
                    writer.writerow([sale, transaction_date, region])

print("Processing complete! Output written to formatted_data.csv")
