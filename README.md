# Weather Flask API

## API Documentation

### Base URL

http://localhost:5000

---

## GET /weather

Get current weather information for a given city.

---

### Request

#### Endpoint

GET /weather

#### Query Parameters

| Parameter | Type   | Required | Description                          |
|----------|--------|----------|--------------------------------------|
| city     | string | No       | Name of the city (default: Auckland) |

---

### Example Request

http://localhost:5000/weather?city=Auckland

---

### Response

#### Success (200 OK)

{
  "city": "Auckland",
  "country": "NZ",
  "temperature": 18,
  "feels_like": 17,
  "humidity": 70,
  "weather": "clear sky",
  "icon_url": "https://openweathermap.org/img/wn/01d@2x.png"
}

---

### Error Response

#### Invalid city or API error

{
  "error": "Failed to fetch weather data",
  "status_code": 404,
  "details": {
    "message": "city not found"
  }
}

---

### Notes

- This API uses the OpenWeatherMap service.
- The API key is stored securely in the backend environment variable.
- The frontend should not call the external API directly.
- The backend acts as a secure layer between the frontend and the cloud service.
