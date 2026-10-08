#ifndef WIFI_SECURITY_MODEL_H
#define WIFI_SECURITY_MODEL_H


// ================================00000000000000000000000000000000000000============================
// ESP32 TinyML Wi-Fi Security Model
//
// Automatically Generated Using Python
//
// Machine Learning Model:
// Scikit-Learn DecisionTreeClassifier
//
// Class Labels:
// 0 = NORMAL
// 1 = SUSPICIOUS 010000000000000000000000000000
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

    if (Repeated_Requests <= 13.000000f)
    {
        return 0;
    }
    else
    {
        return 1;
    }

}


#endif
