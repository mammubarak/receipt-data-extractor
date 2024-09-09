import re
import os
import pandas as pd

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

    print(f"Summary saved to {summary_file}")