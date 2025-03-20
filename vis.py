import sys
import pandas as pd
import matplotlib.pyplot as plt
import subprocess

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 vis.py <input-file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    df = pd.read_csv(input_file)
    
    # Automatically detect a numeric column (just as an example, GPA plot)
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    
    if numeric_cols:
        col_to_plot = numeric_cols[0]
        plt.figure(figsize=(8,6))
        df[col_to_plot].hist(bins=20)
        plt.title(f'Distribution of {col_to_plot}')
        plt.xlabel(col_to_plot)
        plt.ylabel('Frequency')
        plt.savefig('/home/doc-bd-a1/vis.png')  # Save to correct directory
        print(f"Visualization saved as /home/doc-bd-a1/vis.png")
    else:
        print("No numeric columns found for visualization.")

subprocess.run(["python3", "model.py", input_file])