import xml.etree.ElementTree as ET
import pandas as pd

# Specify the file name

file_name = "export.xml"

# Function to parse the XML and extract data for specific types
def parse_xml_to_files(file_name, target_types):
    try:
        # Parse the XML file
        context = ET.iterparse(file_name, events=("start", "end"))

        # Create a dictionary to store rows for each type
        data_by_type = {record_type: [] for record_type in target_types}

        # Iterate through the XML
        for event, elem in context:
            if event == "end" and elem.tag == "Record":
                record_type = elem.attrib.get("type")
                if record_type in target_types:
                    # Extract relevant attributes
                    row = {
                        "sourceName": elem.attrib.get("sourceName"),
                        "creationDate": elem.attrib.get("creationDate"),
                        "startDate": elem.attrib.get("startDate"),
                        "endDate": elem.attrib.get("endDate"),
                        "value": elem.attrib.get("value"),
                        "unit": elem.attrib.get("unit"),
                    }
                    data_by_type[record_type].append(row)
                elem.clear()  # Clear element to save memory

        # Save each type's data to a separate CSV
        for record_type, rows in data_by_type.items():
            if rows:  # Only save if there is data
                df = pd.DataFrame(rows)
                output_file = f"{record_type}.csv"
                df.to_csv(output_file, index=False)
                print(f"Data for {record_type} successfully exported to {output_file}")

    except Exception as e:
        print(f"Error: {e}")

# Define the target types
target_types = [
    "HKCategoryTypeIdentifierAppleStandHour",
    "HKCategoryTypeIdentifierAudioExposureEvent",
    "HKCategoryTypeIdentifierHeadphoneAudioExposureEvent",
    "HKCategoryTypeIdentifierHighHeartRateEvent",
    "HKQuantityTypeIdentifierActiveEnergyBurned",
    "HKQuantityTypeIdentifierAppleExerciseTime",
    "HKQuantityTypeIdentifierAppleStandTime",
    "HKQuantityTypeIdentifierAppleWalkingSteadiness",
    "HKQuantityTypeIdentifierBasalEnergyBurned",
    "HKQuantityTypeIdentifierBodyMass",
    "HKQuantityTypeIdentifierDistanceCycling",
    "HKQuantityTypeIdentifierDistanceSwimming",
    "HKQuantityTypeIdentifierDistanceWalkingRunning",
    "HKQuantityTypeIdentifierEnvironmentalAudioExposure",
    "HKQuantityTypeIdentifierFlightsClimbed",
    "HKQuantityTypeIdentifierHeadphoneAudioExposure",
    "HKQuantityTypeIdentifierHeartRate",
    "HKQuantityTypeIdentifierHeartRateRecoveryOneMinute",
    "HKQuantityTypeIdentifierHeartRateVariabilitySDNN",
    "HKQuantityTypeIdentifierHeight",
    "HKQuantityTypeIdentifierPhysicalEffort",
    "HKQuantityTypeIdentifierRespiratoryRate",
    "HKQuantityTypeIdentifierRestingHeartRate",
    "HKQuantityTypeIdentifierRunningGroundContactTime",
    "HKQuantityTypeIdentifierRunningPower",
    "HKQuantityTypeIdentifierRunningSpeed",
    "HKQuantityTypeIdentifierRunningStrideLength",
    "HKQuantityTypeIdentifierRunningVerticalOscillation",
    "HKQuantityTypeIdentifierSixMinuteWalkTestDistance",
    "HKQuantityTypeIdentifierStairAscentSpeed",
    "HKQuantityTypeIdentifierStairDescentSpeed",
    "HKQuantityTypeIdentifierStepCount",
    "HKQuantityTypeIdentifierSwimmingStrokeCount",
    "HKQuantityTypeIdentifierTimeInDaylight",
    "HKQuantityTypeIdentifierVO2Max",
    "HKQuantityTypeIdentifierWalkingAsymmetryPercentage",
    "HKQuantityTypeIdentifierWalkingDoubleSupportPercentage",
    "HKQuantityTypeIdentifierWalkingHeartRateAverage",
    "HKQuantityTypeIdentifierWalkingSpeed",
    "HKQuantityTypeIdentifierWalkingStepLength"
]

# Parse the XML and create separate files for each type
parse_xml_to_files(file_name, target_types)
