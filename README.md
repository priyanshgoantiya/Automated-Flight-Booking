# 🛫 Automated Flight Booking (AI Browser Automation)

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Browser-Use](https://img.shields.io/badge/AI-Browser--Use-green.svg)](https://github.com/browser-use/browser-use)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An AI-powered browser automation system that automates flight search and booking processes using natural language commands and intelligent decision-making.

## 📌 Project Overview

This project automates the complete flight booking workflow from **Delhi (DEL)** to **Mumbai (BOM)** on popular travel websites. The system uses AI to generate realistic passenger data, select optimal flights based on user criteria, and navigate through the booking process while extracting structured flight information.

## 🚀 Features

- **AI-Powered Automation**: Uses natural language processing to interact with booking websites
- **Smart Flight Selection**: Automatically selects flights based on lowest price or shortest duration
- **Dynamic Data Generation**: AI-generated realistic passenger details and travel information
- **Structured Data Export**: Saves extracted flight details in JSON and CSV formats
- **Safe Automation**: Stops before payment to prevent accidental transactions
- **Cross-Platform**: Works on major flight booking platforms (MakeMyTrip, Goibibo, etc.)

## 🛠 Tech Stack

- **Python 3.10+** - Core programming language
- **Browser-Use** - AI-powered browser automation framework
- **Playwright** - Reliable browser automation and testing
- **Asyncio** - For handling asynchronous operations
- **JSON/CSV** - Structured data storage and export

## 📁 Repository Structure
Automated-Flight-Booking/
├── flight_booking.py # Main automation script
├── requirements.txt # Project dependencies
├── LICENSE # MIT License
├── README.md # Project documentation
├── config/ # Configuration files
│ └── booking_config.json # User preferences and settings
├── output/ # Generated outputs
│ ├── booking_data.json # Extracted flight details (JSON)
│ └── booking_data.csv # Extracted flight details (CSV)
└── screenshots/ # Automation process screenshots


## ⚡ Quick Start

### Prerequisites
- Python 3.10 or higher
- Git installed on your system

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Automated-Flight-Booking.git
   cd Automated-Flight-Booking

pip install -r requirements.txt
playwright install

python flight_booking.py
