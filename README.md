# 🎯 **Company-wise LeetCode Practice App**

🚀 A **Streamlit-powered** web application designed to help you **prepare for coding interviews** by practicing LeetCode questions based on the **company** you're targeting! Whether you're preparing for **Amazon**, **Google**, or any other company, this app offers an easy way to filter coding questions by **difficulty** and **time period**.

## 💡 Features

- **Select Companies**: Choose from a list of companies like Amazon, Google, Microsoft, etc.
- **Filter by Time Period**: Filter coding questions by time periods such as **30 days**, **60 days**, or **all-time**.
- **Difficulty Level**: Sort questions based on difficulty - **Easy**, **Medium**, or **Hard**.
- **Most Asked Questions**: See the **Top 10 Most Frequently Asked Questions** for each company.
- **Interactive UI**: A **beautiful, interactive** user interface powered by **Streamlit**.

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: Python
- **Data Science Libraries**: 
  - [Pandas](https://pandas.pydata.org/) for data manipulation
  - [Matplotlib](https://matplotlib.org/) for data visualization
  - [Seaborn](https://seaborn.pydata.org/) for beautiful plots
- **Data Source**: CSV files containing LeetCode questions and their metadata

## 🚀 How to Get Started

Follow these steps to set up and run the app on your local machine:

### Prerequisites

1. **Python 3.7+**
2. **pip** (Python package installer)

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ABaditya07/company-wise-leetcode-practice-app.git
   cd company-wise-leetcode-practice-app


📂 Project Structure   
bash    
Copy   
Edit   
company-wise-leetcode-practice-app/
│
├── app.py                # Main Streamlit application file
├── requirements.txt      # List of Python dependencies
├── companies/            # Folder with subfolders for each company
│   ├── Amazon/
│   │   ├── 30_days.csv  # CSV with questions from Amazon over the last 30 days
│   ├── Google/
│   └── ...
└── README.md             # This file
Files in the Repository:
app.py: The main Streamlit script where the app logic resides.

companies/: Folder containing subfolders for each company with their respective LeetCode question CSV files.

requirements.txt: All the libraries required to run the app.

🌟 How to Use the App
Select Company: Choose your targeted company (Amazon, Google, etc.) from the sidebar.

Choose Time Period: Select the time period (e.g., 30 days, 60 days, all-time) for the coding questions.

Set Difficulty Level: Filter questions by difficulty - Easy, Medium, or Hard.

Browse Questions: View and explore questions for the selected company.

Top 10 Questions: Get a visual representation of the Top 10 Most Asked Questions based on frequency.

📊 Top 10 Most Asked Questions
The app also displays a bar chart showing the top 10 most frequently asked LeetCode questions for your selected company. The questions are ranked based on frequency, allowing you to focus on the ones that matter most.

🤝 Contributing
We welcome contributions to improve this project! You can help by:

Adding more companies and their LeetCode questions.

Enhancing the app’s functionality (e.g., more filters or features).

Improving the user interface for better user experience.

Steps to Contribute:
Fork the repository.

Create a new branch:

bash
Copy
Edit
git checkout -b feature-branch
Make your changes.

Commit your changes:

bash
Copy
Edit
git commit -am 'Add new feature or fix'
Push your changes:

bash
Copy
Edit
git push origin feature-branch
Create a pull request.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgements
A huge thank you to the following:

Streamlit: For providing an amazing framework to build interactive web apps.

Pandas: For its powerful data manipulation capabilities.

Matplotlib & Seaborn: For creating the stunning visualizations that help us understand the data better.

LeetCode: For providing a rich set of coding problems to prepare for interviews.

🚨 Disclaimer
This app relies on CSV files containing LeetCode questions and their respective metadata. The accuracy and frequency of the questions depend on the data available from the CSV files.

👨‍💻 Happy Coding and Best of Luck with your interviews! ✨

Follow me on GitHub

vbnet
Copy
Edit

---

### Key Features of This README:

1. **Project Name & Introduction**: The project name is emphasized at the top with icons and a catchy description.
2. **Features**: The features of the project are highlighted in an easy-to-read bulleted format with emojis to make it visually engaging.
3. **Tech Stack**: The tech stack section is clean and uses relevant links for easy access to further documentation.
4. **Installation Steps**: Clear and easy-to-follow installation steps with commands formatted for different OS environments (Windows/macOS).
5. **How to Use**: This section is simplified and emphasizes the easy-to-use functionality of the app with the added benefit of the **Top 10 Most Asked Questions** feature.
6. **Contributing**: This section encourages open collaboration and gives clear steps for how to contribute to the project.
7. **Acknowledgements**: A section recognizing the tools and platforms used, with links to their documentation.
8. **License**: Clear and simple license information (MIT License).
9. **Disclaimer**: A brief note on how the app relies on data from the CSV files.

This README is designed to not only inform but also engage potential users and contributors with a
