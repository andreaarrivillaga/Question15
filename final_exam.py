import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
from datetime import datetime

st.title("Final Exam, Question 15")

# Load the dataset
@st.cache_data
def load_data():
  #df = pd.read_csv("/Users/andreaarrivillaga/Desktop/DSBA/visual analytics and analytical storytelling/FinalExam/athlete_events.csv.gz")
  url='https://drive.google.com/uc?id=' +"133D1c5gIVMSogmFb502Rmg34Uj_Q6pTg"
  st.write(f"trying new\n {url}")
  df=pd.read_csv(url)
  return df

df = load_data()



# Sidebar for selecting plot type
plot_type = st.sidebar.selectbox("Select Plot Type", ["Histogram", "Violin Plot", "Bar Plot", "Top 10 Athletes", "Line Plot", "Sport Distribution", "Scatter plot Height vs. Weight"])

# Generate plots based on selected type
if plot_type == "Histogram":
    # Histogram of athlete ages
    st.write("##### Distribution of Athlete Ages")
    fig, ax = plt.subplots()
    ax.hist(df["Age"].dropna(), bins=20, color='skyblue', edgecolor='black')
    ax.set_xlabel("Age")
    ax.set_ylabel("Frequency")
    ax.set_title("Distribution of Athlete Ages", ha='center')  # Center the title
    st.pyplot(fig)

elif plot_type == "Violin Plot":
    # Violin plot of athlete ages by sex
    st.write("##### Violin Plot of Athlete Ages by Gender")
    fig, ax = plt.subplots()
    sns.violinplot(data=df, x="Sex", y="Age", ax=ax)
    ax.set_xlabel("Gender")
    ax.set_ylabel("Age")
    ax.set_title("Violin Plot of Athlete Ages by Gender", ha='center')  # Center the title
    st.pyplot(fig)

elif plot_type == "Bar Plot":
    # Bar plot of count of medals won by each country
    st.write("##### Bar Plot of Count of Medals by the top 10 Countries")
    medal_counts = df[df["Medal"].isin(["Gold", "Silver", "Bronze"])].groupby("Team")["Medal"].count().nlargest(10)
    fig, ax = plt.subplots()
    medal_counts.plot(kind="bar", color='skyblue', edgecolor='black', ax=ax)
    ax.set_xlabel("Country")
    ax.set_ylabel("Number of Medals")
    ax.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
    ax.set_title("Bar Plot of Count of Medals by the top 10 Countries", ha='center')  # Center the title
    st.pyplot(fig)

elif plot_type == "Top 10 Athletes":
    # Horizontal bar plot of top 10 athletes based on number of Olympic events participated
    st.write("##### Top 10 Athletes by Number of Olympic Events Participated")
    top_athletes = df["Name"].value_counts().nlargest(10)
    top_athletes = top_athletes.sort_values(ascending=True)  # Sort in descending order
    fig, ax = plt.subplots()
    top_athletes.plot(kind="barh", color='skyblue', edgecolor='black', ax=ax)
    ax.set_xlabel("Number of Olympic Events")
    ax.set_ylabel("Athlete")
    ax.set_title("Top 10 Athletes by Number of Olympic Events Participated", ha='center')  # Center the title
    st.pyplot(fig)


    # Plot the line chart
elif plot_type == "Line Plot":
    # Line plot of athlete participation over the years with interactive slider widget
    st.write("##### Line Plot of Athlete Participation Over the Years")
    
    # Interactive slider widget for selecting the range of years
    min_year = df["Year"].min()
    max_year = df["Year"].max()
    year_range = st.slider("Select Year Range", min_year, max_year, (min_year, max_year))
    
    # Dropdown menu for selecting the season
    season_options = ["Summer", "Winter", "Both"]
    selected_season = st.selectbox("Select Season", season_options, index=2)  # Default to 'Both'
    
    # Plot the line chart based on the selected season(s)
    fig, ax = plt.subplots(figsize=(10, 6))
    max_athletes = 0  # Initialize maximum number of athletes
    
    if selected_season == "Both":
        for season in ["Summer", "Winter"]:
            # Filter data based on selected year range and season
            filtered_df = df[(df["Year"].between(year_range[0], year_range[1])) & (df["Season"] == season)]
            participation_over_years = filtered_df.groupby("Year")["ID"].nunique()
    
            # Plot the line for the current season
            if season == "Summer":
                participation_over_years.plot(kind="line", marker='o', linestyle='-', ax=ax, label=season, color='orange')
                title_season = "Both Seasons"
            elif season == "Winter":
                participation_over_years.plot(kind="line", marker='o', linestyle='-', ax=ax, label=season, color='blue')
        
            # Update max_athletes if necessary
            max_athletes = max(max_athletes, participation_over_years.max())
    else:
        # Filter data based on selected year range and season
        filtered_df = df[(df["Year"].between(year_range[0], year_range[1])) & (df["Season"] == selected_season)]
        participation_over_years = filtered_df.groupby("Year")["ID"].nunique()

        # Plot the line for the selected season
        participation_over_years.plot(kind="line", marker='o', linestyle='-', ax=ax, label=selected_season, color='orange' if selected_season == "Summer" else 'blue')
        title_season = selected_season
        
        # Update max_athletes
        max_athletes = participation_over_years.max()

    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Athletes")
    ax.set_xlim(year_range[0], year_range[1])  # Adjust x-axis limits
    
    # Set x-axis tick labels to every 10 years
    ax.set_xticks(range(year_range[0], year_range[1] + 1, 10))
    
    # Dynamically adjust y-axis limits
    ax.set_ylim(0, max_athletes * 1.1)  # Set y-axis limits based on max_athletes
    ax.grid(True, linestyle='--', alpha=0.5)  # Add gridlines
    
    # Add legend if both seasons are selected
    if selected_season == "Both":
        ax.legend()
    
    ax.set_title(f"Line Plot of Athlete Participation Over the Years ({title_season})", ha='center')  # Center the title
    st.pyplot(fig)

elif plot_type == "Sport Distribution":
    # Bar plot of count of athletes participating in each sport
    st.write("##### Top 10 Sports by Athlete Participation")
    st.write("This bar plot shows the count of athletes participating in each sport for the top 10 sports.")
    
    # Select top 10 sports
    top_sports = df["Sport"].value_counts().nlargest(10)
    
    # Create a color dictionary to map each sport to a color based on the season
    color_dict = {"Summer": "skyblue", "Winter": "lightgreen"}  # Define colors for Summer and Winter
    
    # Plot the bar chart for each sport
    fig, ax = plt.subplots(figsize=(10, 6))
    for sport in top_sports.index:
        # Get the color based on the season of the sport
        season_color = color_dict[df[df["Sport"] == sport]["Season"].iloc[0]]
        # Plot the bar for the sport
        ax.bar(sport, top_sports[sport], color=season_color, edgecolor='black')

    ax.set_xlabel("Sport")
    ax.set_ylabel("Number of Athletes")
    ax.tick_params(axis='x', rotation=45)  # Rotate x-axis labels by 45 degrees
    ax.set_title("Top 10 Sports by Athlete Participation", ha='center')  # Center the title
    
    # Add a legend for the season colors
    summer_patch = plt.Rectangle((0,0),1,1,fc="skyblue", edgecolor = 'none')
    winter_patch = plt.Rectangle((0,0),1,1,fc="lightgreen", edgecolor = 'none')
    ax.legend([summer_patch, winter_patch], ['Summer', 'Winter'], loc='upper right')

    st.pyplot(fig)


elif plot_type == "Scatter plot Height vs. Weight":
    # Downsample the data
    sampled_df = df.sample(n=min(500, len(df)))  # Downsampling to a maximum of 500 points

    # Adjust transparency based on the number of sampled points
    transparency = min(1, 500 / len(sampled_df))  # Initial transparency calculation
    transparency *= 0.5  # Adjust transparency further (multiply by 0.5 for decreased transparency)

    # Drop missing values from both 'Height' and 'Weight' columns
    sampled_df = sampled_df.dropna(subset=['Weight', 'Height'])

    # Scatter plot of Height vs. Weight
    st.write("##### Scatter Plot of Height vs. Weight (Sampled Data)")
    plt.figure(figsize=(8, 6))
    plt.scatter(sampled_df['Weight'], sampled_df['Height'], color='skyblue', alpha=transparency)
    plt.xlabel('Weight (kg)')
    plt.ylabel('Height (cm)')
    plt.title('Scatter Plot of Weight vs. Height')
    st.pyplot(plt)
