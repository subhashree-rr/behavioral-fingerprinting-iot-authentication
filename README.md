# Behavioral Fingerprinting Based Continuous Authentication for IoT Devices Using Machine Learning
A TinyML-based continuous authentication system for IoT devices using behavioral fingerprinting and machine learning.
# Behavioral Fingerprinting Based Continuous Authentication for IoT Devices Using Machine Learning



## 📌 About the Project

This project presents a machine learning-based continuous authentication system for IoT devices. The system identifies authorized and unauthorized device behavior by analyzing behavioral and communication patterns.

A lightweight Decision Tree model is deployed on an embedded platform to perform local authentication and detect suspicious behavior in real time.

## 🎯 Objectives

* Develop a continuous authentication system for IoT devices.
* Identify device behavior using behavioral fingerprinting.
* Collect and analyze communication-related features.
* Train a lightweight machine learning model for classification.
* Deploy the trained model on an embedded device.
* Detect authorized and unauthorized behavior in real time.
* Provide an alert when suspicious behavior is detected.

## ⚙️ How It Works

```text
IoT Devices
     ↓
Behavior & Communication Data
     ↓
Feature Extraction
     ↓
Dataset Creation
     ↓
Machine Learning Model Training
     ↓
Decision Tree Model
     ↓
Model Conversion
     ↓
Embedded Device
     ↓
Continuous Authentication
     ↓
Authorized / Unauthorized
     ↓
LCD + Buzzer Alert
```

## 🔧 Hardware Used

* ESP32 Development Boards
* Sensors
* LCD Display
* Buzzer
* Push Button
* Breadboard
* Connecting Wires

## 💻 Software & Technologies

* Embedded C / C++
* Python
* Arduino IDE
* ESP32
* Machine Learning
* Decision Tree
* TinyML
* IoT
* CSV Dataset

## 🧠 Machine Learning

A Decision Tree classifier is used to identify the behavioral pattern of the IoT device.

The model is trained using approximately 10 behavioral and communication-related features. After training, the model is converted into an embedded-compatible C/C++ header file and integrated with the firmware.

```text
Dataset
   ↓
Preprocessing
   ↓
Feature Selection
   ↓
Model Training
   ↓
Decision Tree
   ↓
Testing
   ↓
Embedded Deployment
```

## 🔐 Continuous Authentication

Unlike traditional authentication systems that verify a device only during login, this system continuously monitors the device behavior.

The system classifies the observed behavior as:

* ✅ Authorized
* ⚠️ Unauthorized / Malicious

When suspicious behavior is detected, the system provides an alert through the LCD and buzzer.

## 📊 Results

* Successfully implemented a prototype for continuous IoT authentication.
* Achieved approximately **83% classification accuracy**.
* Demonstrated authorized and unauthorized behavior detection.
* Performed machine learning inference on the embedded platform.
* Provided real-time authentication status using LCD and buzzer.
* Demonstrated threat detection using a test condition.

## 🌐 Applications

The proposed system can be applied to:

* Smart Home Security
* Industrial IoT
* Healthcare IoT
* Smart Buildings
* Connected Devices
* IoT Security Gateways
* Edge Computing Systems

## ⭐ Advantages

* Continuous authentication
* Lightweight machine learning model
* Suitable for resource-constrained IoT devices
* Local processing
* Real-time threat detection
* Reduced dependency on cloud-based authentication
* Additional security layer for IoT devices

## 🚀 Future Scope

* Improve model accuracy using a larger dataset.
* Add more IoT devices and behavioral features.
* Explore other lightweight ML algorithms.
* Optimize memory and processing requirements.
* Implement adaptive learning.
* Develop a web/mobile monitoring dashboard.
* Extend the system for large-scale IoT networks.

## 🏁 Conclusion

This project demonstrates the use of behavioral fingerprinting and machine learning for continuous authentication of IoT devices. The lightweight Decision Tree model enables local classification of device behavior and helps identify unauthorized activity in real time.

The prototype combines **Embedded Systems, IoT, Machine Learning, and TinyML** to provide an additional layer of security for connected devices.

## 👩‍💻 Project Team

**Subhashree R R**
B.E. Electronics and Communication Engineering
Muthayammal Engineering College (Autonomous)

**Vaishnavi K**

## 📌 Project Status

**Completed – Final Year Academic Project**
