# AI DDR Report Generator

## Overview
This project is an AI-based workflow that reads two technical input documents:

1. Inspection Report
2. Thermal Report

It extracts relevant observations, merges the findings logically, handles missing/conflicting details, and generates a client-ready DDR (Detailed Diagnostic Report).

## Features
- Upload Inspection and Thermal Reports
- Extract text from PDF/DOCX
- Extract relevant images from PDF documents
- Generate structured DDR report using Gemini LLM
- Handles missing and conflicting information
- Produces client-friendly output
- Saves downloadable report

## DDR Output Structure
1. Property Issue Summary
2. Area-wise Observations
3. Probable Root Cause
4. Severity Assessment (with reasoning)
5. Recommended Actions
6. Additional Notes
7. Missing or Unclear Information

## Tech Stack
- Python
- Streamlit
- Gemini API
- PyMuPDF
- python-docx

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt