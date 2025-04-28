# CalAi

## Overview

CalAi is a cross-platform calorie tracking application for iOS built with React Native. It leverages a Python backend and the DeepSeek AI model to estimate calories based on food descriptions. This app allows users to log meals, view daily and weekly calorie summaries, and receive daily reminders.

## Getting Started

### Prerequisites

- Node.js (>=14.x)
- npm or Yarn
- React Native CLI
- Xcode (for iOS development)
- Python 3.8+
- pip (Python package manager)
- git

### Project Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd CalAi
   ```

2. Install frontend dependencies:
   ```bash
   cd ios
   pod install
   cd ..
   npm install
   ```
   
3. Install backend dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

4. Start the Python backend:
   ```bash
   cd backend
   uvicorn main:app --reload
   ```

5. Run the React Native app on iOS simulator:
   ```bash
   npm run ios
   ```