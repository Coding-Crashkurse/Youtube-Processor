from youtube_processor import YouTubeProcessor
from gui_components import AppGUI

def main():
    processor = YouTubeProcessor()
    app = AppGUI(processor=processor)
    app.run()

if __name__ == "__main__":
    main()
