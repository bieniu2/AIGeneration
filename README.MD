# AI article generation

Article generator basing on text downloaded from internet with HTML and images generation.

## How it works
- Article is downloaded from internet
- OpenAI is used to generate the the article contents
- PNG file names and descriptions are extracted from article
- Images are generated basing on descriptions and saved to extracted paths
## Installation

To get started with the project, follow these steps:

1. **Clone the repository and run the test:**
   ```bash
   git clone https://github.com/bieniu2/AIGeneration.git
   cd AIGeneration
   

2. **In test.py replace API_KEY with another one (the one given in repository has been blocked due to exposing it on public github repository):**
   python test.py

3. **Run python file:**
   ```bash
   python main.py