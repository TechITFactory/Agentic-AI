"""
Test Client for ML Prediction API

Demonstrates how to use the API from Python.
"""

import requests
import json
from typing import List

# API base URL
BASE_URL = "http://localhost:8000"


def test_health():
    """Test health endpoint."""
    print("\n" + "="*60)
    print("Testing Health Check")
    print("="*60)
    
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    print("✅ Health check passed")


def test_single_prediction():
    """Test single prediction endpoint."""
    print("\n" + "="*60)
    print("Testing Single Prediction")
    print("="*60)
    
    # Sample features
    payload = {
        "features": [25.0, 50000.0, 3.5, 1.0]
    }
    
    print(f"Request: {json.dumps(payload, indent=2)}")
    
    response = requests.post(
        f"{BASE_URL}/predict",
        json=payload
    )
    
    print(f"\nStatus Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    assert response.status_code == 200
    result = response.json()
    assert "prediction" in result
    assert "model_version" in result
    print("✅ Single prediction passed")


def test_batch_prediction():
    """Test batch prediction endpoint."""
    print("\n" + "="*60)
    print("Testing Batch Prediction")
    print("="*60)
    
    # Multiple instances
    payload = {
        "instances": [
            [25.0, 50000.0, 3.5, 1.0],
            [30.0, 60000.0, 4.0, 0.0],
            [35.0, 70000.0, 2.5, 1.0]
        ]
    }
    
    print(f"Request with {len(payload['instances'])} instances")
    
    response = requests.post(
        f"{BASE_URL}/predict/batch",
        json=payload
    )
    
    print(f"\nStatus Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    assert response.status_code == 200
    result = response.json()
    assert len(result["predictions"]) == len(payload["instances"])
    print(f"✅ Batch prediction passed ({result['count']} predictions)")


def test_invalid_input():
    """Test error handling with invalid input."""
    print("\n" + "="*60)
    print("Testing Invalid Input Handling")
    print("="*60)
    
    # Invalid: empty features
    payload = {
        "features": []
    }
    
    response = requests.post(
        f"{BASE_URL}/predict",
        json=payload
    )
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    assert response.status_code == 422  # Validation error
    print("✅ Invalid input correctly rejected")


def test_model_info():
    """Test model info endpoint."""
    print("\n" + "="*60)
    print("Testing Model Info")
    print("="*60)
    
    response = requests.get(f"{BASE_URL}/model/info")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    assert response.status_code == 200
    print("✅ Model info retrieved")


def benchmark_api(num_requests=100):
    """Simple benchmark of API performance."""
    print("\n" + "="*60)
    print(f"Benchmarking API ({num_requests} requests)")
    print("="*60)
    
    import time
    
    payload = {
        "features": [25.0, 50000.0, 3.5, 1.0]
    }
    
    start_time = time.time()
    
    for i in range(num_requests):
        response = requests.post(f"{BASE_URL}/predict", json=payload)
        assert response.status_code == 200
        
        if (i + 1) % 10 == 0:
            print(f"  Completed {i + 1}/{num_requests} requests...")
    
    elapsed_time = time.time() - start_time
    avg_latency = (elapsed_time / num_requests) * 1000  # ms
    throughput = num_requests / elapsed_time
    
    print(f"\nResults:")
    print(f"  Total time: {elapsed_time:.2f} seconds")
    print(f"  Average latency: {avg_latency:.2f} ms")
    print(f"  Throughput: {throughput:.2f} requests/second")
    print("✅ Benchmark completed")


def main():
    """Run all tests."""
    print("="*60)
    print("ML Prediction API - Test Suite")
    print("="*60)
    print("\nMake sure the API is running on http://localhost:8000")
    print("Start it with: python simple_ml_api.py")
    
    try:
        # Basic tests
        test_health()
        test_single_prediction()
        test_batch_prediction()
        test_invalid_input()
        test_model_info()
        
        # Performance test
        benchmark_api(num_requests=50)
        
        print("\n" + "="*60)
        print("✅ ALL TESTS PASSED")
        print("="*60)
        
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Could not connect to API")
        print("Make sure the API is running on http://localhost:8000")
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()
