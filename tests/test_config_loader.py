import os
import tempfile
import yaml
from core.config_loader import load_switch_data

def test_load_switch_data_success():
    test_data = [
        {"hostname": "switch01", "ip": "10.0.0.1", "location": "Billund", "vlan": 42},
        {"hostname": "switch02", "ip": "10.0.0.2", "location": "Prague", "vlan": 99},
    ]

    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix=".yml") as tmp_file:
        yaml.dump(test_data, tmp_file)
        tmp_file_path = tmp_file.name

    result = load_switch_data(tmp_file_path)

    os.remove(tmp_file_path)

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["hostname"] == "switch01"
    assert result[1]["vlan"] == 99