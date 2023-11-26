import streamlit as st

def main():
    st.title("Real Estate Analysis and Recommendation System for Gurgaon")

    st.markdown(
        """
        In this comprehensive project, we delve into the dynamic real estate landscape of Gurgaon, leveraging a multi-faceted approach that combines data-driven insights, predictive modeling, and personalized recommendations. The project is structured into three interlinked modules to provide users with a holistic experience:
        """
    )

    st.header("1. Price Predictor Module:")
    st.markdown(
        """
        Our robust price predictor module utilizes advanced regression models to forecast property prices in Gurgaon. By scraping and aggregating real-time data from diverse sources, we've trained a predictive model that takes into account various factors influencing property prices. Users can gain valuable insights into the estimated market value of properties based on specific features, empowering them to make informed decisions.
        """
    )

    st.header("2. Univariate and Bivariate Analysis Module:")
    st.markdown(
        """
        Understanding the market dynamics is pivotal in real estate decision-making. Our univariate and bivariate analysis module offers a visual exploration of key variables and their relationships. Through intuitive charts and graphs, users can explore trends, correlations, and outliers, providing a comprehensive understanding of the real estate landscape in Gurgaon. This analytical tool serves as a valuable resource for those seeking deeper insights into market trends.
        """
    )

    st.header("3. Recommendation System Module:")
    st.markdown(
        """
        Navigating through the multitude of available properties can be overwhelming. Our recommendation system simplifies this process by offering personalized suggestions based on user-defined criteria such as budget, preferences, and location. By employing sophisticated algorithms, the system identifies suitable properties and provides relevant insights, including proximity to amenities, schools, and transportation hubs. This module aims to streamline the property search process and enhance user satisfaction.
        """
    )

    st.subheader("How to Navigate:")
    st.markdown(
        """
        - **Homepage:** Start your exploration by accessing the homepage, where a concise overview of the project is provided.
        - **Price Predictor:** Dive into the price predictor module to estimate property prices and gain insights into the factors influencing them.
        - **Analysis:** Explore the univariate and bivariate analysis module to visualize market trends and correlations.
        - **Recommendations:** Head to the recommendation system to receive personalized property suggestions based on your preferences and budget.
        """
    )

if __name__ == "__main__":
    main()
