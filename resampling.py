'''
This program will resample an experiment a number of times
in order to generate a distribution which can be used to determine
whether the null hypothesis/independence model should be accepted,
or if it should be rejected and the alternative model/hypothesis used
instead.

Hypothetical experiement here is whether GPA affects chances of receiving a
job offer.
'''

import pandas as pd
from random import shuffle

exp_df = pd.read_csv(r'/home/bzmccarthy/Scripts/Random/Data/gpa.csv')

def main():

    yes_exp_mean, no_exp_mean = find_mean(exp_df)
    num_yes, num_no = find_bins(exp_df)
    test_df = get_new_df(num_yes, num_no, exp_df)

def find_mean(df):

    yes_df = exp_df.loc[exp_df['job_offer_flag'] == 'Y']
    no_df = exp_df.loc[exp_df['job_offer_flag'] == 'N']

    yes_mean = yes_df.mean()['gpa']
    no_mean = no_df.mean()['gpa']

    return yes_mean, no_mean

def find_bins(exp_df):

    counts = exp_df['job_offer_flag'].value_counts()

    num_yes = counts['Y']
    num_no = counts['N']

    return num_yes, num_no

def get_new_df(num_yes, num_no, exp_df):

    nums_to_pull = list(range(num_yes+num_no))
    shuffle(nums_to_pull)
    yes_to_pull = nums_to_pull[:num_yes]
    no_to_pull = nums_to_pull[num_yes:num_yes+num_no]

    test_df = pd.DataFrame(columns=['gpa','job_offer_flag'])
    print(test_df)

    return test_df

if __name__ == '__main__':
    main()









