import sys
import pandas as pd

def generate_insights(df):
    insights = []
    
    # Insight 1: Correlation between University GPA and Starting Salary
    if 'University_GPA' in df.columns and 'Starting_Salary' in df.columns:
        corr = df['University_GPA'].corr(df['Starting_Salary'])
        insights.append(f"Correlation between University GPA and Starting Salary: {corr:.2f}")
    else:
        print("Warning: 'University_GPA' or 'Starting_Salary' column not found. Skipping correlation insight.")
    
    # Insight 2: Average number of job offers by field of study
    if 'Field_of_Study' in df.columns and 'Job_Offers' in df.columns:
        avg_offers = df.groupby('Field_of_Study')['Job_Offers'].mean().sort_values(ascending=False)
        insights.append(f"Top 3 fields with highest average job offers: {avg_offers.head(3).to_string()}")
    else:
        print("Warning: 'Field_of_Study' or 'Job_Offers' column not found. Skipping job offers insight.")
    
    # Insight 3: Percentage of entrepreneurs by gender
    if 'Gender' in df.columns and 'Entrepreneurship' in df.columns:
        entrepreneur_rate = df.groupby('Gender')['Entrepreneurship'].mean() * 100
        insights.append(f"Percentage of entrepreneurs by gender: {entrepreneur_rate.to_string()}%")
    else:
        print("Warning: 'Gender' or 'Entrepreneurship' column not found. Skipping entrepreneurship insight.")
    
    return insights

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 eda.py <input-file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    df = pd.read_csv(input_file)
    
    insights = generate_insights(df)
    
    for i, insight in enumerate(insights, 1):
        output_file = f"/home/doc-bd-a1/eda-in-{i}.txt"
        with open(output_file, 'w') as f:
            f.write(insight)
        print(f"Insight {i} saved to {output_file}")

    
    # Invoke the next script
    import subprocess
    subprocess.run(["python3", "vis.py", input_file])