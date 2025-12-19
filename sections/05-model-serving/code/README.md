# FastAPI ML Model Serving Example

Production-ready example of serving ML predictions via REST API.

## Files

- `simple_ml_api.py` - FastAPI application with prediction endpoints
- `test_api.py` - Test client demonstrating API usage
- `Dockerfile` - Docker image for deployment
- `requirements.txt` - Python dependencies

## Features

✅ **Input Validation** - Pydantic schemas ensure data quality
✅ **Error Handling** - Proper HTTP status codes and error messages
✅ **Logging** - Request/response logging for monitoring
✅ **Health Checks** - Kubernetes-ready health endpoint
✅ **Batch Predictions** - Efficient batch processing
✅ **API Documentation** - Auto-generated with Swagger UI

## Quick Start

### 1. Install Dependencies

```bash
pip install fastapi uvicorn pydantic numpy joblib requests
```text
### 2. Run the API

```bash
python simple_ml_api.py
```text
The API will start on `http://localhost:8000`

### 3. Test the API

In a new terminal:

```bash
python test_api.py
```text
Or use curl:

```bash

# Health check

curl http://localhost:8000/health

# Single prediction

curl -X POST http://localhost:8000/predict \

  -H "Content-Type: application/json" \
  -d '{"features": [25.0, 50000.0, 3.5, 1.0]}'

# Batch prediction

curl -X POST http://localhost:8000/predict/batch \

  -H "Content-Type: application/json" \
  -d '{"instances": [[25.0, 50000.0, 3.5, 1.0], [30.0, 60000.0, 4.0, 0.0]]}'

```text
### 4. Interactive Documentation

Visit http://localhost:8000/docs for Swagger UI where you can test all endpoints interactively.

## Docker Deployment

### Build Image

```bash
docker build -t ml-api:1.0 .
```text
### Run Container

```bash
docker run -d \

  --name ml-api \
  -p 8000:8000 \

  ml-api:1.0
```text
### Check Health

```bash
curl http://localhost:8000/health
```text
### Stop Container

```bash
docker stop ml-api
docker rm ml-api
```text
## API Endpoints

### GET /

Root endpoint with API information

### GET /health

Health check for Kubernetes liveness/readiness probes

**Response:**

```json
{
  "status": "healthy",
  "model_loaded": true,
  "model_version": "1.0.0",
  "timestamp": "2024-01-01T12:00:00"
}
```text
### POST /predict

Single prediction endpoint

**Request:**

```json
{
  "features": [25.0, 50000.0, 3.5, 1.0]
}
```text
**Response:**

```json
{
  "prediction": 0.7523,
  "prediction_class": 1,
  "confidence": 0.8234,
  "model_version": "1.0.0",
  "timestamp": "2024-01-01T12:00:00"
}
```text
### POST /predict/batch

Batch prediction endpoint (up to 1000 instances)

**Request:**

```json
{
  "instances": [
    [25.0, 50000.0, 3.5, 1.0],
    [30.0, 60000.0, 4.0, 0.0]
  ]
}
```text
**Response:**

```json
{
  "predictions": [0.7523, 0.6234],
  "count": 2,
  "model_version": "1.0.0",
  "timestamp": "2024-01-01T12:00:00"
}
```text
### GET /model/info

Get model information

## Production Considerations

### Security

- ✅ Runs as non-root user in Docker
- ⚠️ Add authentication (API keys, OAuth)
- ⚠️ Add rate limiting
- ⚠️ Enable HTTPS in production

### Performance

- ✅ Batch endpoint for multiple predictions
- ⚠️ Add model caching
- ⚠️ Consider async prediction queue for long-running models
- ⚠️ Add connection pooling

### Monitoring

- ✅ Structured logging
- ⚠️ Add Prometheus metrics
- ⚠️ Add distributed tracing (OpenTelemetry)
- ⚠️ Set up alerting

### Reliability

- ✅ Health check endpoint
- ✅ Input validation
- ⚠️ Add retry logic
- ⚠️ Add circuit breakers
- ⚠️ Implement graceful shutdown

## Replacing Mock Model

To use a real trained model:

1. Train and save model:
```python
import joblib
from sklearn.ensemble import RandomForestClassifier

# Train your model

model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save it

joblib.dump(model, 'models/model.pkl')
```text
2. Update `simple_ml_api.py`:
```python
@app.on_event("startup")
async def load_model():
    global model
    model = joblib.load('models/model.pkl')
```text
3. Update Dockerfile to copy model:
```dockerfile
COPY models/ ./models/
```text
## Load Testing

Use `hey` or `ab` for load testing:

```bash

# Install hey

go install github.com/rakyll/hey@latest

# Test single prediction endpoint

hey -n 1000 -c 10 \

  -m POST \
  -H "Content-Type: application/json" \
  -d '{"features": [25.0, 50000.0, 3.5, 1.0]}' \

  http://localhost:8000/predict
```text
Or use Apache Bench:

```bash
ab -n 1000 -c 10 \

  -p payload.json \
  -T application/json \

  http://localhost:8000/predict
```text
## Next Steps

1. Add authentication (API keys or OAuth)
2. Implement caching for frequent predictions
3. Add Prometheus metrics
4. Set up CI/CD pipeline
5. Deploy to Kubernetes (see Section 6)
6. Implement A/B testing for model versions

## Common Issues

**Port already in use**:

```bash

# Find process using port 8000

lsof -i :8000

# Kill it

kill -9 <PID>
```text
**Model not loading**:

- Check file path is correct
- Ensure model file exists
- Verify Python version compatibility

**High latency**:

- Use batch prediction for multiple instances
- Consider model optimization (quantization, pruning)
- Profile code to find bottlenecks

## Learn More

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Docs](https://docs.pydantic.dev/)
- [Uvicorn Docs](https://www.uvicorn.org/)
