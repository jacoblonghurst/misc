import os
import json
import pprint
from pathlib import Path
from typing import List, Dict, Any


def extract_host_info(host: str) -> List[str]:
    return [
        f"host: {host}",
        "release: CentOS Linux release 7.7.1908 (Core)",
        "kernel: 3.10.0-1160.36.2.el7.x86_64",
        "uptime: 154 days",
        "free_memory: 69%",
        "used_memory: 4901MB",
        "available_memory: 11144MB",
        "load_avg_1_min: 0.48",
        "load_avg_5_min: 0.37",
        "load_avg_15_min: 0.41",
        "free_disk_space: 90%",
        "used_disk_space: 8850MB",
        "avail_disk_space: 86680MB",
    ]


def create_json_file():
    cleaned = Path('clean_host_data.json')
    if cleaned.exists():
        os.remove(cleaned)

    with open('host_metadata.json', 'w') as f:
        meta = {'host': 'db123.or1', 'server_id': 41231, 'location': 'Oregon', 'rack_location': 'SE:1211.dc', 'asset_tag': '98211ADQ1'}
        json.dump(meta, f)


def verify_json_saved():
    with open('clean_host_data.json', 'r') as f:
        data = json.load(f)

    keys = ['host', 'release', 'kernel', 'uptime', 'free_memory', 
            'used_memory', 'available_memory', 'load_avg_1_min', 
            'load_avg_5_min', 'load_avg_15_min', 'free_disk_space', 
            'used_disk_space', 'avail_disk_space', 'host', 'server_id', 
            'location', 'rack_location', 'asset_tag']
    return all(k in data for k in keys)

