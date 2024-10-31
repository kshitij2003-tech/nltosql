# NL to SQL Project

## Overview

The NL to SQL Project leverages Ollama and the OpenAI API to transform natural language input into SQL queries. This system enables users to interact with databases using plain language, simplifying data retrieval and enhancing user experience.

## Features

- **Natural Language Processing**: Converts user queries in plain language into accurate SQL statements.
- **Seamless Database Interaction**: Connects to user databases, allowing intuitive data requests.
- **User-Friendly Interface**: Eliminates the need for users to understand complex SQL syntax.

## Getting Started

### Prerequisites

- Python 3.x
- Ollama
- OpenAI API key
- Database (e.g., MySQL, PostgreSQL)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone this project link
   cd nl-to-sql
   ```

2. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the root directory with the following:
   ```
   OPENAI_API_KEY=your_openai_api_key
   DATABASE_URL=your_database_url
   ```

### Usage

1. **Run the Application**:
   ```bash
   python app.py
   ```

2. **Interact with the System**:
   Once the application is running, you can input natural language queries, such as:
   - "Show me customers who made purchases this year."
   - "List all products in the inventory."

3. **View Results**:
   The application will convert your query into an SQL statement, execute it, and return the results.

## Contributing

We welcome contributions! Please fork the repository and submit a pull request. For major changes, please open an issue to discuss your ideas.

## License

This project is licensed under the MIT License. 

## Acknowledgments

- [Ollama](https://ollama.com/)
- [OpenAI API](https://openai.com/api/)
- Contributors and community for their support.

## Contact

For questions or feedback, please reach out to [kshitijkr2003@gmail.com].
