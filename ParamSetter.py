import json
import os
import logging

class ParamSetter:
    CONFIG_FILE_PATH = "config.json"
    DEFAULT_CONFIG_FILE_PATH = "default_config.json"

    def __init__(self):
        # Load default parameters
        self.DEFAULT_PARAMS = self.load_default_params_from_file()
        self.clahe_for_value = self.DEFAULT_PARAMS["for_value"]
        self.clahe_clip_limit = self.DEFAULT_PARAMS["cliplimit_value"]
        self.clahe_tile_grid_size = self.DEFAULT_PARAMS["tilegrid_value"]
        self.camera_resolution = tuple(map(int, self.DEFAULT_PARAMS["resolution"].split('x')))

    def load_default_params_from_file(self):
        """Load default parameters from a JSON file."""
        if os.path.exists(self.DEFAULT_CONFIG_FILE_PATH):
            with open(self.DEFAULT_CONFIG_FILE_PATH, "r") as config_file:
                default_params = json.load(config_file)
                logging.debug(f"Default parameters loaded from {self.DEFAULT_CONFIG_FILE_PATH}")
                return default_params
        else:
            default_params = {
                "for_value": 2,
                "cliplimit_value": 2.5,
                "tilegrid_value": 8,
                "resolution": "640x480"
            }
            with open(self.DEFAULT_CONFIG_FILE_PATH, "w") as config_file:
                json.dump(default_params, config_file)
            logging.debug(f"Default parameters created in {self.DEFAULT_CONFIG_FILE_PATH}")
            return default_params

    def save_params_to_file(self):
        """Save current parameters to a JSON file."""
        params = {
            "for_value": self.clahe_for_value,
            "cliplimit_value": self.clahe_clip_limit,
            "tilegrid_value": self.clahe_tile_grid_size,
            "resolution": f"{self.camera_resolution[0]}x{self.camera_resolution[1]}"
        }
        with open(self.CONFIG_FILE_PATH, "w") as config_file:
            json.dump(params, config_file)
        logging.debug(f"Parameters saved to {self.CONFIG_FILE_PATH}")

    def load_params_from_file(self):
        """Load parameters from a JSON file or fallback to default."""
        if os.path.exists(self.CONFIG_FILE_PATH):
            with open(self.CONFIG_FILE_PATH, "r") as config_file:
                params = json.load(config_file)
                self.clahe_for_value = params.get("for_value", self.DEFAULT_PARAMS["for_value"])
                self.clahe_clip_limit = params.get("cliplimit_value", self.DEFAULT_PARAMS["cliplimit_value"])
                self.clahe_tile_grid_size = params.get("tilegrid_value", self.DEFAULT_PARAMS["tilegrid_value"])
                resolution_str = params.get("resolution", self.DEFAULT_PARAMS["resolution"])
                self.camera_resolution = tuple(map(int, resolution_str.split("x")))
                logging.debug(f"Parameters loaded from {self.CONFIG_FILE_PATH}")
        else:
            logging.debug(f"No config file found, loading default parameters.")
            self.clahe_for_value = self.DEFAULT_PARAMS["for_value"]
            self.clahe_clip_limit = self.DEFAULT_PARAMS["cliplimit_value"]
            self.clahe_tile_grid_size = self.DEFAULT_PARAMS["tilegrid_value"]
            self.camera_resolution = tuple(map(int, self.DEFAULT_PARAMS["resolution"].split('x')))
