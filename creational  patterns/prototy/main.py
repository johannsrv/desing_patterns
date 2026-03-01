from concrete_prototype import ConcretePrototype

def main():
    original = {
        "OS": "Linux",
        "Version": "Ubuntu 20.04",
        "Applications": ["Nginx", "MySQL", "Python"]
    }

    original_config = SystemCopy(original)
    cloned_config = original_config.clone()
    print("Original Configuration:", original_config.configuration)
    print("Cloned Configuration:", cloned_config.configuration)

if __name__ == "__main__":
    main()
