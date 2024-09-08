import os
import matplotlib.pyplot as plt

def compare_receipts(summary_folder, output_folder):
    summary_files = [f for f in os.listdir(summary_folder) if f.endswith('_totals.txt')]

    # Initialize a list to store data
    data = []

    # Read each totals.txt and extract the total
    for summary_file in summary_files:
        total_file_path = os.path.join(summary_folder, summary_file)

        # Read the total from the total.txt file
        with open(total_file_path, "r") as f:
            lines = f.readlines()
            subtotal_line = [line for line in lines if "Sub Total" in line][0]
            total = float(subtotal_line.split(":")[1].strip())

        # Append the filename (receipt name) and total to the data list
        receipt_name = summary_file.replace("_totals.txt", "")
        data.append({"Receipt": receipt_name, "Total": total})

    # Create a bar chart
    receipts = [entry["Receipt"] for entry in data]
    totals = [entry["Total"] for entry in data]

    plt.figure(figsize=(10, 6))
    plt.bar(receipts, totals, color='blue')
    plt.title("Comparison of Receipts")
    plt.xlabel("Receipt")
    plt.ylabel("Total Amount")
    plt.xticks(rotation=45, ha="right")

    # Save the plot
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    output_path = os.path.join(output_folder, "comparison_chart.png")
    plt.savefig(output_path)
    plt.show()

    print(f"|__ Comparison chart saved to {output_path}")