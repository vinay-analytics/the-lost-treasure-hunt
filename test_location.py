from location import Location


village = Location(
    "Ancient Village",
    "An abandoned village."
)



forest = Location(
    "Dark Forest",
    "A dangerous forest."
)


village.add_connection(forest)


village.show_connections()