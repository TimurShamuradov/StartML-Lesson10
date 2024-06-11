from session import User, Session



if __name__ == "__main__":
    user = User(
        first_name="Timur",
        last_name="Shamuradov",
        age=37
    )
    session = Session()
    session.add(user)
    session.commit()