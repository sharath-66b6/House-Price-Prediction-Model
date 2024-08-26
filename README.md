
# House Price Prediction Model

## Overview
This project involves building a machine learning model to predict house prices based on various features. The model is developed using Python and various machine learning libraries, and it is deployed using Streamlit for an interactive web interface.

## Project Structure
The repository contains the following files:

- **House_price_predict.ipynb**: Jupyter notebook containing the code for data exploration, preprocessing, model training, and evaluation.
- **README.md**: Documentation for the project.
- **app.py**: The Streamlit application that serves the model and allows users to interact with it through a web interface.
- **house_price_model.pkl**: Serialized machine learning model saved using Joblib, ready to be loaded and used for predictions.
- **requirements.txt**: A list of Python dependencies required to run the project.
- **train.csv**: The dataset used for training the model.
- **updated_file.csv**: A cleaned or preprocessed version of the dataset.

## Dependencies
Make sure you have the required dependencies installed. You can install them using the following command:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Data
The \`train.csv\` file contains the data used for training the model. It includes features such as the number of rooms, square footage, location, etc., and the target variable is the price of the house.

The \`updated_file.csv\` file is a cleaned version of the original dataset, ready for training and evaluation.

## Model Training
The model training process is documented in the \`House_price_predict.ipynb\` notebook. This notebook includes:

1. **Data Exploration**: Understanding the data through visualizations and statistical analysis.
2. **Data Preprocessing**: Handling missing values, feature engineering, and data transformation.
3. **Model Building**: Training the machine learning model using scikit-learn.
4. **Model Evaluation**: Assessing the model's performance using various metrics.

## Running the App
To run the Streamlit app, use the following command:

\`\`\`bash
streamlit run app.py
\`\`\`

This will launch a web interface where you can input various features of a house, and the model will predict the price.

## Model Deployment
The model is deployed using Streamlit, making it accessible through a simple web interface. The app allows users to input new data and get predictions based on the trained model.

## Conclusion
This project demonstrates the process of building, evaluating, and deploying a machine learning model for house price prediction. It covers the entire workflow from data exploration to model deployment, making it a comprehensive example of a real-world ML project.

## Author
**Sharath Kumar Reddy** - AI/ML Engineer and Frontend Web Developer
 