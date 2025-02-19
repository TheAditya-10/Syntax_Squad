import sys

# ✅ Machine Learning & Data Science
try:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import sklearn
    import tensorflow as tf
    import torch
    import torchvision
    import torchaudio
    print("✅ ML Libraries Loaded Successfully!")
except ImportError as e:
    print(f"❌ Missing ML Library: {e}")

# ✅ Flask & Web Frameworks
try:
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    from flask_cors import CORS
    print("✅ Flask & Web Libraries Loaded Successfully!")
except ImportError as e:
    print(f"❌ Missing Flask Library: {e}")

# ✅ Database Libraries
try:
    import mysql.connector
    import sqlalchemy
    print("✅ Database Libraries Loaded Successfully!")
except ImportError as e:
    print(f"❌ Missing Database Library: {e}")

# ✅ NLP Libraries
try:
    import transformers
    print("✅ NLP Libraries Loaded Successfully!")
except ImportError as e:
    print(f"❌ Missing NLP Library: {e}")

# ✅ General Utilities
try:
    import requests
    import json
    import os
    import re
    print("✅ Utility Libraries Loaded Successfully!")
except ImportError as e:
    print(f"❌ Missing Utility Library: {e}")

print("\n🎉 All Tests Completed!")
