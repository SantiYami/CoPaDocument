from .app import run_app

def main():
    """
    Main function to run the application.
    """
    try:
        run_app()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_app()
