import sys
import pandas as pd
from sklearn.cluster import KMeans

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 model.py <input-file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    df = pd.read_csv(input_file)
    
    features = ['University_GPA', 'Internships_Completed', 'Projects_Completed', 'Soft_Skills_Score', 'Networking_Score']
    
    # Check if columns exist
    missing = [col for col in features if col not in df.columns]
    if missing:
        print(f"Missing columns: {missing}")
        sys.exit(1)
    
    X = df[features]
    
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(X)
    
    labels = kmeans.labels_
    cluster_counts = pd.Series(labels).value_counts().sort_index()
    
    output_file = "/home/doc-bd-a1/k.txt"
    with open(output_file, 'w') as f:
        for i, count in enumerate(cluster_counts):
            f.write(f"Cluster {i}: {count} records\n")
    
    print(f"Cluster counts saved to {output_file}")
