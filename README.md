# Attribute Manager for Maya
Description
This project provides a tool for managing custom attributes in Autodesk Maya. It allows users to easily add, modify, and remove attributes from selected objects, ensuring efficient workflow management in a Maya project. The tool is particularly useful for those who need to handle large scenes with multiple objects requiring custom attributes.

## Features
- Add Attributes: Create and add a new float attribute to selected objects with a default value of 1.0.
- Modify Attributes: Update the value of existing attributes on selected objects.
- Delete Attributes: Remove custom attributes from selected objects.
- Group Management: Automatically includes child objects when a parent group is selected.
- Clear Selection: Deselect objects and clear the attribute window with a single click.
- Space Conversion: Automatically converts spaces in attribute names to underscores.

## Installation
Download the Project: Clone or download the repository from GitHub.

`git clone https://github.com/SUNDAYROO/AttributeManager.git`

Place the Script: Copy AttributeM.py to a location accessible by Maya's Python environment.

Setup Environment: Ensure that Maya's Python environment is correctly configured to recognize the script path.

## Usage
[Video Guide](https://youtu.be/kGxRoVOZa58)
1. Launch Maya: Open Autodesk Maya and load your scene.
2. Execute the Script:
3. Open the Script Editor in Maya.
4. Load AttributeM.py into the Script Editor.
5. Run the script by selecting all and pressing the execute button (usually a "play" icon).
   
## Using the Tool
- Enter Attribute Name: Type the desired attribute name in the input field.
- Select Objects: Choose the objects to which you want to add the attribute.
- Add Attribute: Click the "Select" button to create the attribute.
- Modify or Delete Attribute: Enter the attribute name and click "Delete" to remove it.
- Clear Selection: Click the "Clear" button to deselect objects and clear the input window.

## Guide
Before running the script, please refer to the ReadMe.txt file included in the project for detailed instructions and troubleshooting tips.

This guide will help you understand the script's requirements and how to effectively utilize its features.
