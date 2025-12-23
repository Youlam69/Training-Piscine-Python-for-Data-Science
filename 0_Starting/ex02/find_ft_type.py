def all_thing_is_obj(obj: any) -> int:
    typ = type(obj).__name__

    if typ == "int":
        print("Type not found")
        return 42
    elif typ == "str":
        typ = obj + " is in the kitchen"
    else:
        typ = typ.capitalize()
    print(typ, ":", type(obj))
    return 42