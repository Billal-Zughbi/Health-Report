import xml.etree.ElementTree as ET

# Specify the file name
file_name = "export.xml"

# Function to extract all unique record types
def extract_record_types(file_name):
    try:
        # Parse the XML file
        context = ET.iterparse(file_name, events=("start", "end"))

        record_types = set()  # Use a set to store unique record types

        # Iterate through the XML
        for event, elem in context:
            if event == "end" and elem.tag == "Record":
                record_type = elem.attrib.get("type")
                if record_type:
                    record_types.add(record_type)
                elem.clear()  # Clear element to save memory

        # Save the unique record types to a text file
        output_file = "record_types.txt"
        with open(output_file, "w") as file:
            for record_type in sorted(record_types):  # Sort alphabetically for readability
                file.write(record_type + "\n")

        print(f"Unique record types successfully saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")

# Extract and save the unique record types
extract_record_types(file_name)
