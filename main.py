import streamlit as st
import plotly.express as px
import pandas as pd


def main():
    # Set page config.
    st.set_page_config(page_title='INST 490 Capstone Project',
                       page_icon='💡')

    # Print title.
    st.title(body='💡 INST 490 Capstone Project')

    # Print team member names.
    st.write('Mohamed Nabeel, Grant Buttrey, Jiin Kim, Mahad Abdi, Matthew Makonnen, Fabrice Tedonjeu')

    # Summary header.
    st.header(body='Summary')

    # The summary.
    st.write('Our capstone project is to provide an energy data analysis report that details the current energy '
             'status of DMV region, in regards to energy consumption and cost, while also providing methods and '
             'policies states within the region can implement to improve energy efficiency.')

    # Choose dataset header.
    st.header(body='Choose Dataset', anchor='choose-dataset')

    # Select box to choose dataset.
    visualization = st.selectbox(label='Select a dataset:',
                                 options=('Energy Consumption', 'Energy Usage Price'))

    # Table of contents.
    st.header(body='Table of Contents')

    # The contents.
    contents = '- [Summary](#summary)\n' \
               '- [Choose Dataset](#choose-dataset)\n'

    # If dataset is energy consumption.
    if visualization == 'Energy Consumption':
        contents += '- [Data Visualization](#data-visualization)\n' \
                    '  - [Choropleth Map](#choropleth-map)\n' \
                    '  - [Line Plot](#line-plot)\n' \
                    '- [Machine Learning](#machine-learning)\n' \
                    '  - [Equation](#equation)\n' \
                    '  - [Prediction](#prediction)'

    st.markdown(body=contents, unsafe_allow_html=True)

    # Header for Data Visualization.
    st.header(body='Data Visualization')

    if visualization == 'Energy Consumption':
        # Set subheader.
        st.subheader(body='Total Energy Consumption Estimates by End-Use Sector')

        # Write description.
        st.write('Comprehensive state-level estimates of energy production, consumption, prices, and expenditures by '
                 'source and sector.')

        # Subheader for choropleth map.
        st.subheader('Choropleth Map')

        # Set 2 columns for the options.
        col1, col2 = st.columns(2)

        with col1:
            # Select box to choose sector.
            sector = st.selectbox(label='Select a sector:',
                                  options=('Total Consumption', 'Residential Sector', 'Commercial Sector',
                                           'Industrial Sector', 'Transportation Sector'),
                                  key='sector1')
        with col2:
            # Year slider.
            year = st.slider(label='Select a year:',
                             min_value=1960,
                             max_value=2019,
                             key='slider1')

        # Read total energy consumption data.
        df = pd.read_excel(io=r'use_tot_sector.xlsx',
                           sheet_name=sector,
                           header=2)

        # Drop first row.
        df.drop(index=df.index[0],
                axis=0,
                inplace=True)

        # Drop last row.
        df.drop(index=df.index[-1],
                axis=0,
                inplace=True)

        # Create figure.
        fig = px.choropleth(data_frame=df,
                            locations='State',
                            locationmode='USA-states',
                            color=year,
                            scope='usa',
                            title=f'Total Energy Consumption Estimates U.S. {sector} {year}',
                            labels={f'{year}': 'Billion Btu'})

        # Print choropleth map figure to page.
        st.write(fig)

        # Print DataFrame.
        file_container = st.expander(label=f'Click to display Total Energy Consumption U.S. {sector} {year} Data')
        file_container.write(df)

        # Save raw data button to save DataFrame as CSV file.
        st.download_button(label='Press to Download Raw Data',
                           data=df.to_csv(),
                           file_name=f'{sector}.csv',
                           mime='text/csv',
                           key='download-csv1')

        # Set 2 columns for the options.
        col1, col2 = st.columns(2)

        with col1:
            # Select box to choose sector.
            sector = st.selectbox(label='Select a sector:',
                                  options=('Total Consumption', 'Residential Sector', 'Commercial Sector',
                                           'Industrial Sector', 'Transportation Sector'),
                                  key='sector2')
        with col2:
            # Year slider.
            year = st.slider(label='Select a year:',
                             min_value=1960,
                             max_value=2019,
                             key='slider2')

        # Read total energy consumption data.
        df = pd.read_excel(io=r'use_tot_sector.xlsx',
                           sheet_name=sector,
                           header=2)

        # Drop first row.
        df.drop(index=df.index[0],
                axis=0,
                inplace=True)

        # Drop last row.
        df.drop(index=df.index[-1],
                axis=0,
                inplace=True)

        # Drops states except DMV.
        dmv_df = df[df['State'].isin(['DC', 'MD', 'VA'])]

        # Create choropleth map figure.
        fig = px.choropleth(data_frame=dmv_df,
                            locations='State',
                            locationmode='USA-states',
                            color=year,
                            scope='usa',
                            title=f'Total Energy Consumption Estimates DMV {sector} {year}',
                            labels={f'{year}': 'Billion Btu'})

        fig.update_geos(fitbounds='locations')

        # Print choropleth map figure to page.
        st.write(fig)

        # Print DataFrame.
        file_container = st.expander(label=f'Click to display Total Energy Consumption DMV {sector} {year} Data')
        file_container.write(df)

        # Save raw data button to save DataFrame as CSV file.
        st.download_button(label='Press to Download Raw Data',
                           data=df.to_csv(),
                           file_name=f'{sector}.csv',
                           mime='text/csv',
                           key='download-csv2')

        # Subheader for line plot.
        st.subheader('Line Plot', anchor='line-plot')

        # Set 2 columns for the options.
        col1, col2 = st.columns(2)

        with col1:
            # Select box to choose sector.
            sector = st.selectbox(label='Select a sector:',
                                  options=('Total Consumption', 'Residential Sector', 'Commercial Sector',
                                           'Industrial Sector', 'Transportation Sector'),
                                  key='sector3')
        with col2:
            # Slider for year range.
            years = st.slider(label='Select a year range:',
                              min_value=1960,
                              max_value=2019,
                              value=(1960, 2019),
                              key='range1')

        # Read total energy consumption data.
        df = pd.read_excel(io=r'use_tot_sector.xlsx',
                           sheet_name=sector,
                           header=2)

        # Drop first row.
        df.drop(index=df.index[0],
                axis=0,
                inplace=True)

        # Drop last row.
        df.drop(index=df.index[-1],
                axis=0,
                inplace=True)

        # Drops states except DMV.
        dmv_df = df[df['State'].isin(['DC', 'MD', 'VA'])]

        # Make years a column for plotting.
        dmv_df = pd.melt(dmv_df, id_vars=['State'], var_name='Year')

        # Filter between year range.
        dmv_df = dmv_df[dmv_df['Year'] >= years[0]]
        dmv_df = dmv_df[dmv_df['Year'] <= years[1]]

        # Create line plot figure.
        fig = px.line(data_frame=dmv_df,
                      x='Year',
                      y='value',
                      color='State',
                      title=f'Total Energy Consumption Estimates DMV {sector} {years[0]}-{years[1]}',
                      labels={'value': 'Energy Consumption (Billion Btu)'})

        # Print line plot figure to page.
        st.write(fig)

        # Print DataFrame.
        file_container = st.expander(label=f'Click to display Total Energy Consumption DMV {sector} '
                                           f'{years[0]}-{years[1]} Data')
        file_container.write(dmv_df)

        # Save raw data button to save DataFrame as CSV file.
        st.download_button(label='Press to Download Raw Data',
                           data=dmv_df.to_csv(),
                           file_name=f'{sector}.csv',
                           mime='text/csv',
                           key='download-csv3')

        # Header for machine learning.
        st.header(body='Machine Learning', anchor='machine-learning')

        # Subheader for linear regression model.
        st.subheader(body='Scatter Plot with Linear Regression Model', anchor='linear-regression-model')

        # Set 2 columns for the options.
        col1, col2, col3 = st.columns(3)

        with col1:
            # Select box to choose state.
            state = st.selectbox(label='Select a state:',
                                 options=('US', 'DC', 'MD', 'VA'))

        with col2:
            # Select box to choose sector.
            sector = st.selectbox(label='Select a sector:',
                                  options=('Total Consumption', 'Residential Sector', 'Commercial Sector',
                                           'Industrial Sector', 'Transportation Sector'),
                                  key='sector4')

        with col3:
            # Slider for year range.
            years = st.slider(label='Select a year range:',
                              min_value=1960,
                              max_value=2019,
                              value=(1960, 2019),
                              key='range2')

        # Read total energy consumption data.
        scatter_df = pd.read_excel(io=r'use_tot_sector.xlsx',
                                   sheet_name=sector,
                                   header=2)

        # Drop first row.
        scatter_df.drop(index=df.index[0],
                        axis=0,
                        inplace=True)

        # Drop other states.
        scatter_df = scatter_df[scatter_df['State'].isin(['DC', 'MD', 'VA', 'US'])]
        scatter_df = scatter_df[scatter_df['State'] == state]

        # Make years a column for plotting.
        scatter_df = pd.melt(scatter_df, id_vars=['State'], var_name='Year')

        # Filter between year range.
        scatter_df = scatter_df[scatter_df['Year'] >= years[0]]
        scatter_df = scatter_df[scatter_df['Year'] <= years[1]]

        # Create scatter plot figure.
        fig = px.scatter(data_frame=scatter_df,
                         x='Year',
                         y='value',
                         color='State',
                         title=f'Total Energy Consumption Estimates {state} {sector} {years[0]}-{years[1]}',
                         labels={'value': 'Energy Consumption (Billion Btu)'},
                         trendline='ols',
                         trendline_color_override='red')

        # Print scatter plot figure to page.
        st.write(fig)

        # Get OLS results.
        results = px.get_trendline_results(fig)

        # Print summary.
        file_container = st.expander(label='Click to display Model Parameters')
        file_container.write(results.px_fit_results.iloc[0].summary())

        # Print DataFrame.
        file_container = st.expander(label=f'Click to display Total Energy Consumption {state} {sector} '
                                           f'{years[0]}-{years[1]} Data')
        file_container.write(scatter_df)

        # Save raw data button to save DataFrame as CSV file.
        st.download_button(label='Press to Download Raw Data',
                           data=dmv_df.to_csv(),
                           file_name=f'{sector}.csv',
                           mime='text/csv',
                           key='download-csv4')

        # Get coefficients.
        b = results.iloc[0]['px_fit_results'].params[0]
        m = results.iloc[0]['px_fit_results'].params[1]

        # Print subheader.
        st.subheader(body='Equation')

        # Print equation.
        st.write(state, ' ', sector, ' ', years[0], '-', years[1])
        st.write('y = ', m, 'x + ', b)

        # Print subheader for prediction.
        st.subheader(body='Prediction', anchor='prediction')

        year = st.number_input(label='Enter a year:',
                               value=2022,
                               format='%d')

        # Print explanation.
        st.write('Using Ordinary Least Squares (OLS) linear regression model, we predict that ', state, ' ', sector,
                 ' will consume ', (m * year + b), ' billion Btu of energy in the ', sector, ' for ', year, '.')

    # Print header for data analysis.
    st.header(body='Data Analysis')

    # Print analysis.
    st.write('TODO')

    # Print header for Insights and Recommendations.
    st.header(body='Insights and Recommendations')

    # Print analysis.
    st.write('TODO')


if __name__ == '__main__':
    main()
