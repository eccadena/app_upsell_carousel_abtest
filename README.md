# **A/B Test Analysis for Up-sell Carousel**
🚀 **Understanding the impact of store-brand vs. national-brand items in an up-sell carousel**

## **Project Overview**
This Streamlit application simulates an **A/B test** to analyze the impact of featuring **store-brand** vs. **national-brand** products in a grocery store’s **mobile app carousel**. The goal is to determine which option **drives more conversions and revenue per session**.

### **Business Question**
> Should the up-sell carousel prioritize **store-brand** or **national-brand** products to maximize conversion rates and revenue?

This app follows the **H.E.A.R.T. framework** to structure the experiment, analyze results, and provide a data-driven business decision.

---

## **H.E.A.R.T. Framework for A/B Testing**
### **1️⃣ Hypothesis & Business Goal**
- **Hypothesis:** Featuring national-brand products in the up-sell carousel will lead to a higher **conversion rate** and **revenue per session** compared to store-brand products.
- **Primary Metrics:**  
  - Conversion Rate (% of users making a purchase)
  - Revenue Per Session  
- **Secondary Metrics:**  
  - Average Order Value (AOV)  
  - Customer Lifetime Value (CLV)  

### **2️⃣ Experiment Design**
- **Test Type:** A/B test  
- **Control Group (A):** Users see a carousel with **store-brand** items.  
- **Treatment Group (B):** Users see a carousel with **national-brand** items.  
- **Randomization:** At **user-session level** to prevent biases.  
- **Duration:** Minimum **2 weeks** for robust statistical power.  

### **3️⃣ Analysis & Statistical Testing**
- **Chi-square test** → Compare conversion rates between groups.  
- **T-test** → Compare revenue per session for converted users.  
- **Bias Checks:**  
  - Ensure randomization is balanced  
  - Account for novelty effect & external influences  

### **4️⃣ Results Interpretation**
- If **conversion rate & revenue per session are significantly higher** for national brands, then we roll out the feature.  
- If **conversion rate is lower but revenue is higher**, we assess the **trade-off** of fewer but higher-value purchases.  
- If results are **inconclusive**, we explore further **segmentation analysis** (e.g., price-sensitive vs. brand-loyal users).  

### **5️⃣ Tactical Next Steps**
- ✅ **Go/No-Go Decision:** Deploy, iterate, or refine feature  
- 📊 **Long-term monitoring:** Measure post-experiment impact  
- 🔁 **Potential Iterations:** Test hybrid approaches (e.g., mixed store & national brands in carousel)  

---

## **App Features**
✅ **Simulates A/B Test Data** → Generate user-level conversion & revenue data  
✅ **Performs Statistical Tests** → Chi-square test & t-test for significance  
✅ **Visualizes Results** → Graphs for conversion rates & revenue distributions  
✅ **Provides Business Recommendations** → Data-driven decision-making  

---

## **How to Run the App**
### **1️⃣ Install Dependencies**
Ensure you have **Conda** installed, then create and activate the environment:

```bash
conda env create -f environment.yaml
conda activate my_env
```

### **2️⃣ Run the Streamlit App**
```bash
streamlit run app.py
```

### **3️⃣ Adjust Experiment Parameters**
- Use the **sidebar sliders** to change:
  - Number of users
  - Conversion rates
  - Average purchase amounts
  - Confidence level for statistical significance

### **4️⃣ Analyze Results**
- The app **simulates** an A/B test, performs **statistical tests**, and provides a **business decision** based on the data.

---

## **Expected Outcomes**
| Scenario                                         | Business Decision                  |
| ------------------------------------------------ | ---------------------------------- |
| **National-brand → Higher conversion & revenue** | ✅ Adopt national-brand in carousel |
| **Store-brand → Higher conversion or revenue**   | ✅ Stick with store-brand           |
| **No significant difference**                    | 🔄 Further iteration needed         |
| **Mixed results**                                | 📊 Additional segmentation analysis |

---

## **Additional Considerations**
📌 **Customer Segmentation:** Do different **user demographics** respond differently?  
📌 **Long-Term Impact:** Does the feature **increase repeat purchases** over time?  
📌 **Operational Feasibility:** Does switching to national brands impact **supply chain logistics**?  

---

## **Final Thoughts**
This app demonstrates **strong product sense** by:
✔️ Framing the problem using structured **A/B testing methodologies**  
✔️ Applying **statistical rigor** to analyze experiment results  
✔️ Making **data-driven business recommendations**  
✔️ Enabling **dynamic scenario testing** through an interactive Streamlit UI  

🚀 **Try it out and make informed decisions for better user engagement & revenue growth!**  

---
