from scipy import stats

pearson_coef, p_value = stats.pearsonr(df['series_1'], df['series_2'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)  
