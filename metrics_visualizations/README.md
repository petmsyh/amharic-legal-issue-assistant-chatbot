# Metrics Visualizations

This directory contains automatically generated visualization charts for the Software Metrics Document.

## Charts Available

### 1. Code Distribution (`code_distribution.png`)
- **Type:** Pie chart and bar chart
- **Purpose:** Shows the distribution of code between Python (40.2%) and HTML (59.8%)
- **Data:** Based on lines of executable code across all project files

### 2. Complexity Distribution (`complexity_distribution.png`)
- **Type:** Horizontal bar chart
- **Purpose:** Displays cyclomatic complexity for each function in the codebase
- **Key Insight:** All 7 functions are Grade A (complexity 1-4)
- **Average:** 2.71 (excellent)

### 3. Maintainability Index (`maintainability_index.png`)
- **Type:** Horizontal bar chart with gauge
- **Purpose:** Shows maintainability scores for each Python file
- **Range:** 56.47 to 100.00 (all Grade A)
- **Average:** 77.00

### 4. LOC Breakdown (`loc_breakdown.png`)
- **Type:** Grouped bar chart
- **Purpose:** Compares code, comment, and blank lines between Python and HTML
- **Highlights:** Python has 119 code lines with 12 comments; HTML has 177 lines

### 5. Metrics Dashboard (`metrics_dashboard.png`)
- **Type:** Composite dashboard with multiple visualizations
- **Purpose:** Comprehensive overview of all key metrics
- **Sections:**
  - Total LOC: 337
  - Average Complexity: 2.71 (Grade A)
  - Average MI: 77.0 (Grade A)
  - Language distribution pie chart
  - File-level LOC breakdown
  - Quality indicators

### 6. Quality Comparison (`quality_comparison.png`)
- **Type:** Grouped bar chart
- **Purpose:** Compares project metrics against industry averages
- **Metrics Compared:**
  - Cyclomatic Complexity: 95 vs 70 (above average ✓)
  - Maintainability Index: 77 vs 65 (above average ✓)
  - Comment Density: 30 vs 75 (below average ✗)
  - Code Duplication: 20 vs 95 (needs improvement ✗)
  - Test Coverage: 0 vs 70 (critical gap ✗)

## Regenerating Charts

To regenerate all charts with updated data:

```bash
python generate_metrics_charts.py
```

This will overwrite existing charts in this directory.

## Requirements

Charts are generated using:
- matplotlib >= 3.5.0
- numpy >= 1.21.0

## Usage in Documentation

These visualizations are referenced in `SOFTWARE_METRICS_DOCUMENT.md` to provide graphical representation of the metrics data.

## Notes

- All charts are saved at 300 DPI for high-quality printing
- Color scheme follows accessibility guidelines
- Charts use consistent styling for professional appearance
- File sizes optimized for web viewing (100-300KB each)
