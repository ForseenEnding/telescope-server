# Flask Camera App

This project is a web service built using Flask that allows users to view, control, and transfer images from a USB-connected camera.

## Project Structure

```
flask-camera-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── camera.py
│   └── templates
│       └── index.html
├── static
│   └── css
│       └── styles.css
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-camera-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:
   ```
   flask run
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000` to access the application.

## Features

- View images captured from the USB-connected camera.
- Control camera settings and capture images.
- Transfer images to your local machine.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you would like to add.

## License

This project is licensed under the MIT License. See the LICENSE file for details.