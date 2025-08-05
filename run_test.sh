#!/bin/bash

# Activate the virtual environment
# Works for most Mac/Linux and Windows setups
source venv/Scripts/activate 2>/dev/null || source venv/bin/activate

# Run the tests
pytest test_app.py
test_status=$?

# Deactivate environment
deactivate

# Exit code
if [ $test_status -eq 0 ]; then
    echo "All tests passed."
    exit 0
else
    echo "Some tests failed."
    exit 1
fi
# Ensure the script is executable
chmod +x run_test.sh

# Run the script
./run_test.sh