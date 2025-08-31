import smallpond

def main():
    # initialize session
    sp = smallpond.init()

    print("✅ Smallpond session initialized")
    # keep container running interactively
    import code
    code.interact(local=locals())

if __name__ == "__main__":
    main()
