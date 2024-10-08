# 📊 E-Commerce Dashboard

This project is an interactive E-Commerce Dashboard built with Streamlit. It provides insights into seller performance, payment methods, and daily orders. The dashboard allows users to filter data by date range and visualize key metrics.

**The datasets used in this project are available on Google Drive**
https://drive.google.com/drive/folders/1viUklHGljU8vwRoOVu_E1KBn53xsranq?usp=sharing

## Features

- **Daily Orders**: Visualize the total number of orders and revenue on a daily basis.
- **Seller Performance**: Analyze and rank sellers based on total sales volume and revenue.
- **Payment Methods Analysis**: Identify the preferred payment methods by buyers.
- **Filtered Data**: View the filtered dataset based on the selected date range.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/e-commerce-dashboard.git
    ```
2. Navigate to the project directory:
    ```bash
    cd e-commerce-dashboard
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Open the Jupyter Notebook:
    ```bash
    jupyter notebook notebook.ipynb
    ```
2. After running the necessary cells in the notebook, navigate to the `dashboard` folder:
    ```bash
    cd dashboard
    ```
3. Run the Streamlit app:
    ```bash
    streamlit run dashboard.py
    ```
4. Open your web browser and go to `http://localhost:8501` to view the dashboard.

## Files

- `dashboard/dashboard.py`: The main Streamlit application file.
- `dashboard/main_data.csv`: The main dataset used in the dashboard.
- `data/data_1.csv`: Additional dataset 1.
- `data/data_2.csv`: Additional dataset 2.
- `notebook.ipynb`: Jupyter Notebook for data analysis.
- `requirements.txt`: The list of dependencies required to run the app.
- `url.txt`: A file containing URLs related to the project.

## Screenshots

!image

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- Streamlit
- Seaborn
- Pandas
