from typing import List, Dict, Any

# "text" is the string that contains the entirety of the contract

def normalize_whitespace(text: str) -> str:
    # This converts all whitespace to single spaces for consistency
    return " ".join(text.split())

def chunk_text(text: str, chunk_size: int=500, overlap: int=50) -> List[str]:
    
    """Split `text` into overlapping word-based chunks.

    Args:
        text: The raw text to split.
        chunk_size: Target size of each chunk in *words*.
        overlap: Number of words to overlap between consecutive chunks.

    Returns:
        A list of chunk strings.
    """
    
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than 0")
    if overlap < 0:
        raise ValueError("Overlap size must be greater than 0")
    if chunk_size <= overlap:
        raise ValueError("Chunk size must be bigger than overlap")
    
    
    words = text.split()
    
    # If words is empty, return an empty array
    if not words:
        return []
    
    step = chunk_size - overlap
    # chunks = List[str] = []
    chunks = []
    
    # So this works by storing "chunk_size" words in "chunks", and iterating by a stride of "step"
    # The "overlap" # of last words will be the beginning of the next element
    
    """
        Example: "hello how are you today", chunk_size = 2, overlap = 1
        ["hello how", "how are", "are you", "you today"]
    """
    
    for start in range(0, len(words), step):
        end = start + chunk_size
        chunk_words = words[start:end]
        if not chunk_words:
            break
        chunks.append(" ".join(chunk_words))

        if end >= len(words):
            break
        
    return chunks

def create_chunks(documents: List[Dict[str, Any]],
    chunk_size: int = 500,
    overlap: int = 50,
    normalize: bool = True,
) -> List[Dict[str, Any]]:
    
    """Create chunk metadata dicts from raw documents.

    Each input document must have keys: {"text": str, "source": str}.
    """

    all_chunks = []
    
    # for every document in the documents List of Dicts
    for doc in documents:
        
        # this holds the raw_text from the "text" attribute of each document
        raw_text = doc.get("text", "")
        
        # this holds the source from the "source" attribute of each document
        source = doc.get("source", "unknown")
        
        # normalize the text to have one whitespace if possible
        text = normalize_whitespace(raw_text) if normalize else raw_text
        
        # chunk the text using the helper function
        pieces = chunk_text(text, chunk_size=chunk_size, overlap=overlap)
        
        # enumerate applies a counter/index for every element, makinf it easily iterable
        # Now each chunk in the document is labeled with an index, and this loop loops through those chunks
        for idx, chunk in enumerate(pieces):
            
            # add information about each chunk to the all_chunks list
            all_chunks.append(
                {
                    "id": f"{source}::chunk-{idx}",
                    "source": source,
                    "chunk_index": idx,
                    "text": chunk,
                    "n_words": len(chunk.split()),
                }
            )

    return all_chunks


if __name__ == "__main__":
    # Minimal self-test (expects you already loaded documents elsewhere)
    sample_docs = [
        {"text": "This is a small example document about plans and expirations." * 20, "source": "example.txt"}
    ]
    chunks = create_chunks(sample_docs, chunk_size=20, overlap=5)
    print(f"Created {len(chunks)} chunks:")
    for c in chunks[:3]:
        print(c["id"], "->", c["n_words"], "words")
    
    