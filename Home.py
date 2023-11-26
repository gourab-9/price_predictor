import streamlit as st

st.set_page_config(
    page_title="Gurgaon Real Estate Analytics App",
    page_icon="🏠",
)
st.title('🏠🏡👨‍👩‍👧‍👦🏢🛏🛁📈📉🏦🏚️🤝🔑')
st.write("# Welcome to Real Estate Project of Gurgaon 👋🤗🎉💗Welcome")

st.sidebar.success("Select a demo above.")



def main():
    st.title("Your Dream Home: A Revolutionary Real Estate Experience")

    st.markdown(
        """
        Welcome to "Your Dream Home," a cutting-edge real estate project designed to redefine your property search journey. We've seamlessly blended advanced technology, data-driven insights, and personalized recommendations to create an unparalleled experience tailored just for you.
        """
    )

    st.subheader("Why 'Your Dream Home'?")
    st.markdown(
        """
        Discover the future of real estate exploration where innovation meets intuition. Here's what sets us apart:
        """
    )

    st.markdown("1. **Intelligent Predictions with Price Precision:**")
    st.markdown(
        """
        Unleash the power of our state-of-the-art price predictor module. We've harnessed advanced regression models to forecast property prices in your desired location, ensuring you're always one step ahead in making informed decisions. Say goodbye to guesswork; say hello to precision.
        """
    )

    st.markdown("2. **Visualize Your Investment with Unparalleled Analysis:**")
    st.markdown(
        """
        Dive deep into the heart of the market with our univariate and bivariate analysis module. Stunning visuals and interactive charts reveal market trends, correlations, and outliers, empowering you with a comprehensive understanding of the real estate landscape. Knowledge is your superpower.
        """
    )

    st.markdown("3. **Tailored Recommendations, Your Way:**")
    st.markdown(
        """
        Navigate through the sea of available properties effortlessly with our recommendation system module. Imagine a personalized guide that considers your budget, preferences, and location – delivering not just a property, but a home. Our sophisticated algorithms ensure you find your perfect match.
        """
    )

    st.subheader("Embark on Your Real Estate Journey:")
    st.markdown(
        """
        - **Homepage:**
            - A gateway to your dream home. The homepage provides a glimpse into the project's capabilities, setting the stage for an immersive experience.
        - **Price Predictor:**
            - Take control of your investment strategy. Explore estimated property prices and gain valuable insights into the factors shaping the market.
        - **Analysis:**
            - Uncover the secrets of the market. Visualize trends, correlations, and outliers through interactive charts that transform complex data into actionable insights.
        - **Recommendations:**
            - Let us be your guide. Receive tailor-made property suggestions that align with your unique preferences and budget. It's more than a recommendation; it's a roadmap to your future home.
        """
    )

    st.subheader("Why Wait? Your Dream Home Awaits:")
    st.markdown(
        """
        Imagine a real estate journey where every step is guided by intelligence, fueled by insights, and tailored to your aspirations. "Your Dream Home" isn't just a project; it's a promise – a promise to transform your property search into a seamless, enjoyable experience.

        Embark on this exciting adventure with us. Your dream home is not just a possibility; it's a certainty. Welcome to a new era of real estate exploration. Welcome home.
        """
    )

if __name__ == "__main__":
    main()


