"""
Simple ML Prediction API with FastAPI

This is a production-ready example of serving ML predictions via API.
Demonstrates best practices for model serving.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
from typing import List, Dict, Any
import joblib
import numpy as np
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ============================================================================
# Pydantic Models for Request/Response Validation
# ============================================================================

class PredictionInput(BaseModel):
    """Input schema for single prediction."""
    features: List[float] = Field(
        ..., 
        description="Feature values for prediction",
        min_items=1,
        max_items=100
    )
    
    @validator('features')
    def validate_features(cls, v):
        """Validate feature values."""
        if any(np.isnan(val) or np.isinf(val) for val in v):
            raise ValueError("Features cannot contain NaN or Inf values")
        return v
    
    class Config:
        schema_extra = {
            "example": {
                "features": [25.0, 50000.0, 3.5, 1.0]
            }
        }


class PredictionOutput(BaseModel):
    """Output schema for prediction."""
    prediction: float
    prediction_class: int = None  # For classification
    confidence: float = None
    model_version: str
    timestamp: str


class BatchPredictionInput(BaseModel):
    """Input schema for batch prediction."""
    instances: List[List[float]] = Field(
        ...,
        description="List of feature vectors",
        min_items=1,
        max_items=1000  # Limit batch size
    )


class BatchPredictionOutput(BaseModel):
    """Output schema for batch prediction."""
    predictions: List[float]
    count: int
    model_version: str
    timestamp: str


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    model_loaded: bool
    model_version: str
    timestamp: str


# ============================================================================
# Mock Model (Replace with Real Model)
# ============================================================================

class MockModel:
    """
    Mock model for demonstration.
    Replace this with actual trained model loaded via joblib.
    """
    def __init__(self):
        self.version = "1.0.0"
        self.is_loaded = True
        logger.info(f"Mock model initialized (version {self.version})")
    
    def predict(self, X):
        """Make predictions."""
        # Simple mock: sum of features
        if isinstance(X, list):
            X = np.array(X)
        if len(X.shape) == 1:
            X = X.reshape(1, -1)
        
        # Mock prediction logic
        predictions = np.sum(X, axis=1) / X.shape[1]
        return predictions
    
    def predict_proba(self, X):
        """Get prediction probabilities (for classification)."""
        predictions = self.predict(X)
        # Mock probability
        proba = 1 / (1 + np.exp(-predictions))
        return proba


# ============================================================================
# FastAPI App
# ============================================================================

app = FastAPI(
    title="ML Prediction API",
    description="Production-ready ML model serving with FastAPI",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Global model instance
model = None
MODEL_VERSION = "1.0.0"


@app.on_event("startup")
async def load_model():
    """Load model on startup."""
    global model
    try:
        # In production, load actual model:
        # model = joblib.load('models/model.pkl')
        
        # For demo, use mock model
        model = MockModel()
        logger.info("Model loaded successfully")
    except Exception as e:
        logger.error(f"Failed to load model: {e}")
        raise


@app.get("/", response_model=Dict[str, str])
async def root():
    """Root endpoint."""
    return {
        "message": "ML Prediction API",
        "version": MODEL_VERSION,
        "docs": "/docs"
    }


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint for Kubernetes probes."""
    return HealthResponse(
        status="healthy" if model and model.is_loaded else "unhealthy",
        model_loaded=model is not None and model.is_loaded,
        model_version=MODEL_VERSION,
        timestamp=datetime.now().isoformat()
    )


@app.post("/predict", response_model=PredictionOutput)
async def predict(input_data: PredictionInput):
    """
    Single prediction endpoint.
    
    Args:
        input_data: PredictionInput with feature values
    
    Returns:
        PredictionOutput with prediction and metadata
    """
    try:
        # Log request (be careful with PII in production!)
        logger.info(f"Prediction request received with {len(input_data.features)} features")
        
        # Check if model is loaded
        if model is None:
            raise HTTPException(status_code=503, detail="Model not loaded")
        
        # Make prediction
        features = np.array(input_data.features).reshape(1, -1)
        prediction = model.predict(features)[0]
        
        # For classification, also get class and confidence
        prediction_class = int(prediction > 0.5)  # Binary classification threshold
        confidence = float(model.predict_proba(features)[0])
        
        response = PredictionOutput(
            prediction=float(prediction),
            prediction_class=prediction_class,
            confidence=confidence,
            model_version=MODEL_VERSION,
            timestamp=datetime.now().isoformat()
        )
        
        logger.info(f"Prediction successful: {prediction:.4f}")
        return response
        
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@app.post("/predict/batch", response_model=BatchPredictionOutput)
async def predict_batch(input_data: BatchPredictionInput):
    """
    Batch prediction endpoint.
    
    Args:
        input_data: BatchPredictionInput with multiple feature vectors
    
    Returns:
        BatchPredictionOutput with predictions for all instances
    """
    try:
        logger.info(f"Batch prediction request with {len(input_data.instances)} instances")
        
        if model is None:
            raise HTTPException(status_code=503, detail="Model not loaded")
        
        # Convert to numpy array
        features = np.array(input_data.instances)
        
        # Make predictions
        predictions = model.predict(features)
        
        response = BatchPredictionOutput(
            predictions=[float(p) for p in predictions],
            count=len(predictions),
            model_version=MODEL_VERSION,
            timestamp=datetime.now().isoformat()
        )
        
        logger.info(f"Batch prediction successful: {len(predictions)} predictions")
        return response
        
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Batch prediction error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/model/info")
async def model_info():
    """Get model information."""
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    return {
        "version": MODEL_VERSION,
        "type": "MockModel (replace with actual model type)",
        "loaded": model.is_loaded,
        "timestamp": datetime.now().isoformat()
    }


# ============================================================================
# Run Server
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    
    print("="*60)
    print("Starting ML Prediction API")
    print("="*60)
    print("\nEndpoints:")
    print("  - http://localhost:8000/docs (Interactive API docs)")
    print("  - http://localhost:8000/redoc (Alternative docs)")
    print("  - http://localhost:8000/health (Health check)")
    print("  - http://localhost:8000/predict (Single prediction)")
    print("  - http://localhost:8000/predict/batch (Batch prediction)")
    print("\nPress Ctrl+C to stop")
    print("="*60)
    
    uvicorn.run(
        "simple_ml_api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Auto-reload on code changes (dev only)
        log_level="info"
    )
