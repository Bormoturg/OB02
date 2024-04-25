class User:
    def __init__(self, user_id, name):
        self._user_id = user_id  # Уникальный идентификатор пользователя
        self._name = name  # Имя пользователя
        self._access_level = 'user'  # Уровень доступа обычного пользователя

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def get_access_level(self):
        return self._access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'  # Уровень доступа администратора

    def add_user(self, user_list, user_id, name):
        new_user = User(user_id, name)
        user_list.append(new_user)
        print(f"User {name} added to the system.")

    def remove_user(self, user_list, user_id):
        for i, user in enumerate(user_list):
            if user.get_user_id() == user_id:
                user_list.pop(i)
                print(f"User with ID {user_id} removed from the system.")
                return
        print("User not found.")


# Пример использования
def main():
    # Создаем список пользователей
    users = []

    # Создаем администратора
    admin = Admin(1, "Alice")

    # Добавляем пользователей
    admin.add_user(users, 2, "Bob")
    admin.add_user(users, 3, "Charlie")

    # Удаляем пользователя
    admin.remove_user(users, 2)

    # Проверяем текущий список пользователей
    for user in users:
        print(f"User ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")


if __name__ == "__main__":
    main()
