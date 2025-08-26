# Contributing to Shellhorn

Thanks for your interest in contributing to Shellhorn! 

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/mitchins/shellhorn.git
   cd shellhorn
   ```

2. **Set up development environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e ".[dev]"
   ```

3. **Run tests**
   ```bash
   pytest --cov=shellhorn --cov=monitor --cov-report=term-missing
   ```

## Code Quality

We maintain high code quality standards:

- **Linting**: `flake8 shellhorn/ monitor/ --max-line-length=88 --extend-ignore=E203,W503`
- **Security**: `bandit -r shellhorn/ monitor/`
- **Dead code**: `vulture shellhorn/ monitor/`
- **Formatting**: `black shellhorn/ monitor/`

## Testing

- Write tests for new functionality
- Ensure all tests pass locally before submitting
- Aim for good test coverage on new code

## Pull Request Process

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes with tests
4. Run the full test suite
5. Submit a pull request with a clear description

## Questions?

Feel free to open an issue for questions or discussion!