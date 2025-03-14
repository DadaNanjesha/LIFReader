# 🚀 LIFReader: Visualize and Understand AGV Layouts 🗺️

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Dependencies](https://img.shields.io/badge/Dependencies-Up%20to%20date-brightgreen)](https://requires.io/github/your-username/LIFReader/requirements/?branch=main)
[![Code Style](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)


## ✨ Overview

LIFReader is a powerful Python tool designed to **parse, visualize, and analyze AGV (Automated Guided Vehicle) layouts** defined in the Layout Interchange Format (LIF). Imagine effortlessly transforming complex AGV track layouts into clear, insightful visualizations – that's what LIFReader empowers you to do!

Inspired by the VDA 5050 standard, LIFReader provides a streamlined way to understand and work with AGV systems. Whether you're an integrator, system designer, or researcher, LIFReader offers a valuable toolkit for navigating the world of automated vehicle layouts.

## 🌟 Key Features

*   **Effortless LIF Parsing**: Seamlessly converts LIF files into a structured graph representation.
*   **Stunning Visualizations**: Transforms AGV layouts into easily understandable visual maps using Matplotlib.
*   **Fully Configurable**: Customize visualization settings (colors, node sizes, labels) via a simple `config.json` file.
*   **Logging Support**: Track script activity with comprehensive logging for debugging and analysis.
*   **Lightweight and Modular**: Easy to integrate into existing projects and workflows.

## 🛠️ Installation

Get LIFReader up and running in a few simple steps:

1.  **Clone the repository:**

    ```
    git clone https://github.com/your-username/LIFReader.git
    cd LIFReader
    ```

2.  **Install the dependencies:**

    ```
    pip install networkx matplotlib pydantic
    ```

## 🚀 Quick Start

Ready to visualize your AGV layout? Follow these steps:

1.  **Configure `config.json`**:

    *   Update the `lif_file` path in `config.json` to point to your LIF file.
    *   Customize graph appearance in the `graph_settings` section.

2.  **Run the script:**

    ```
    python main.py
    ```

    ✨ Voila! ✨ You'll see a Matplotlib window displaying your AGV layout. An image file is created by the script to the file path you provided in the filepaths section.

## ⚙️ Configuration

The `config.json` file puts you in control!  Here's a breakdown of the key settings:

*   **`file_paths`**:  Specify file locations.
    *   `lif_file`: Path to your LIF JSON file.
    *   `output_graph`:  (Optional) Path to save the visualization as a PNG image.
*   **`graph_settings`**:  Customize the look and feel of the graph.
    *   `node_size`: Size of nodes.
    *   `node_color`: Color of nodes.
    *   `with_labels`: Show/hide node labels.
    *   `edge_color`: Color of edges.
    *   `edge_width`: Width of edges.
    *   `edge_alpha`: Edge transparency.
    *   `edge_style`: Edge line style ("solid", "dashed", etc.).
    *   `edge_connectionstyle`: Edge curvature ("-" for straight lines).
*   **`logging`**: Configure logging behavior.
    *   `log_level`:  Set the logging level ("INFO", "DEBUG", "WARNING", "ERROR").
    *   `log_file`:  Specify the log file path.
*   **`command_line_args`**:  Enable or disable features.
    *   `lif`: Enable LIF parsing.
    *   `visualize`: Enable graph visualization.

## 🏗️ Project Structure

LIFReader is thoughtfully organized for clarity and maintainability:

```
LIFReader/
├── lif_reader/
│ ├── init.py
│ ├── json_reader.py
│ ├── graph/
│ │ ├── init.py
│ │ ├── graph_renderer.py
│ │ ├── lif_graph.py
│ ├── models/
│ │ ├── init.py
│ │ ├── action.py
│ │ ├── action_parameter.py
│ │ ├── control_point.py
│ │ ├── edge.py
│ │ ├── layout.py
│ │ ├── lif.py
│ │ ├── load_restriction.py
│ │ ├── meta_information.py
│ │ ├── node.py
│ │ ├── station.py
│ │ ├── trajectory.py
│ │ ├── vehicle_type_edge_property.py
│ │ ├── vehicle_type_node_property.py
│ ├── utils/
│ │ ├── init.py
│ │ ├── config_loader.py
├── files/
│ ├── example2.json
├── logs/
│ ├── lif_reader.log
├── config.json
├── main.py
├── requirements.txt
├── setup.py
├── LICENSE
└── README.md


```

## 🎯 Contributing

LIFReader thrives on community contributions! Whether you have bug fixes, new features, or documentation improvements, we welcome your input.

1.  Fork the repository.
2.  Create a feature branch (`git checkout -b feature/your-feature`).
3.  Commit your changes (`git commit -am 'Add some feature'`).
4.  Push to the branch (`git push origin feature/your-feature`).
5.  Create a new Pull Request.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

*   This project was created according to VDMA.
*   Thanks to the open-source community for providing valuable libraries and resources.


## ⭐️ Support & Call-to-Action

If you find this project useful, please consider:
- **Starring** the repository ⭐️
- **Forking** the project to contribute enhancements
- **Following** for updates on future improvements

Your engagement helps increase visibility and encourages further collaboration!

---

Happy coding! 🚀✨


