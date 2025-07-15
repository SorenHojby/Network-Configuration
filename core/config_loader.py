import yaml
import logging
from typing import List, Dict, Optional

def load_switch_data(filepath: str) -> Optional[List[Dict[str, str]]]:
    """
    Load switch configuration data from a YAML file.

    Args:
        filepath (str): Path to the YAML file containing switch definitions.

    Returns:
        Optional[List[Dict[str, str]]]: A list of dictionaries representing each switch,
        or None if loading fails.

    Raises:
        None: All exceptions are handled internally with logging.

    Logs:
        - File not found or unreadable
        - Invalid YAML format
    """
    try:
        with open(filepath, 'r') as f:
            data = yaml.safe_load(f)
            logging.info(f"Successfully loaded {len(data)} switches from {filepath}")
            return data
    except FileNotFoundError:
        logging.error(f"File not found: {filepath}")
    except PermissionError:
        logging.error(f"Permission denied when trying to read: {filepath}")
    except yaml.YAMLError as e:
        logging.error(f"YAML parsing error in {filepath}: {e}")
    except Exception as e:
        logging.error(f"Unexpected error while reading {filepath}: {e}")
    
    return None