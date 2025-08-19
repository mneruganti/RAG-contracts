# test_loader.py

from load_files import load_documents  # assuming your main function is in load_py.py

def test_loader():
    # Call your loader
    documents = load_documents("contracts/")   # adjust path to your dataset

    # Basic checks
    print(f"✅ Loaded {len(documents)} documents")
    
    # Show sample metadata for sanity check
    for i, doc in enumerate(documents[::]):
        print("\n--- Document Preview ---")
        print(f"Source: {doc['source: ']}")
        print(f"Text (first 300 chars): {doc['text: '][:300]}...")
        print(f"Length: {len(doc['text: '].split())} words")

if __name__ == "__main__":
    test_loader()
