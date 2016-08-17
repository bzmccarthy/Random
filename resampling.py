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
import matplotlib.pyplot as plt

exp_df = pd.read_csv(r'/home/bzmccarthy/Scripts/Random/Data/gpa.csv')
num_pulls = 10000

def main():

    yes_test_means = []

    yes_exp_mean, no_exp_mean = find_mean(exp_df)
    num_yes, num_no = find_bins(exp_df)

    for i in range(num_pulls):

        test_df = get_new_df(num_yes, num_no, exp_df)
        yes_test_means.append(find_mean(test_df)[0])

    yes_test_means_df = pd.DataFrame(yes_test_means,columns=['gpa'])

    n, bins, patches = plt.hist(yes_test_means, 100, normed=1,
                                facecolor='green', alpha=0.75)
    plt.show()

    print("Experimental mean GPA for offers: " + str(yes_exp_mean))
    print("Resampling mean GPA for offers: " + str(yes_test_means_df.mean()['gpa']))
    print("Resampling max GPA mean: " + str(max(yes_test_means)))
    print("Resampling min GPA mean: " + str(min(yes_test_means)))

def find_mean(df):

    yes_df = df.loc[df['job_offer_flag'] == 'Y']
    no_df = df.loc[df['job_offer_flag'] == 'N']

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

    yes_gpas = []
    no_gpas = []

    for index in yes_to_pull:

        yes_gpas.append([exp_df.loc[index]['gpa'],'Y'])

    for index in no_to_pull:
        no_gpas.append([exp_df.loc[index]['gpa'],'N'])

    test_df = pd.DataFrame(yes_gpas, columns=['gpa','job_offer_flag'])
    test_df = test_df.append(pd.DataFrame(no_gpas, columns=['gpa','job_offer_flag']))

    return test_df

if __name__ == '__main__':
    main()









