"""Utility functions for loading and managing ML models"""
import pickle
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ModelLoader:
    """Handles loading and caching of ML models"""
    
    def __init__(self, model_dir="saved_models"):
        self.model_dir = Path(model_dir)
        self.models = {}
    
    def load_model(self, model_name, file_path):
        """Load a single model with error handling"""
        try:
            full_path = self.model_dir / file_path
            if full_path.exists():
                with open(full_path, 'rb') as f:
                    self.models[model_name] = pickle.load(f)
                logger.info(f"Successfully loaded {model_name} model from {full_path}")
                return True
            else:
                logger.warning(f"Model file not found: {full_path}")
                return False
        except Exception as e:
            logger.error(f"Error loading {model_name} model: {str(e)}")
            return False
    
    def load_all_models(self):
        """Load all available models"""
        models_config = {
            'diabetes': 'diabetes.pkl',
            'heart': 'heart.pkl',
            'kidney': 'kidney.pkl'
        }
        
        results = {}
        for model_name, file_path in models_config.items():
            results[model_name] = self.load_model(model_name, file_path)
        
        return results
    
    def get_model(self, model_name):
        """Retrieve a loaded model"""
        return self.models.get(model_name, None)
    
    def model_exists(self, model_name):
        """Check if a model is loaded"""
        return model_name in self.models
