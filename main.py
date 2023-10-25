import uvicorn
from app.common.logger import logger
from app.startup.application import app
from app.config.config import get_settings



# Run the application server
if __name__ == "__main__":
    settings = get_settings()
    if settings.ENVIRONMENT == "development":
        logger.info("Running in development mode")
        uvicorn.run(app, host="localhost", port=3000)
    else:
        logger.info("Running in production mode")
        uvicorn.run(app, host="0.0.0.0", port=3000)