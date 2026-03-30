from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import settings
from app.chains import build_map_chain, build_combine_chain

class ContentSummarizer:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = settings.CHUNK_SIZE,
            chunk_overlap = settings.CHUNK_OVERLAP
        )
        self.map_chain = build_map_chain()
        self.combine_chain = build_combine_chain()

    def split_text(self, text: str) -> list[str]:
        return self.text_splitter.split_text(text)
    
    def summarize(self, text: str) -> str:
        chunks = self.split_text(text)

        if not chunks:
            raise ValueError("No text chunks were created for summarization.")
        
        partial_summaries = []
        for chunk in chunks:
            summary = self.map_chain.invoke({"context": chunk})
            partial_summaries.append(summary)

        combined_input = "\n\n".join(partial_summaries)
        final_summary = self.combine_chain.invoke({"context": combined_input})

        return final_summary