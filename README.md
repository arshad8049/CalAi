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

## Environment Variables

Before running the backend, set the following (e.g. in your shell or a `.env` file):

```bash
export CALORIENINJAS_API_KEY="your_api_key_here"
export DATABASE_URL="sqlite:///./calai.db"  # or your production Postgres URL
```

## API Reference

### Nutrition Estimation (Dry Run)
- **Endpoint**: `POST /api/estimate`
- **Request Body**:
  ```json
  { "description": "meal description" }
  ```
- **Response**:
  ```json
  {
    "calories": 123.4,
    "protein": 10.2,
    "fat": 5.6,
    "carbs": 15.8,
    "fiber": 2.3
  }
  ```
- **Description**: Returns the calorie and macro breakdown without saving to the database.

### Create Meal Entry
- **Endpoint**: `POST /api/meals`
- **Request Body**:
  ```json
  { "description": "meal description" }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "description": "meal description",
    "calories": 123.4,
    "protein": 10.2,
    "fat": 5.6,
    "carbs": 15.8,
    "fiber": 2.3,
    "timestamp": "2025-05-03T21:14:28.112178"
  }
  ```
- **Description**: Estimates and persists the nutrition data for a meal.

### Get Meals by Date
- **Endpoint**: `GET /api/meals?date_str=YYYY-MM-DD`
- **Response**:
  ```json
  [
    {
      "id": 1,
      "description": "meal description",
      "calories": 123.4,
      "protein": 10.2,
      "fat": 5.6,
      "carbs": 15.8,
      "fiber": 2.3,
      "timestamp": "2025-05-03T21:14:28.112178"
    },
    ...
  ]
  ```
- **Description**: Retrieves all meal entries for the given date.

## Next Steps

- Backend is fully set up with nutrition endpoints and data persistence.
- No further backend tasks remain—time to start frontend development!