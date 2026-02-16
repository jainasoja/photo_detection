# AI Image Sorter
This script uses OpenAI's CLIP model to find "ocean" photos in a local folder.

## Setup
1. Open PowerShell
2. Clone the repo: `git clone <your-url>`
3. Create a virtual environment: `python -m venv venv`
4. Activate it:
   - Windows: `.\venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
5. Install libraries: `pip install -r requirements.txt`

## Usage
Update the paths in code:
```py
# 2. Setup paths and keyword
search_query = "A photo of ocean or a big water mass" # CHANGE THIS 
image_folder = "Path to the photos" # CHANGE THIS 
matches_folder = "Path to the new folder (does not have exist)" # CHANGE THIS 
```

Run:
`python recognize.py`

If ran twice it will just add new matches to the same folder so remember to change folder paths if this is not the desired functionality. 

## Other
There is some sections commented out. If results are not showing the top 5 matches and their values could be printed when removing `#` from lines 44-47. Whit these values the threshold could be adjusted on line 51 to get more matches.
