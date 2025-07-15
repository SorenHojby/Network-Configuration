import argparse
from core.config_loader import load_switch_data
from core.config_renderer import render_configs
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logs/network_config_switches.log"),
        logging.StreamHandler()
    ]
)

def main():
    """
    Entry point for the CLI tool.

    Parses command-line arguments for:
    - input YAML file containing switch data *required*
    - Jinja2 template file *defaults to 'templates/switch_config.j2'*
    - output folder for generated configuration files *required*

    Loads the switch data, renders the configurations using the template,
    and writes the output files to the specified folder.
    """
    parser = argparse.ArgumentParser(description="Generate network configurations from YAML and Jinja2")
    parser.add_argument('--input', required=True, help='Path to YAML-configurationsfile')
    parser.add_argument('--template', default='templates/switch_config.j2', help='Path to Jinja2-template')
    parser.add_argument('--output', required=True, help='Output-folder for generated configs')

    args = parser.parse_args()
    
    switches = load_switch_data(args.input)
    if switches is None:
        print("Error loading switch data. Please check the input file.")
        exit(1)
    render_configs(switches, args.template, args.output)

if __name__ == "__main__":
    main()