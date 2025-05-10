
# Mintora

Mintora is an automated content generation platform designed to help users generate content for various purposes like blog posts, product descriptions, emails, and more. The app integrates with AI models like OpenAI to streamline content creation for different use cases.

## Installation

Follow the steps below to get the app up and running on your local machine.

### Clone the repository

To get the project, clone the repository:

```bash
git clone https://github.com/Prithika-97/Mintora.git
cd Mintora
```

### Set up the environment

1. Install Python dependencies:

```bash
pip install -r requirements.txt
```

2. Rename `.env.example` to `.env` and add your environment variables. Refer to `.env.example` for required variables.

### Run the app locally

To run the app locally, use Uvicorn:

```bash
uvicorn app.main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

### Testing the API

You can use tools like Postman or curl to test the API endpoints. For example:

```bash
curl http://127.0.0.1:8000/your-endpoint
```

## Contributing

Feel free to fork the repository, submit issues, and open pull requests. We welcome contributions!

### How to contribute

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Write tests for your changes (if applicable).
4. Make sure the tests pass by running `pytest`.
5. Submit a pull request to the `main` branch.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
