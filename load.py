import sys
import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        print("Column names and data types:")
        print(df.dtypes)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 load.py <dataset-path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    df = load_data(file_path)
    
    if df is not None:
        output_file = "loaded_data.csv"
        df.to_csv(output_file, index=False)
        print(f"Data saved to {output_file}")
        
        # Invoke the next script
        import subprocess
        subprocess.run(["python3", "dpre.py", output_file])