from typing import List, Dict, Any, Tuple
import numpy as np


"""
    In order to use FAISS, we need this method to ensure that the vectors array
    is of type float32 because this is what FAISS expects
"""
def _as_float32_matrix(vectors: np.ndarray) -> np.ndarray:
    
    # if vectors is not an n dimensional np array, create an array with the datatype "float32"
    if not isinstance(vectors, np.ndarray):
        vectors = np.array(vectors, dtype = "float32")
    
    # if vectors datatype is not float32, convert it into float32 using astype()
    if vectors.dtype != np.float32:
        vectors = vectors.astype("float32", False)
    
    # return as a contiguous array for optimal memory performace as it stores everything in one
    # uninterrupted block of elements for easy access and predictability
    return np.ascontiguousrray(vectors)

def embed_with_sentence_transformer() -> List[Dict[str, Any]]:
    return 