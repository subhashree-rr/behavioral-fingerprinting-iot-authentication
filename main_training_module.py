import pandas as pd
import numpy as np
import joblib

from pathlib import Path

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)


# ============================================================
# PROJECT CONFIGURATION
# ============================================================

DATASET_FILE = "wifi_security_dataset.csv"

MODEL_FILE = "wifi_security_decision_tree.pkl"

HEADER_FILE = "wifi_security_model.h"

RESULT_FILE = "model_results.csv"


# ============================================================
# FEATURE NAMES
#
# IMPORTANT:
# The feature order must remain exactly the same during:
#
# Dataset Training
# Python Prediction
# ESP32 Prediction
# ============================================================

FEATURES = [

    "RSSI",

    "Avg_RSSI",

    "RSSI_Variation",

    "WiFi_Channel",

    "Packet_Count",

    "Packet_Rate",

    "Avg_Packet_Size",

    "Max_Packet_Size",

    "Data_Rate",

    "Inter_Arrival_Time",

    "Connection_Attempts",

    "Auth_Failures",

    "Invalid_Commands",

    "Repeated_Requests",

    "Command_Frequency"

]


TARGET = "Label"


# ============================================================
# DISPLAY PROJECT HEADER
# ============================================================

print("\n")

print("====================================================")

print("     ESP32 TINYML WI-FI SECURITY SYSTEM")

print("     COMPLETE TRAINING + ESP32 CONVERTER")

print("====================================================")


# ============================================================
# STEP 1: CHECK DATASET
# ============================================================

print("\n[STEP 1] CHECKING DATASET")


if not Path(DATASET_FILE).exists():

    print("\nERROR!")

    print("Dataset file not found.")

    print("Expected File:")

    print(DATASET_FILE)

    print("\nPlease place the CSV file in the same folder.")

    exit()


print("Dataset File Found Successfully!")


# ============================================================
# STEP 2: LOAD DATASET
# ============================================================

print("\n[STEP 2] LOADING DATASET")


dataset = pd.read_csv(

    DATASET_FILE

)


print("Dataset Loaded Successfully!")


print("\nDataset Shape:")

print(dataset.shape)


# ============================================================
# STEP 3: DISPLAY DATASET INFORMATION
# ============================================================

print("\n[STEP 3] DATASET INFORMATION")


print("\nDataset Columns:")


for column in dataset.columns:

    print(" -", column)


print("\nFirst 5 Samples:")


print(dataset.head())


print("\nMissing Values:")


print(dataset.isnull().sum())


# ============================================================
# STEP 4: VALIDATE REQUIRED COLUMNS
# ============================================================

print("\n[STEP 4] VALIDATING DATASET")


required_columns = FEATURES + [TARGET]


missing_columns = []


for column in required_columns:

    if column not in dataset.columns:

        missing_columns.append(

            column

        )


if len(missing_columns) > 0:

    print("\nERROR!")

    print("The following required columns are missing:")


    for column in missing_columns:

        print(" -", column)


    exit()


print("All Required Columns Found!")


# ============================================================
# STEP 5: REMOVE MISSING VALUES
# ============================================================

print("\n[STEP 5] CLEANING DATASET")


original_size = len(

    dataset

)


dataset = dataset.dropna()


new_size = len(

    dataset

)


removed_rows = (

    original_size

    - new_size

)


print("Original Samples:", original_size)

print("Samples After Cleaning:", new_size)

print("Removed Samples:", removed_rows)


# ============================================================
# STEP 6: CLASS DISTRIBUTION
# ============================================================

print("\n[STEP 6] CLASS DISTRIBUTION")


class_distribution = dataset[

    TARGET

].value_counts()


print(class_distribution)


print("\nLabel Information:")

print("0 = NORMAL")

print("1 = SUSPICIOUS")


# ============================================================
# STEP 7: PREPARE FEATURES AND LABEL
# ============================================================

print("\n[STEP 7] PREPARING MACHINE LEARNING DATA")


X = dataset[

    FEATURES

]


y = dataset[

    TARGET

]


print("Total Features:", len(FEATURES))

print("Total Samples:", len(dataset))


# ============================================================
# STEP 8: TRAIN TEST SPLIT
# ============================================================

print("\n[STEP 8] SPLITTING TRAINING AND TESTING DATA")


X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42,

    stratify=y

)


print("Training Samples:", len(X_train))

print("Testing Samples :", len(X_test))


# ============================================================
# STEP 9: CREATE DECISION TREE MODEL
# ============================================================

print("\n[STEP 9] CREATING DECISION TREE MODEL")


model = DecisionTreeClassifier(

    max_depth=6,

    min_samples_split=5,

    random_state=42

)


print("Decision Tree Model Created!")


# ============================================================
# STEP 10: TRAIN MODEL
# ============================================================

print("\n[STEP 10] TRAINING MODEL")


model.fit(

    X_train,

    y_train

)


print("Model Training Completed Successfully!")


# ============================================================
# STEP 11: TEST MODEL
# ============================================================

print("\n[STEP 11] TESTING MODEL")


prediction = model.predict(

    X_test

)


print("Prediction Completed!")


# ============================================================
# STEP 12: CALCULATE PERFORMANCE
# ============================================================

print("\n[STEP 12] CALCULATING MODEL PERFORMANCE")


accuracy = accuracy_score(

    y_test,

    prediction

)


precision = precision_score(

    y_test,

    prediction,

    zero_division=0

)


recall = recall_score(

    y_test,

    prediction,

    zero_division=0

)


f1 = f1_score(

    y_test,

    prediction,

    zero_division=0

)


print("\n====================================================")

print("MODEL PERFORMANCE RESULTS")

print("====================================================")


print("Accuracy  :", round(accuracy * 100, 2), "%")

print("Precision :", round(precision * 100, 2), "%")

print("Recall    :", round(recall * 100, 2), "%")

print("F1 Score  :", round(f1 * 100, 2), "%")


# ============================================================
# STEP 13: CLASSIFICATION REPORT
# ============================================================

print("\n[STEP 13] CLASSIFICATION REPORT")


print(

    classification_report(

        y_test,

        prediction,

        target_names=[

            "NORMAL",

            "SUSPICIOUS"

        ],

        zero_division=0

    )

)


# ============================================================
# STEP 14: CONFUSION MATRIX
# ============================================================

print("\n[STEP 14] CONFUSION MATRIX")


cm = confusion_matrix(

    y_test,

    prediction

)


print(cm)


# ============================================================
# STEP 15: SAVE MODEL AS PKL
# ============================================================

print("\n[STEP 15] SAVING TRAINED MODEL")


joblib.dump(

    model,

    MODEL_FILE

)


print("PKL Model Saved Successfully!")

print("File:", MODEL_FILE)


# ============================================================
# STEP 16: SAVE MODEL RESULTS
# ============================================================

print("\n[STEP 16] SAVING MODEL RESULTS")


results = pd.DataFrame({

    "Model": [

        "Decision Tree"

    ],

    "Accuracy": [

        accuracy

    ],

    "Precision": [

        precision

    ],

    "Recall": [

        recall

    ],

    "F1_Score": [

        f1

    ]

})


results.to_csv(

    RESULT_FILE,

    index=False

)


print("Results Saved Successfully!")

print("File:", RESULT_FILE)


# ============================================================
# STEP 17: GET DECISION TREE STRUCTURE
# ============================================================

print("\n[STEP 17] PREPARING MODEL FOR ESP32 CONVERSION")


tree = model.tree_


children_left = tree.children_left

children_right = tree.children_right

feature_index = tree.feature

threshold = tree.threshold

tree_values = tree.value


print("Decision Tree Structure Loaded!")


# ============================================================
# FUNCTION:
# GET PREDICTED CLASS AT LEAF NODE
# ============================================================

def get_leaf_class(node_id):


    class_counts = tree_values[

        node_id

    ][0]


    predicted_class = int(

        np.argmax(

            class_counts

        )

    )


    return predicted_class


# ============================================================
# FUNCTION:
# GENERATE ESP32 C++ IF-ELSE CODE
# ============================================================

def generate_tree_code(

    node_id,

    depth=1

):


    indent = "    " * depth


    # ========================================================
    # LEAF NODE
    # ========================================================

    if (

        children_left[node_id]

        ==

        children_right[node_id]

    ):


        predicted_class = get_leaf_class(

            node_id

        )


        return (

            indent

            + "return "

            + str(

                predicted_class

            )

            + ";\n"

        )


    # ========================================================
    # DECISION NODE
    # ========================================================

    current_feature_index = feature_index[

        node_id

    ]


    current_feature_name = FEATURES[

        current_feature_index

    ]


    current_threshold = threshold[

        node_id

    ]


    code = ""


    # ========================================================
    # IF CONDITION
    # ========================================================

    code += (

        indent

        + "if ("

        + current_feature_name

        + " <= "

        + f"{current_threshold:.6f}"

        + "f)\n"

    )


    code += (

        indent

        + "{\n"

    )


    # LEFT TREE

    code += generate_tree_code(

        children_left[

            node_id

        ],

        depth + 1

    )


    code += (

        indent

        + "}\n"

    )


    # ========================================================
    # ELSE CONDITION
    # ========================================================

    code += (

        indent

        + "else\n"

    )


    code += (

        indent

        + "{\n"

    )


    # RIGHT TREE

    code += generate_tree_code(

        children_right[

            node_id

        ],

        depth + 1

    )


    code += (

        indent

        + "}\n"

    )


    return code


# ============================================================
# STEP 18: GENERATE DECISION TREE C++ CODE
# ============================================================

print("\n[STEP 18] GENERATING ESP32 C++ MODEL CODE")


generated_tree_code = generate_tree_code(

    0,

    1

)


print("ESP32 Decision Tree Code Generated!")


# ============================================================
# STEP 19: CREATE HEADER FILE
# ============================================================

print("\n[STEP 19] CREATING ESP32 HEADER FILE")


header_code = """\
#ifndef WIFI_SECURITY_MODEL_H
#define WIFI_SECURITY_MODEL_H


// ============================================================
// ESP32 TinyML Wi-Fi Security Model
//
// Automatically Generated Using Python
//
// Machine Learning Model:
// Scikit-Learn DecisionTreeClassifier
//
// Class Labels:
// 0 = NORMAL
// 1 = SUSPICIOUS
//
// IMPORTANT:
// Feature order must match Python training dataset.
// ============================================================


#define WIFI_NORMAL 0

#define WIFI_SUSPICIOUS 1


// ============================================================
// TINYML PREDICTION FUNCTION
// ============================================================


int predictWiFiSecurity(

    float RSSI,

    float Avg_RSSI,

    float RSSI_Variation,

    float WiFi_Channel,

    float Packet_Count,

    float Packet_Rate,

    float Avg_Packet_Size,

    float Max_Packet_Size,

    float Data_Rate,

    float Inter_Arrival_Time,

    float Connection_Attempts,

    float Auth_Failures,

    float Invalid_Commands,

    float Repeated_Requests,

    float Command_Frequency

)

{

"""


# ADD AUTOMATICALLY GENERATED TREE CODE

header_code += generated_tree_code


# CLOSE FUNCTION AND HEADER FILE

header_code += """\

}


#endif
"""


# ============================================================
# STEP 20: WRITE HEADER FILE
# ============================================================

with open(

    HEADER_FILE,

    "w",

    encoding="utf-8"

) as file:


    file.write(

        header_code

    )


print("ESP32 Header File Created Successfully!")

print("File:", HEADER_FILE)


# ============================================================
# STEP 21: DISPLAY FEATURE ORDER
# ============================================================

print("\n====================================================")

print("FEATURE ORDER FOR ESP32")

print("====================================================")


for index, feature_name in enumerate(

    FEATURES

):


    print(

        index,

        "->",

        feature_name

    )


# ============================================================
# STEP 22: FINAL PREDICTION TEST
# ============================================================

print("\n====================================================")

print("FINAL PREDICTION TEST")

print("====================================================")


# ------------------------------------------------------------
# NORMAL SAMPLE
# ------------------------------------------------------------

normal_sample = pd.DataFrame(

    [[

        -50,    # RSSI

        -51,    # Avg_RSSI

        2.5,    # RSSI_Variation

        6,      # WiFi_Channel

        50,     # Packet_Count

        8,      # Packet_Rate

        100,    # Avg_Packet_Size

        180,    # Max_Packet_Size

        800,    # Data_Rate

        0.12,   # Inter_Arrival_Time

        1,      # Connection_Attempts

        0,      # Auth_Failures

        0,      # Invalid_Commands

        1,      # Repeated_Requests

        3       # Command_Frequency

    ]],

    columns=FEATURES

)


normal_result = model.predict(

    normal_sample

)[0]


print("\nNORMAL TEST SAMPLE:")


if normal_result == 0:


    print(

        "Prediction: NORMAL / SAFE"

    )


else:


    print(

        "Prediction: SUSPICIOUS"

    )


# ------------------------------------------------------------
# SUSPICIOUS SAMPLE
# ------------------------------------------------------------

suspicious_sample = pd.DataFrame(

    [[

        -58,    # RSSI

        -60,    # Avg_RSSI

        7.0,    # RSSI_Variation

        6,      # WiFi_Channel

        500,    # Packet_Count

        90,     # Packet_Rate

        350,    # Avg_Packet_Size

        850,    # Max_Packet_Size

        31500,  # Data_Rate

        0.01,   # Inter_Arrival_Time

        35,     # Connection_Attempts

        15,     # Auth_Failures

        10,     # Invalid_Commands

        55,     # Repeated_Requests

        70      # Command_Frequency

    ]],

    columns=FEATURES

)


suspicious_result = model.predict(

    suspicious_sample

)[0]


print("\nSUSPICIOUS TEST SAMPLE:")


if suspicious_result == 1:


    print(

        "Prediction: SUSPICIOUS / HIGH THREAT"

    )


else:


    print(

        "Prediction: NORMAL"

    )


# ============================================================
# STEP 23: FINAL COMPLETION MESSAGE
# ============================================================

print("\n")

print("====================================================")

print(" COMPLETE PROCESS FINISHED SUCCESSFULLY")

print("====================================================")


print("\nGENERATED OUTPUT FILES:")


print("\n1. Trained Machine Learning Model:")

print("   ", MODEL_FILE)


print("\n2. ESP32 TinyML Header File:")

print("   ", HEADER_FILE)


print("\n3. Model Performance Results:")

print("   ", RESULT_FILE)


print("\n====================================================")

print(" NEXT STEP")

print("====================================================")


print(

    "\nCopy the generated wifi_security_model.h "

    "file into your ESP32 Arduino project folder."

)


print(

    "\nThen include it in Arduino code using:"

)


print(

    '#include "wifi_security_model.h"'

)


print("\n====================================================")
