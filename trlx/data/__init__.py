from dataclasses import dataclass
from typing import Iterable

from jaxtyping import Float, Array

@dataclass
class GeneralElement:
    """
    General element outputted by a data pipeline
    """

    pass


@dataclass
class RLElement:
    """
    Batch element for RL model
    """

    state: Iterable[str] = None  # Context/prompts
    action: Float[Array, "N"] = None  # Tokens generated by model given prompts
    reward: float = None  # Reward obtained for that generation


@dataclass
class BatchElement:
    """
    General batch element for any transformer to use in its forward pass
    """

    tokens: Float[Array, "BATCH", "SEQ_LEN"]
    masks: Float[Array, "BATCH", "SEQ_LEN"]
