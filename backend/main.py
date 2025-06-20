
## FastAPI Backend for Financial LLM App

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Create the FastAPI application instance
app = FastAPI(
    title="Financial LLM App",
    description="A portfolio analysis app with AI-powered investment suggestions",
    version="1.0.0"
)

# Add CORS middleware to allow your frontend to connect
# This allows your React Native app to make requests to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your actual frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Your first API endpoint - a simple welcome message
@app.get("/")
def read_root():
    """
    Welcome endpoint - this will be your app's homepage
    """
    return {
        "message": "Welcome to your Financial LLM App!",
        "status": "Server is running successfully",
        "version": "1.0.0"
    }

# Health check endpoint - useful for monitoring if your app is working
@app.get("/health")
def health_check():
    """
    Health check endpoint to verify the server is running
    """
    return {"status": "healthy", "message": "Server is operational"}

# A test endpoint to verify everything is working
@app.get("/test")
def test_endpoint():
    """
    Test endpoint to make sure your API is responding
    """
    return {
        "message": "Test successful!",
        "next_steps": [
            "Add market data endpoints",
            "Create user authentication",
            "Build portfolio management",
            "Integrate AI recommendations"
        ]
    }

# This runs the server when you execute this file directly
if __name__ == "__main__":
    # Run the server on localhost:8000
    # You can access it at: http://127.0.0.1:8000
    uvicorn.run(
        "main:app",  # This refers to the 'app' variable in this file
        host="127.0.0.1",  # localhost
        port=8000,  # Port number
        reload=True  # Automatically restart when you make changes
    )