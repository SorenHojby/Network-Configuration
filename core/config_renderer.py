from jinja2 import Environment, FileSystemLoader, TemplateError
import os
import logging
from typing import List, Dict

def render_configs(switches: List[Dict[str, str]], template_path: str, output_dir: str) -> None:
    """
    Render network configuration files for a list of switches using a Jinja2 template.

    Args:
        switches (List[Dict[str, str]]): List of dictionaries containing switch configuration data.
        template_path (str): Path to the Jinja2 template file.
        output_dir (str): Path to the output folder where rendered config files will be saved.

    Returns:
        None

    Logs:
        - Template load status
        - Output folder creation
        - File write success/failure for each switch
        - Template rendering errors
    """
    try:
        env = Environment(loader=FileSystemLoader(os.path.dirname(template_path)))
        template = env.get_template(os.path.basename(template_path))
        logging.info(f"Loaded template: {template_path}")
    except TemplateError as e:
        logging.error(f"Failed to load template: {e}")
        return

    try:
        os.makedirs(output_dir, exist_ok=True)
        logging.info(f"Output folder is ready: {output_dir}")
    except Exception as e:
        logging.error(f"Failed to create output folder '{output_dir}': {e}")
        return

    for switch in switches:
        try:
            rendered = template.render(switch=switch)
            output_path = os.path.join(output_dir, f"{switch['hostname']}.conf")
            with open(output_path, "w") as f:
                f.write(rendered)
            logging.info(f"Config written for {switch['hostname']} -> {output_path}")
        except (KeyError, TemplateError) as e:
            logging.error(f"Rendering failed for switch: {switch}. Error: {e}")
        except IOError as e:
            logging.error(f"Failed to write config file for {switch['hostname']}: {e}")