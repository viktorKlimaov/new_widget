from utils import get_list_operation, get_user_operation


def main():
    items = get_list_operation()
    for i in range(5):
        print(get_user_operation(items[i]))
        print()


if __name__ == '__main__':
    main()
