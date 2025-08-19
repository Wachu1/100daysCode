def calculate_love_score(name1, name2):

    name = name1 + name2

    t = name.count("t")
    r = name.count("r")
    u = name.count("u")
    e = name.count("e")

    true_count = t + r + u + e

    l = name.count("l")
    o = name.count("o")
    v = name.count("v")
    e2 = name.count("e")

    love_count = l + o + v + e2

    total = str(true_count) + str(love_count)

    print(f"Love Score = {total}")


calculate_love_score("Dominik Vach", "Hania Navara")