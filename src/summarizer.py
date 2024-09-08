import re
import os
import pandas as pd

def summarize_receipt(text, output_folder, file_name):
    # Regular expressions to extract item name, quantity, and price
    item_pattern = re.compile(r"([A-Za-z\s]+)\s+(\d+)\s+([\d\.]+)")
    
    # Extract the subtotal, cash, and change
    subtotal_pattern = re.compile(r"Sub Total\s+([\d\.]+)", re.IGNORECASE)
    cash_pattern = re.compile(r"Cash\s+([\d\.]+)", re.IGNORECASE)
    change_pattern = re.compile(r"Change\s+([\d\.]+)", re.IGNORECASE)

    items = []
    subtotal = 0.0
    cash = 0.0
    change = 0.0

    # Extract item lines
    for match in item_pattern.finditer(text):
        item_name = match.group(1).strip()
        quantity = int(match.group(2))
        price = float(match.group(3))
        items.append({"Item": item_name, "Quantity": quantity, "Price": price})

    # Search for subtotal, cash, and change
    subtotal_match = subtotal_pattern.search(text)
    cash_match = cash_pattern.search(text)
    change_match = change_pattern.search(text)

    if subtotal_match:
        subtotal = float(subtotal_match.group(1))

    if cash_match:
        cash = float(cash_match.group(1))

    if change_match:
        change = float(change_match.group(1))

    # change = cash - subtotal

    # Create a pandas DataFrame for the items
    df_items = pd.DataFrame(items)

    # Save the summary to CSV
    save_summary(df_items, subtotal, cash, change, output_folder, file_name)

    print(f"|__ Summarized receipt: {file_name}\n")
    print(df_items)
    print(f"\nSub Total: {subtotal}")
    print(f"Cash: {cash}")
    print(f"Change: {change}")

    return df_items, subtotal, cash, change

def save_summary(df, subtotal, cash, change, output_folder, file_name):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    summary_file = os.path.join(output_folder, f"{file_name}_summary.csv")
    df.to_csv(summary_file, index=False)

    # Save totals to a separate file or append it to the summary
    with open(os.path.join(output_folder, f"{file_name}_totals.txt"), "w") as f:
        f.write(f"Sub Total: {subtotal}\n")
        f.write(f"Cash: {cash}\n")
        f.write(f"Change: {change}\n")

    print(f"|__ Summary saved to {summary_file}")