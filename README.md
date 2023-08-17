# YouTube Processor

This project provides a GUI application to process YouTube URLs and extract main themes from the content using a ChatOpenAI model.

## Setup

### Environment Variables
Set up the `.env` file with necessary configurations for the ChatOpenAI model and any other configurations.

## Files

- **main.py**: The entry point for the application. Initializes the YouTubeProcessor and the GUI.
- **youtube_processor.py**: Contains the `YouTubeProcessor` class. Responsible for processing the YouTube URL, extracting content, and identifying main themes using the ChatOpenAI model.
- **gui_components.py**: Contains the `AppGUI` class. Defines the GUI components and their behaviors.

## Usage

1. Run the `main.py` script:
```bash
python main.py
```

In the GUI:
- Enter a valid YouTube URL.
- Adjust the chunk size if necessary.
- Click on the "Process" button.
- Review the extracted themes in the results section.