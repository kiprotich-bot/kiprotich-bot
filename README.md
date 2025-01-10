import pandas as pd
salary_data = pd.read_csv('salary_data.csv')
print(salary_data.head())
def get_employee_details(name):
    employee = salary_data[salary_data['Name'] == name]
    if not employee.empty:
        return employee.to_dict('records')[0]
    else:
        return "Employee not found."
salary_dict = salary_data.set_index('Name').to_dict('index')
print(salary_dict)`
def export_employee_details(name):
    employee = get_employee_details(name)
    if is instance(employee, dict):
        df = pd.DataFrame([employee])
        csv_filename = f"{name}_details.csv"
        df.to_csv(csv_filename, index=False)
        
        with zipfile.ZipFile('Employee_Profile.zip', 'w') as Zipf:
            Zipf.write(csv_filename)
        
        os.remove(csv_filename)
        return "Employee details exported and zipped successfully."
    else:
        return employee


R Script to unzip and display data\n",
    "\n",
    "```R\n",
    "# R Script for unzipping and displaying employee profile\n",
    "library(utils)\n",
    "\n",
    "# Unzip the file\n",
    "unzip(\"Employee Profile.zip\", ex dir = \"Employee Profile\")\n",
    "\n",
    "# Read and display the CSV\n",
    "employee_data <- read.csv(\"Employee Profile/John_Doe_profile.csv\")\n",
    "print(employee_data)\n",
    "```"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from zipfile import ZipFile
import os

def prepare_data(/Users/HPELITEBOOK/Desktop/Netflix_data.csv):
    """
    Unzip the dataset and load it into a DataFrame
    """
    if not os.path.exists('data'):
        os.makedirs('data')
    
    with ZipFile(/Users/HPELITEBOOK/Desktop/Netflix_data.csv, 'r') as zip_ref:
        zip_ref.extractall('data')
    
    df = pd.read_csv('data/netflix_data.csv')
    
    df.to_csv('data/Netflix_shows_movies.csv', index=False)
    return df

def clean_data(df):
    """
    Handle missing values in the dataset
    """
    print("Missing values before cleaning:")
    print(df.isnull().sum())
    df['director'].fillna('Unknown Director', inplace=True)
    df['cast'].fillna('Not Available', inplace=True)
    df['country'].fillna('Unknown', inplace=True)
    df['rating'].fillna('Not Rated', inplace=True)
    df['date_added'].fillna(df['date_added'].mode()[0], inplace=True)
    df['duration'] = df.groupby('type')['duration'].transform(
        lambda x: x.fillna(x.mode()[0]))
    
    print("\nMissing values after cleaning:")
    print(df.isnull().sum())
    return df

def explore_data(df):
    """
    Perform exploratory data analysis
    """
    print("\nDataset Overview:")
    print(df.info())
    print("\nNumerical Data Statistics:")
    print(df.describe())
    print("\nContent Type Distribution:")
    print(df['type'].value_counts())
    
    # Ratings distribution
    print("\nRatings Distribution:")
    print(df['rating'].value_counts())
    
    return df

def visualize_genres(df):
    """
    Create visualization for most watched genres
    """
    genres = df['listed_in'].str.split(',', expand=True).stack()
    genre_counts = genres.str.strip().value_counts().head(10)
    plt.figure(figsize=(12, 6))
    sns.barplot(x=genre_counts.values, y=genre_counts.index, palette='viridis')
    plt.title('Top 10 Netflix Genres', pad=20, fontsize=14)
    plt.xlabel('Number of Titles', fontsize=12)
    plt.ylabel('Genre', fontsize=12)
    plt.tight_layout()
    plt.savefig('visualizations/genre_distribution.png')
    plt.close()

def visualize_ratings(df):
    """
    Create visualization for ratings distribution
    """
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='rating', order=df['rating'].value_counts().index, 
                 palette='Set2')
    plt.title('Distribution of Netflix Content Ratings', pad=20, fontsize=14)
    plt.xticks(rotation=45)
    plt.xlabel('Rating', fontsize=12)
    plt.ylabel('Number of Titles', fontsize=12)
    plt.tight_layout()
    plt.savefig('visualizations/ratings_distribution.png')
    plt.close()

def main():
    if not os.path.exists('visualizations'):
        os.makedirs('visualizations')
    df = prepare_data('netflix_data.zip')
    df = clean_data(df)
    df = explore_data(df)
    visualize_genres(df)
    visualize_ratings(df)
    df.to_csv('data/Netflix_shows_movies_cleaned.csv', index=False)



