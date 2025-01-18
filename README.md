# Emergency Panic Button System

## Description
The **Emergency Panic Button System** is a safety-focused project designed to assist individuals, especially elderly people, in emergency situations. The system integrates hardware and software components to provide a quick and reliable way to notify emergency contacts and authorities when assistance is required. By combining physical panic buttons, a backend system, and a user-friendly interface, the project ensures immediate responses during emergencies.

---

## Features
1. **Panic Button Alert**:
   - A physical button is placed in multiple rooms of a house.
   - Press the button once to trigger an alert to emergency contacts via email and SMS.
   - If no one cancels the emergency mode within 20 minutes (by pressing the button twice), the system automatically sends all patient details, contact information, and the location of the triggered button to 911.

2. **Health Tips**:
   - The system retrieves health-related tips from authoritative websites based on the user's health condition and displays them on the main page.

3. **User-Friendly Interface**:
   - A web-based UI allows users to input and update personal information, including name, age, gender, health condition, and emergency contacts.

4. **Secure Login System**:
   - Supports multiple users with secure login, ensuring separate data management.

5. **Backend System**:
   - A NoSQL database stores all user details, health conditions, and emergency contacts.

---

## Components
- **Hardware**:
  - **Raspberry Pi**: Connects to the panic buttons and communicates with the backend system.
  - **Buttons**: Momentary push buttons trigger emergency alerts.
  - Additional components: Breadboard, jump wires, resistors, and LEDs.

- **Software**:
  - **Web UI**: Built using Python Flask, HTML, and CSS for an interactive user experience.
  - **NoSQL Database**: Stores user and emergency contact information.
  - **RESTful API**: Fetches health tips based on user details.

---

## How It Works
1. **Setup**:
   - Users input their personal information and emergency contacts via the web UI.
2. **Emergency Mode**:
   - Press the panic button to trigger emergency mode.
   - A notification is sent to emergency contacts via SMS and email.
   - If the emergency mode isn't canceled within 20 minutes, the system sends a detailed alert to 911.
3. **Canceling Emergency Mode**:
   - Press the panic button twice to cancel the alert and notify emergency contacts of the cancellation.

---

## System Diagram
![Screenshot](https://github.com/LXWHX/Python-Web-Server-Using-RESTful-API-Design/blob/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-01-18%20143203.png)

---

## Hardware Requirements
1. **Components**:
   - Raspberry Pi
   - Monitor
   - Computer mouse
   - Breadboard
   - Jump wires
   - Resistors
   - Momentary push buttons
