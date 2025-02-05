import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Streamlit App Title
st.title("A/B Test Analysis for Up-sell Carousel")

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["Question", "Understanding the Question", "Pseudocode and Solution", "App"])

with tab1:
    st.header("Question")
    st.write("""
    In this scenario, we're evaluating whether the up-sell carousel in a grocery store's mobile app should feature store-brand items or national-brand products.
    """)

with tab2:
    st.header("Understanding the Question")
    st.write("""
    ### H.E.A.R.T. Framework for Data Science Interviews

    #### Hypothesis & Business Goal
    - **Problem:** What business metric are we trying to improve?
    - **Hypothesis:** We hypothesize that showing national brands in the upsell carousel will lead to higher conversion rates than in-store brands, increasing revenue per session.
    - **Success Metrics:** 
        - Primary: Conversion rate, revenue per session
        - Secondary: Average order value (AOV), profit margin

    #### Experiment Design & Data Collection
    - **Test Type:** A/B test
    - **Randomization Strategy:** Randomize at the user-session level to ensure fair comparisons.
    - **Control vs Treatment:** 
        - Control (A): Carousel featuring in-store brands
        - Treatment (B): Carousel featuring national brands
    - **Duration & Sample Size:** Run for at least 2 weeks to capture different shopping behaviors and ensure enough power to detect significant changes.

    #### Analysis & Statistical Testing
    - **Statistical Tests:** 
        - Two-sample t-test to compare mean revenue per session
        - Chi-square test for conversion rate differences
    - **Effect Size & Confidence Intervals:** Assess the magnitude of impact and statistical significance.
    - **Bias Checks:** Check for biases such as selection bias, novelty effect, and Simpson’s paradox.

    #### Results Interpretation & Business Impact
    - **Test Success:** Determine if the uplift is significant.
    - **Trade-offs & Secondary Metrics:** Evaluate if revenue increased at the cost of higher return rates.
    - **Segmentation Analysis:** Analyze if different user groups behaved differently (e.g., price-sensitive vs. brand-loyal customers).

    #### Tactical Next Steps & Decision Making
    - **Go / No-go Decision:** Decide whether to roll out the feature.
    - **Iterate or Scale:** Determine if any adjustments are needed.
    - **Long-term Monitoring:** Plan how to track the feature’s impact over time.

    ### Example Answer Using H.E.A.R.T.
    **Question:** "How would you evaluate whether showing national brands vs. in-store brands in a carousel upsell feature drives more revenue?"

    **H (Hypothesis & Business Goal)**
    - Hypothesis: "Displaying national brands in the carousel will increase conversion rates and revenue per session compared to in-store brands."
    - Success metrics:
        - Primary: Conversion rate, revenue per session
        - Secondary: Average order value (AOV), profit margin

    **E (Experiment Design & Data Collection)**
    - Conduct an A/B test with two variations:
        - Control (A): Carousel featuring in-store brands
        - Treatment (B): Carousel featuring national brands
    - Randomize at the user-session level
    - Ensure power calculation to detect at least a 2% conversion uplift
    - Run for at least 2 weeks to capture different shopping behaviors

    **A (Analysis & Statistical Testing)**
    - Use a two-sample t-test to compare mean revenue per session
    - Chi-square test for conversion rate differences
    - Check for novelty bias (users engaging more due to a new feature)
    - Segment users by demographics, purchase history

    **R (Results Interpretation & Business Impact)**
    - If revenue per session increased by 5% with national brands and is statistically significant, we consider rolling out
    - If conversion rate drops but AOV increases, we assess the trade-off (fewer but higher-value purchases)

    **T (Tactical Next Steps & Decision Making)**
    - If successful, roll out to all users
    - If inconclusive, refine (e.g., test mix of both brand types)
    - If negative impact, consider alternative placements (e.g., showing both brand types)
    """)

with tab3:
    st.header("Pseudocode and Solution")
    st.write("""
    ### Pseudocode for A/B Test Analysis

    1. **Define the Objective:**
        - Evaluate the effectiveness of store-brand vs. national-brand items in an up-sell carousel.

    2. **Set Parameters:**
        - Number of users (e.g., 10,000).
        - Conversion rates for store-brand and national-brand items.
        - Average purchase amounts and standard deviations for both groups.
        - Confidence level for statistical tests.

    3. **Simulate User Data:**
        - Randomly assign users to control (store-brand) or treatment (national-brand) groups.
        - Simulate conversion behavior based on predefined rates.
        - Simulate purchase amounts for converted users.

    4. **Analyze Results:**
        - Calculate conversion rates for both groups.
        - Calculate average purchase amounts for converted users in both groups.
        - Perform Chi-Square test to compare conversion rates.
        - Perform T-Test to compare average purchase amounts.

    5. **Make Decisions:**
        - Determine statistical significance based on p-values and confidence intervals.
        - Provide business recommendations based on test outcomes.

    ### Additional Metrics to Consider:
    - **Customer Lifetime Value (CLV):** Estimate the long-term value of customers acquired through each group.
    - **Retention Rate:** Measure how many users return to make additional purchases.
    - **Average Order Value (AOV):** Calculate the average value of orders placed by users in each group.
    - **Click-Through Rate (CTR):** Measure the percentage of users who click on the carousel items.
    - **Bounce Rate:** Measure the percentage of users who leave the app after viewing the carousel.

    ### Expected Outcomes:
    - **Higher Conversion Rate:** Indicates which group is more effective at converting users.
    - **Higher Average Purchase Amount:** Indicates which group generates more revenue per converted user.
    - **Statistical Significance:** Helps determine if observed differences are likely due to the changes in the carousel.

    ### Business Outcomes:
    - **Adopt National-Brand Items:** If national-brand items show significantly better performance.
    - **Stick with Store-Brand Items:** If there is no significant difference or store-brand performs better.
    - **Further Investigation:** If results are mixed or inconclusive, conduct additional tests or gather more data.

    ### Visualization:
    - The app provides a way to visualize the data and results, making it easier to interpret and communicate findings.
    """)

with tab4:
    st.header("App")

    # Sidebar for Parameter Inputs
    st.sidebar.header("Simulation Parameters")

    # User Inputs
    n_users = st.sidebar.slider("Number of Users", min_value=1000, max_value=20000, value=10000, step=1000)
    conversion_rate_store_brand = st.sidebar.slider("Store-Brand Conversion Rate (%)", min_value=1, max_value=20, value=8) / 100
    conversion_rate_national_brand = st.sidebar.slider("National-Brand Conversion Rate (%)", min_value=1, max_value=20, value=10) / 100

    # Purchase Amount Distribution Inputs
    st.sidebar.subheader("Purchase Amount Distribution")
    store_brand_mean = st.sidebar.slider("Store-Brand Average Purchase ($)", min_value=1.0, max_value=20.0, value=5.0, step=0.5)
    store_brand_std = st.sidebar.slider("Store-Brand Purchase Std Dev", min_value=0.5, max_value=5.0, value=1.5, step=0.1)

    national_brand_mean = st.sidebar.slider("National-Brand Average Purchase ($)", min_value=1.0, max_value=20.0, value=6.0, step=0.5)
    national_brand_std = st.sidebar.slider("National-Brand Purchase Std Dev", min_value=0.5, max_value=5.0, value=2.0, step=0.1)

    # Confidence Interval for Decision Making
    confidence_interval = st.sidebar.slider("Confidence Level (%)", min_value=90, max_value=99, value=95)
    alpha = 1 - (confidence_interval / 100)

    # Section 2: Simulating the Experiment
    st.subheader("Simulating the Experiment")
    st.write("""
    We assume the A/B test has been conducted, and now we're analyzing the results.

    ### Group Assignment
    Users are randomly assigned to one of two groups:
    - **Control Group:** Exposed to store-brand items.
    - **Treatment Group:** Exposed to national-brand items.

    This random assignment helps ensure unbiased results. Other methods could include stratified sampling if user demographics influence purchase behavior.
    """)

    # Simulate Data
    np.random.seed(42)

    # Simulating users split into control (store-brand) and treatment (national-brand)
    users = pd.DataFrame({
        'user_id': range(1, n_users + 1),
        'group': np.random.choice(['control', 'treatment'], size=n_users, p=[0.5, 0.5])
    })

    # Simulate conversion behavior
    users['converted'] = users.apply(lambda row: 
        np.random.binomial(1, conversion_rate_store_brand) if row['group'] == 'control' 
        else np.random.binomial(1, conversion_rate_national_brand), axis=1)

    # Simulate purchase amount for those who converted
    users['purchase_amount'] = users['converted'] * np.where(
        users['group'] == 'control', 
        np.random.normal(store_brand_mean, store_brand_std, n_users), 
        np.random.normal(national_brand_mean, national_brand_std, n_users)
    )

    # Display Simulated Data
    st.subheader("Simulated User Data")
    st.write("This is the dataset of users, their group assignments, conversion status, and purchase amounts.")
    st.dataframe(users)

    # Section 3: Analyzing the Results
    st.subheader("Analyzing the Results")
    st.write("""
    To determine if there's a significant difference between the groups, we use statistical tests:
    """)

    # Analysis
    control_group = users[users['group'] == 'control']
    treatment_group = users[users['group'] == 'treatment']

    control_conversion_rate = control_group['converted'].mean()
    treatment_conversion_rate = treatment_group['converted'].mean()

    control_avg_purchase = control_group[control_group['converted'] == 1]['purchase_amount'].mean()
    treatment_avg_purchase = treatment_group[treatment_group['converted'] == 1]['purchase_amount'].mean()

    # Statistical Tests
    conversion_table = pd.crosstab(users['group'], users['converted'])
    st.write("""Conversion Table/Cross Tabulation:
    We create a cross-tabulation of groups vs. conversion status to summarize the data in a contingency table.
             """)
    st.write(conversion_table)

    chi2, p_value_conversion, _, _ = stats.chi2_contingency(conversion_table)
    st.write(f"""
    **Chi-Square Test for Conversion Rates:**
    - p-value = {p_value_conversion:.4f}

    The Chi-Square test evaluates whether there is a significant association between the group assignment (store-brand vs. national-brand) and the conversion rate.
    A p-value less than {alpha} indicates a statistically significant difference in conversion rates between the two groups.
    For more information on statistical tests and when to use them, check out this [resource video](https://www.youtube.com/watch?v=dYJLUvo0Q6g).
    """)

    control_purchases = control_group[control_group['converted'] == 1]['purchase_amount']
    treatment_purchases = treatment_group[treatment_group['converted'] == 1]['purchase_amount']
    t_stat, p_value_purchase = stats.ttest_ind(control_purchases, treatment_purchases)
    st.write(f"""
    **T-Test for Average Purchase Amounts:**
    - p-value = {p_value_purchase:.4f}

    The T-Test evaluates whether there is a significant difference in the average purchase amounts between the store-brand and national-brand groups among users who converted.
    A p-value less than {alpha} indicates a statistically significant difference in average purchase amounts between the two groups.
    For more information on statistical tests and when to use them, check out this [resource video](https://www.youtube.com/watch?v=dYJLUvo0Q6g).
    """)

    # Display Results
    st.subheader("Statistical Results")
    st.markdown(f"**Conversion Rates:** Store-Brand = {control_conversion_rate:.2%}, National-Brand = {treatment_conversion_rate:.2%} (p-value = {p_value_conversion:.4f})")
    st.markdown(f"**Average Purchases (Converted Users):** Store-Brand = \${control_avg_purchase:.2f}, National-Brand = \${treatment_avg_purchase:.2f} (p-value = {p_value_purchase:.4f})", unsafe_allow_html=True)

    # Decision Logic
    if p_value_conversion < alpha and p_value_purchase < alpha:
        decision = "National-Brand items perform significantly better."
    elif p_value_conversion >= alpha and p_value_purchase >= alpha:
        decision = "No significant difference; consider sticking with Store-Brand items."
    else:
        decision = "Mixed results; further investigation needed."

    st.subheader("Decision")
    st.write(f"At a {confidence_interval}% confidence level, the conclusion is: **{decision}**")

    # Section 4: Visualizing the Data
    st.subheader("Visualizing the Data")

    # Conversion Rate Bar Chart
    fig1, ax1 = plt.subplots()
    ax1.bar(['Store-Brand', 'National-Brand'], [control_conversion_rate, treatment_conversion_rate], color=['blue', 'orange'])
    ax1.set_ylabel('Conversion Rate')
    ax1.set_title('Conversion Rates by Group')
    st.pyplot(fig1)

    # Purchase Amount Box Plot
    fig2, ax2 = plt.subplots()
    users[users['converted'] == 1].boxplot(column='purchase_amount', by='group', ax=ax2)
    ax2.set_title('Purchase Amount Distribution by Group')
    ax2.set_xlabel('Group')
    ax2.set_ylabel('Purchase Amount ($)')
    plt.suptitle('')
    st.pyplot(fig2)

    # Sidebar Explanation Section
    st.sidebar.subheader("Explanation")
    st.sidebar.write("""
    This app simulates an A/B test to compare the effectiveness of store-brand vs. national-brand items in an up-sell carousel.

    1. **Adjust Parameters:** Modify the number of users, conversion rates, and purchase behavior.
    2. **Analyze Results:** View conversion rates, average purchases, and statistical significance.
    3. **Make Decisions:** Based on p-values and confidence intervals, determine which option performs better.
    4. **Visualize Data:** Graphs help interpret outcomes.
    """)
