import pandas as pd
import sys

def clean_data(input1, input2, output):

    contact_df = pd.read_csv(input1)
    other_df = pd.read_csv(input2)


    merged_df = pd.merge(contact_df, other_df, left_on='respondent_id', right_on='id')


    merged_df.drop(columns='id', inplace=True)


    merged_df.dropna(inplace=True)


    merged_df = merged_df[~merged_df['job'].str.contains('insurance', case=False)]


    merged_df.to_csv(output, index=False)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python clean.py <input1> <input2> <output>")
        sys.exit(1)

    input1 = sys.argv[1]
    input2 = sys.argv[2]
    output = sys.argv[3]

    clean_data(input1, input2, output)