# Apple Health Data Analytics Dashboard

This project consists of a Power BI dashboard and a Python script that work together to analyze and visualize personal health data sourced from Apple Health. The dashboard provides valuable insights into key health metrics like activity levels, heart rate and more, allowing users to track their wellness progress over time. The Python code prepares the data by extracting and organizing it, ensuring seamless integration with Power BI for effective analysis.

## Python Script Overview

The Python script extracts data from Apple Health's XML export format and processes it into structured CSV files for Power BI analysis. The main steps in the script are:

1. **Parsing the XML File**  
   Using Python’s `xml.etree.ElementTree` library, the script reads through the Apple Health XML data.

2. **Filtering Health Metrics**  
   The script filters and extracts over 40 health-related metrics, including steps, heart rate, active energy burned and more.

3. **Extracting Key Data**  
   For each health metric, the script captures relevant attributes such as `sourceName`, `creationDate`, `value` and `unit`.

4. **Exporting to CSV**  
   The script organizes the extracted data into CSV files for each health metric, making the data ready for analysis in Power BI.

## Report Overview

Below are the four main sections of the Power BI report, each providing insights into different aspects of health data:

### **1. Energy & Activity Overview**
![Energy & Activity Overview](https://github.com/Billal-Zughbi/Health-Report/blob/main/images/energyscreenshot.png)
This section visualizes metrics like active energy burned, exercise minutes, and flights climbed over time.

### **2. Cardiovascular Metrics**
![Cardiovascular Metrics](https://github.com/Billal-Zughbi/Health-Report/blob/87efba8d44f5fa414c86ced8c59b7d3941115e01/images/cardiovascularscreenshot.png)
This section focuses on heart health, displaying trends in resting heart rate, high heart rate events, and heart rate recovery.

### **3. Mobility & Movement**
![Mobility & Movement](https://github.com/Billal-Zughbi/Health-Report/blob/main/images/mobilityscreenshot.png)
This section highlights step count, walking asymmetry, and other mobility-related factors.

### **4. Physical & Environmental Factors**
![Physical & Environmental Factors](https://github.com/Billal-Zughbi/Health-Report/blob/main/images/physicalscreenshot.png)
This section explores environmental influences such as noise exposure and other external health indicators.

## Power BI Dashboard

The Power BI dashboard is designed to visualize the structured data created by the Python script. Key features of the dashboard include:

- **Activity Levels**: Visualizing data on active energy burned, exercise time and distance walked or run.
- **Heart Rate**: Displaying metrics such as resting heart rate, high heart rate events and heart rate recovery.
- **Other Health Metrics**: Step count, VO2 max and other health data.

The dashboard offers an interactive interface to monitor trends in health metrics, providing insights to help users make informed decisions about their fitness and wellness.

## Project Goals

The goal of this project is to create a tool that helps users track and visualize their personal health data from Apple Health. By leveraging Python for data extraction and Power BI for visualization, this project aims to provide actionable insights that users can use to monitor their wellness progress and make informed decisions about their health.

## Requirements

- Python 3.x
- Pandas
- Power BI Desktop
- Apple Health Data Export (XML)

## How to Use

1. **Extract Data from Apple Health**  
   Export your health data from the Apple Health app in XML format.

2. **Run the Python Script**  
   Run the Python script to parse the XML file and extract health metrics into CSV files.

3. **Load the Data into Power BI**  
   Import the generated CSV files into Power BI to visualize and analyze your health data.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

Feel free to modify or expand on this template depending on your needs.
