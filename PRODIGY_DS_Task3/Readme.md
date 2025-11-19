📊 Decision Tree Classifier – Bank Marketing Dataset  
A machine learning project built using a Decision Tree Classifier to predict whether a customer will subscribe to a bank’s term deposit.  
This project was fully developed and executed in Google Colab.

🚀 Project Overview

This project uses a cleaned sample of the Bank Marketing Dataset from the UCI Machine Learning Repository.  
The goal is to classify customer responses (`yes`/`no`) based on demographic and behavioral features.

🧠 Objective

To build a Decision Tree model that predicts customer subscription decisions using features such as age, job type, marital status, balance, previous campaign outcome, etc.

🛠 Tools & Technologies

- **Google Colab**   
- **Python**  
- **Pandas**  
- **NumPy**  
- **Scikit-learn**  
- **Matplotlib**  

📁 Files Included

decision_tree.ipynb 
bank.csv 
README.md


--📂 Dataset Information

The dataset contains customer details such as:

- `age`
- `job`
- `marital`
- `education`
- `balance`
- `housing`
- `loan`
- `contact`
- `duration`
- `campaign`
- `pdays`
- `previous`
- `poutcome`
- `y` (target variable: yes/no)

▶️ How to Run This Project in Google Colab

1. Open **Google Colab**:  
   https://colab.research.google.com

2. Upload the notebook:  
   **decision_tree.ipynb**

3. Upload the dataset:
   - In Colab → Left panel → Files → Upload → Select `bank.csv`

4. Run all cells in the notebook:
   - Runtime → Run all  

The notebook will:
- Load data  
- Encode categorical variables  
- Split data  
- Train Decision Tree  
- Evaluate accuracy  
- Display feature importance chart  

🧩 Code Summary

Key steps inside the Colab notebook:

1. **Load dataset**
2. **Label encode categorical columns**
3. **Split into train/test sets**
4. **Train Decision Tree Model**
5. **Evaluate using accuracy & classification report**
6. **Visualize feature importance**

📈 Model Results

The model outputs:

- **Accuracy score**
- **Precision, Recall, F1-score**
- **Feature importance ranking**
- **Bar plot of important features**

These metrics help understand how well the Decision Tree is making predictions.


📝 Important Notes (Google Colab Use)

- The entire project was executed in **Google Colab**, NOT VS Code.
- Files (`.ipynb`, `.csv`) were uploaded directly using Colab’s file system.
- After execution, project files were downloaded and pushed to GitHub manually:
  - GitHub → Add file → Upload files → Commit

🔮 Future Improvements

- Add hyperparameter tuning (GridSearchCV)
- Try Random Forest or XGBoost for better accuracy
- Build a Streamlit web application for deployment
- Add confusion matrix heatmap visualization

👨‍💻 Author

Project built for learning, practice, and portfolio enhancement using Google Colab and scikit-learn's Decision Tree Classifier.

📬 Contact

If you have any questions or would like to connect, feel free to reach out:

-LinkedIn:www.linkedin.com/in/munji-tanuja-0782552a5
-Email:tanuja6305@gmail.com  

