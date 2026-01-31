# Spark 101 - Installation Guide for macOS

This repository contains materials for learning Apache Spark fundamentals on macOS.

## Prerequisites

- Homebrew package manager
- At least 4GB of RAM

## Installing Apache Spark on macOS

### Step 1: Install Homebrew (if not already installed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Step 2: Install Java

Apache Spark requires Java. Install using Homebrew:

```bash
brew install openjdk@11
```

Add Java to your PATH by adding this to your `~/.zshrc`:

```bash
export PATH="/opt/homebrew/opt/openjdk@11/bin:$PATH"
```

Apply changes:

```bash
source ~/.zshrc
```

Verify Java installation:

```bash
java -version
```

### Step 3: Install Apache Spark

Install Spark using Homebrew:

```bash
brew install apache-spark
```

### Step 4: Set Environment Variables

Add to your `~/.zshrc`:

```bash
export SPARK_HOME="/opt/homebrew/opt/apache-spark/libexec"
export PATH="$SPARK_HOME/bin:$PATH"
export PYSPARK_PYTHON=python3
```

Apply changes:

```bash
source ~/.zshrc
```

### Step 5: Verify Installation

Check Spark version:

```bash
spark-shell --version
```

Start PySpark:

```bash
pyspark
```

You should see the Spark shell with ASCII art logo.

## Quick Test

Once in the PySpark shell, try:

```python
df = spark.range(10)
df.show()
```

Exit the shell:

```python
exit()
```

## Running Spark Applications

### Interactive Shell

Start Scala shell:
```bash
spark-shell
```

Start Python shell:
```bash
pyspark
```
