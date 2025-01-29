# PubMed Research Paper Fetcher 📑🔬

## Overview

The **PubMed Research Paper Fetcher** is a Python tool that allows users to fetch research papers from PubMed based on a query they provide. The program identifies papers that have at least one author affiliated with a pharmaceutical or biotech company and returns the filtered results in a CSV format. This tool is designed to help researchers and professionals quickly find papers of interest, especially those with industry ties.

## Features ✨

- Fetch research papers from PubMed based on a search query.
- Filter papers with at least one author from a pharmaceutical or biotech company.
- Save results as a CSV file for easy analysis and reference.
- Supports command-line interaction with customizable options.

## Code Organization 🗂️

The project is structured as follows:

```
bing/
├── __pycache__/
├── __init__.py
├── get_papers_list.py
├── pubmed_fetcher.py
├── dist/
│   ├── bing-0.1.0-py3-none-any.whl
│   └── bing-0.1.0.tar.gz
├── tests/
├── README.md
├── install-poetry.py
├── output.csv
├── output1.csv
├── output2.csv
├── output3.csv
├── output4.csv
├── output5.csv
├── output6.csv
├── poetry.lock
├── pyproject.toml
└── test.pypirc
```

### Directory Breakdown:

- **`bing/`**: Main package directory containing the core logic.
  - **`__init__.py`**: Marks the directory as a Python package.
  - **`get_papers_list.py`**: The main entry point for running the program via the command line.
  - **`pubmed_fetcher.py`**: Contains the `PubMedFetcher` class, which fetches and filters the research papers.
  
- **README.md**: This file, which provides documentation about the project.
- **install-poetry.py**: Script to install Poetry (dependency management tool).
- **output.csv**: Example output file containing filtered research papers.
- **poetry.lock**: Automatically generated by Poetry, locks dependencies to specific versions.
- **pyproject.toml**: Configuration file for managing project dependencies and settings.
- **test.pypirc**: A configuration file related to Python packaging (for future use).

## Installation 🚀

To get started, follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/bing.git
   cd bing
   ```

2. **Install Poetry** (if you don't have it installed already):
   ```bash
   python install-poetry.py
   ```

3. **Install Project Dependencies** using Poetry:
   ```bash
   poetry install
   ```

## Usage 💻

To run the program and fetch research papers, use the following command:

```bash
poetry run get-papers-list "your query here"
```

### Command-Line Options:
- `-h` or `--help`: Display usage instructions.
- `-d` or `--debug`: Enable debug mode for detailed logs.
- `-f` or `--file`: Specify a file name to save the results. If not provided, the output will be printed to the console.

### Example Command:
To fetch research papers related to "cancer research" and save the results to a CSV file:

```bash
poetry run get-papers-list "cancer research" -f output.csv
```

This command will:
- Search PubMed for papers on cancer research.
- Filter the results to include only papers with at least one author from a pharmaceutical or biotech company.
- Save the results to `output.csv`.

## Development 💡

### Running Tests:
To run the test suite, use:

```bash
poetry run pytest
```

### Linting:
To check for code style and linting issues, run:

```bash
poetry run flake8
```

## Contributing 🤝

We welcome contributions to this project! To get involved, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-branch
   ```
3. Make your changes.
4. Commit your changes:
   ```bash
   git commit -am 'Add new feature'
   ```
5. Push to your branch:
   ```bash
   git push origin feature-branch
   ```
6. Create a pull request.

## Acknowledgements 🙏

This project was developed using various open-source libraries and tools. Special thanks to the contributors and maintainers of these resources!

## Contact 📧

For any questions or inquiries, feel free to reach out at:  
[saikumar98125@gmail.com.com](mailto:saikumar98125@gmail.com)

