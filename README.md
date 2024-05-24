# Inflation Explorer

This is the GitHub repository for the project featured on Posit's End-to-End Workflow with Posit Team in May 2024. In the webinar, we feature a Quarto dashboard that is automatically refreshed on a monthly basis to feature the latest Consumer Price Index data from the Bureau of Labor Statistics.

* YouTube Link
* Slides

├── images
│   └── logo.png            # Logo image to use in the dashboard
├── .gitignore              # Files and folders to ignore when pushing up changes
├── README.md               # Project overview and setup instructions
├── _publish.yml            # File for specifying the publishing destination
├── _quarto.yml             # Quarto project configuration file
├── all_data_report.json    # JSON version of the downloaded BLS data
├── custom.scss             # Custom Sass file
├── data-pull.qmd           # Quarto document version of the ETL script
├── filename.csv            # CSV version of the downloaded BLS data
├── index.qmd               # Quarto dashboard document
├── requirements.txt        # List of dependencies
└── script.py               # Python script version of the ETL script



