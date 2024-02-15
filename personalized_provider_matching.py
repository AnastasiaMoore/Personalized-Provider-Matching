import streamlit as st

# Create tabs
tab1, tab2 = st.tabs(["App", "About This App"])

# Content for the "App" tab
with tab1:
    st.title('Personalized Provider Matching')

    # Problem Statement
    st.header('Problem Statement')
    st.write('Healthcare systems struggle to evaluate and rank providers effectively, which hinders patients from identifying top-performing doctors who offer the best patient outcomes and satisfaction at lower costs.')

    # Solution
    st.header('Solution')
    st.write('Our app provides data-driven insights to evaluate healthcare providers, helping patients find quality care that is also cost-effective.')

# Content for the "About This App" tab
with tab2:
    st.title('Personalized Provider Matching')

    # Dataset Description
    st.header('Dataset Description')
    st.write('The data includes key performance indicators like treatment success rates, patient satisfaction, and cost metrics. This information powers our recommendation engine.')

    # Running Instructions
    st.header('Instructions')
    st.write('This is a prototype. To interact with the full features, please visit our official website when it is live.')

    # Footer
    st.write('Thank you for your interest in Healthcare Provider Insight. For further inquiries, contact info@healthcareinsight.com.')
