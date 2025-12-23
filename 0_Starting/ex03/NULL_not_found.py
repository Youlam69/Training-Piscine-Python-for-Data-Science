def NULL_not_found(object: any) -> int:
    match object:
        case None:
            print(f"Nothing: {object} {type(object)}")
        case _ if object != object:
            print(f"Cheese: {object} {type(object)}")
        case False if type(object) is bool:
            print(f"Fake: {object} {type(object)}")
        case 0 if type(object) is int:
            print(f"Zero: {object} {type(object)}")
        case "":
            print(f"Empty: {type(object)}")
        case _:
            print("Type not Found")
            return 1
    return 0