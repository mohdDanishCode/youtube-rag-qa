from langchain_community.document_loaders import YoutubeLoader

def load_youtube_transcript(video_url: str):
    loader = YoutubeLoader.from_youtube_url(
        video_url,
        add_video_info=False,
        language=["en"]
    )
    documents  = loader.load()
    return documents