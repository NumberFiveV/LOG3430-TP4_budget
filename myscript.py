import os

# Get commit hashes from environment variables
good_hash = os.getenv('GOOD_HASH')
bad_hash = os.getenv('BAD_HASH')

if good_hash and bad_hash:
    os.system(f"git bisect start {bad_hash} {good_hash}")
    os.system("git bisect run python manage.py test")
    os.system("git bisect reset")
else:
    print("Error: GOOD_HASH and BAD_HASH environment variables are not set.")
