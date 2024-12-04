# Malaria Cell Detection Web Application

A web application that uses deep learning to detect malaria-infected cells from microscopic images. Built with Flask and TensorFlow, it provides a user-friendly interface for medical professionals to quickly analyze blood cell images.

## ⚠️ Disclaimer

This application is intended for **educational and research purposes only**. Please note:

- This is not a certified medical device or diagnostic tool
- Results should not be used as the sole basis for medical decisions
- The application should only be used by qualified medical professionals as a supplementary tool
- Performance and accuracy may vary depending on image quality and other factors
- Always follow proper medical protocols and guidelines for malaria diagnosis

## Features

- Upload and analyze microscopic blood cell images
- Real-time image classification
- User-friendly web interface
- Instant results with clear visualization

## Technologies Used

- Python 3.9
- Flask
- TensorFlow
- OpenCV
- Bootstrap for UI

## CI/CD

- Automated testing and deployment using GitHub Actions
- Continuous Integration: `main` branch is automatically built and tested on every push
- Continuous Deployment: `main` branch is automatically deployed to production on every successful build

## Local Development

### Prerequisites

- Python 3.9+
- Git

### Setup

1. Clone the repository:
```bash
git clone <your-repository-url>
cd mlp-malaria-app
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Access the web interface through your browser
2. Click on the "Upload Image" button
3. Select a microscopic blood cell image
4. Click "Analyze Image" to get the results
5. The application will display whether the cell is infected or not

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.
