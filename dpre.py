import sys
import pandas as pd
import numpy as np

def clean_data(df):
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Handle missing values
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
    
    # Convert categorical variables to numerical
    if 'Gender' in df.columns:
        df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1, 'Other': 2})
    if 'Field_of_Study' in df.columns:
        df['Field_of_Study'] = pd.Categorical(df['Field_of_Study']).codes
    if 'Current_Job_Level' in df.columns:
        df['Current_Job_Level'] = pd.Categorical(df['Current_Job_Level']).codes
    if 'Entrepreneurship' in df.columns:
        df['Entrepreneurship'] = df['Entrepreneurship'].map({'No': 0, 'Yes': 1})
    
    # Convert numeric columns to float64
    numeric_columns = ['Age', 'High_School_GPA', 'SAT_Score', 'University_Ranking', 'University_GPA',
                       'Internships_Completed', 'Projects_Completed', 'Certifications', 'Soft_Skills_Score',
                       'Networking_Score', 'Job_Offers', 'Starting_Salary', 'Career_Satisfaction',
                       'Years_to_Promotion', 'Work_Life_Balance']
    for col in numeric_columns:
        if col in df.columns:
            df[col] = df[col].astype('float64')
    
    return df

def transform_data(df):
    # Normalize numerical columns
    numeric_columns = ['Age', 'High_School_GPA', 'SAT_Score', 'University_Ranking', 'University_GPA',
                       'Internships_Completed', 'Projects_Completed', 'Certifications', 'Soft_Skills_Score',
                       'Networking_Score', 'Job_Offers', 'Starting_Salary', 'Career_Satisfaction',
                       'Years_to_Promotion', 'Work_Life_Balance']
    existing_numeric_columns = [col for col in numeric_columns if col in df.columns]
    df[existing_numeric_columns] = (df[existing_numeric_columns] - df[existing_numeric_columns].min()) / (df[existing_numeric_columns].max() - df[existing_numeric_columns].min())
    
    return df

def discretize_data(df):
    if 'Starting_Salary' in df.columns:
        # Discretize 'Starting_Salary' into bins
        df['Salary_Bin'] = pd.cut(df['Starting_Salary'], bins=[0, 0.33, 0.66, 1], labels=['Low', 'Medium', 'High'])
    else:
        print("Warning: 'Starting_Salary' column not found. Skipping discretization.")
    
    return df

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 dpre.py <input-file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    df = pd.read_csv(input_file)
    
    df = clean_data(df)
    df = transform_data(df)
    df = discretize_data(df)
    
    output_file = "/home/doc-bd-a1/res_dpre.csv"
    df.to_csv(output_file, index=False)
    print(f"Processed data saved to {output_file}")
    
    # Invoke the next script
    import subprocess
    subprocess.run(["python3", "eda.py", output_file])