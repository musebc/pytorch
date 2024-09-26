import dataclasses
import pathlib
from enum import Enum
from typing import Dict, List, Optional

import torch

from .metrics import Device, Metrics


@dataclasses.dataclass
class OperatorConfig:
    name: str
    variant: str
    device: str
    extra_args: List[str]
    extra_env: Optional[Dict[str, str]] = None
    output_dir: Optional[pathlib.Path] = None


class BenchmarkResults:
    def __init__(self, durations: List[float]):
        self.durations = durations

    def median(self) -> float:
        # return np.median(self.durations)
        pass


@dataclasses.dataclass
class BenchmarkConfig:
    device: Device
    dtype: torch.dtype
    phase: str
    max_samples: int
    repeat: int
    metrics: List[Metrics]
    profile: bool
    profile_folder: str


class Phase(Enum):
    FORWARD = "forward"
    BACKWARD = "backward"
    FULL = "full"


dtype_mapping = {
    "bfloat16": torch.bfloat16,
    "float16": torch.float16,
    "float32": torch.float32,
}
