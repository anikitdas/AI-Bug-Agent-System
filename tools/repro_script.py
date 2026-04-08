def run():
    user = None
    try:
        return user.upper()
    except Exception as e:
        raise Exception("Reproduced Error: " + str(e))

if __name__ == "__main__":
    run()